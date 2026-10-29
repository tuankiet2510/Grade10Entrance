import json
import os
import re
import sys
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

BASE_URL = "https://loigiaihay.com"
START_URL = "https://loigiaihay.com/tu-dien-mon-toan-lop-9-c2298.html"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}

def probe_loigiaihay():
    print(f"[*] Accessing category page: {START_URL}")
    resp = requests.get(START_URL, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # 1. Target the main container
    container = soup.find("div", id="event_1_columns")
    if not container:
        print("[!] Target container #event_1_columns not found. Check DOM.")
        return

    # 2. Extract topic items
    subjects = container.find_all(
        "div", class_=lambda c: c and "subject-item" in c
    )
    print(f"[+] Found {len(subjects)} topics (subject-item).")
    if not subjects:
        return

    # Inspect only the first topic
    first_subject = subjects[0]
    h2_tag = first_subject.find("h2")
    strong_tag = h2_tag.find("strong") if h2_tag else None
    subject_title = (
        strong_tag.get_text(strip=True) if strong_tag else "Unknown_Title"
    )
    print(f"[+] First topic title: {subject_title}")

    # 3. Extract lesson links inside wrap-width50or100
    wrap_divs = first_subject.find_all(
        "div", class_=lambda c: c and "wrap-width50or100" in c
    )
    article_links = []
    for div in wrap_divs:
        for a in div.find_all("a", href=True):
            span = a.find("span")
            link_title = (
                span.get_text(strip=True)
                if span
                else a.get("title", a.get_text(strip=True))
            )
            full_url = urljoin(BASE_URL, a["href"])
            article_links.append({"title": link_title, "url": full_url})

    print(
        f"[+] Found {len(article_links)} articles under topic '{subject_title}'."
    )
    if not article_links:
        return

    # 4. Probe the first lesson's main-content
    first_article = article_links[0]
    print(f"\n[*] Probing first article: {first_article['title']}")
    print(f"    URL: {first_article['url']}")

    art_resp = requests.get(first_article["url"], headers=HEADERS, timeout=15)
    art_resp.raise_for_status()
    art_soup = BeautifulSoup(art_resp.text, "html.parser")

    # Locate article body container
    main_content = (
        art_soup.find(id="main-content")
        or art_soup.find(class_="main-content")
        or art_soup.find("div", id="box-content")
    )

    if not main_content:
        print(
            "[!] Direct 'main-content' identifier missing. Capturing DOM candidates"
            "..."
        )
        candidates = [
            {"tag": tag.name, "id": tag.get("id"), "class": tag.get("class")}
            for tag in art_soup.find_all(["div", "article", "section"])
            if tag.get("id") or tag.get("class")
        ]
        with open("dom_candidates.json", "w", encoding="utf-8") as f:
            json.dump(candidates[:50], f, ensure_ascii=False, indent=2)
        print("    -> Dumped 50 container nodes to dom_candidates.json.")
        return

    # 5. Analyze DOM makeup
    tags_used = set()
    classes_used = set()
    inline_styles = set()
    images = []

    for tag in main_content.find_all(True):
        tags_used.add(tag.name)
        if tag.get("class"):
            classes_used.update(tag.get("class"))
        if tag.get("style"):
            inline_styles.add(f"<{tag.name} style='{tag.get('style')}'>")
        if tag.name == "img":
            img_src = tag.get("src") or tag.get("data-src")
            images.append({
                "src": urljoin(BASE_URL, img_src) if img_src else None,
                "attrs": dict(tag.attrs),
            })

    analysis_report = {
        "subject_title": subject_title,
        "total_articles_in_first_subject": len(article_links),
        "probed_article": first_article,
        "tags_present": sorted(list(tags_used)),
        "classes_present": sorted(list(classes_used)),
        "sample_inline_styles": sorted(list(inline_styles))[:30],
        "images_found": images,
        "has_mathjax_or_latex": bool(
            re.search(r"(\$\$|\\\(|\bsqrt\b|\bfrac\b|math-tex)", str(main_content))
        ),
    }

    os.makedirs("probe_output", exist_ok=True)
    with open(
        "probe_output/structure_analysis.json", "w", encoding="utf-8"
    ) as f:
        json.dump(analysis_report, f, ensure_ascii=False, indent=2)

    with open(
        "probe_output/raw_first_article.html", "w", encoding="utf-8"
    ) as f:
        f.write(main_content.prettify())

    print("\n[SUCCESS] Inspection data exported to directory 'probe_output/':")
    print("  1. probe_output/structure_analysis.json (Tags, classes, styles, math)")
    print("  2. probe_output/raw_first_article.html (Raw main-content HTML)")

if __name__ == "__main__":
    probe_loigiaihay()
