# Cào Dữ Liệu Toán 9 Loigiaihay

**Created:** 10/20/2026 10:00:40  
**Updated:** 10/20/2026 10:03:40  
**Exported:** 10/20/2026 10:04:49  
**Link:** [https://gemini.google.com/app/91872e307a8d43bf](https://gemini.google.com/app/91872e307a8d43bf)  

## Gemini:

> 10/20/2026 10:03:40

> **Thinking steps**
>
> **Translated the original response**
>
> Translated the prior response from an unknown language into English, ensuring that all concepts and instructions could be used as an input for the agent.

# Technical Specification & Agent Workflow: Math Scraper

---

## 1. Output Format Recommendation for Print-Ready Delivery

When scraping secondary school mathematics content featuring MathJax/LaTeX formulas, geometric diagrams, charts, inline color emphasis, and typographical tags (`<b>`, `<i>`, `<u>`), **Standalone HTML5 paired with an intermediate JSON backup** is the optimal format. Direct conversions to Markdown or DOCX during initial scraping frequently corrupt LaTeX delimiters, break equation alignments, or strip inline color styling.

### Advantages of Standalone HTML5
* **Preserves Complete Typography & Inline Styles:** Directly retains `style="color:..."`, highlight backgrounds, boxed definitions, and tags (`<b>`, `<strong>`, `<i>`, `<u>`, `<sub>`, `<sup>`, `<table>`).
* **Accurate Math Rendering:** Embeds the MathJax CDN inside `<head>`, allowing the browser or headless renderer to compile raw TeX/LaTeX expressions into crisp mathematical typography.
* **Self-Contained Offline Portability:** Relative image paths (`/uploads/...`) are resolved to absolute URLs or embedded as Base64 data URIs.
* **Print Engine Integration (`@media print`):** Enables native browser printing (`Ctrl + P` to PDF) or headless PDF conversion (e.g., via Playwright/Puppeteer) using:
  * `page-break-before: always;` / `page-break-after: always;` to paginate each lesson onto clean page boundaries.
  * `-webkit-print-color-adjust: exact; print-color-adjust: exact;` to enforce background colors and text styling in physical print or PDF exports.

---

## 2. Python Probe Script (`probe.py`)

Run this probe script first. It hits the category page, extracts the first topic, discovers the first lesson URL, isolates `#main-content`, and exports DOM structural diagnostics and raw HTML to `probe_output/` for inspection.

`​`​`python
import json
import os
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

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
`​`​`

---

## 3. Agent Task Directive (Agentic Workflow Prompt)

Copy and feed the prompt below into the coding agent. It instructs the agent to execute a self-correcting feedback loop: probe, analyze, refine on one topic, and scale to full execution.

`​`​`markdown
# TASK: BUILD & REFINE A PRINT-READY MATH CRAWLING PIPELINE (LOIGIAIHAY.COM)

## OBJECTIVE
Crawl mathematics curriculum content from:
`https://loigiaihay.com/tu-dien-mon-toan-lop-9-c2298.html`

Target Elements:
1. Target container: `<div class="box clearfix font-opensans-b font-16" id="event_1_columns">`.
2. For each `<div class="subject-item no-bg">`:
   - Topic Title: Text of `<strong>` inside `<h2>` (e.g., "Phương trình bậc nhất hai ẩn").
   - Lesson Links: All `<a>` tags inside `<div class="wrap-width50or100">`.
3. Fetch the full content of each lesson link from its primary content area (`main-content`).
4. Output Requirement: Consolidate all lessons belonging to a single Topic into **one single, standalone HTML document** (e.g., `01_Phuong_trinh_bac_nhat_hai_an.html`). The file must include print-optimized CSS (`@media print`), retain full text styling (`<b>, <i>, <u>`), colored inline text, tables, MathJax rendering, and properly resolved diagrams/images.

---

## REQUIRED EXECUTION PROTOCOL (SELF-REFINING AGENTIC LOOP)
Do not crawl the full site immediately. Execute the following phases sequentially:

### STAGE 1: Execute Initial Probe
1. Create and execute `probe.py`.
2. Restrict extraction to the catalog page, the first topic item, and **only the first article link** (`/phuong-trinh-bac-nhat-hai-an-la-gi-cach-xac-dinh-phuong-trinh-bac-nhat-hai-an-li-thuyet-va-bai-tap-a183395.html`).
3. Extract `main-content`, writing the raw HTML to `probe_output/raw_first_article.html` and metadata diagnostics to `probe_output/structure_analysis.json`.
4. Run the script via the terminal.

### STAGE 2: Inspect Diagnostics & DOM Structure
Read and evaluate the generated artifacts in `probe_output/`:
1. **Extraneous Elements & Advertisements:** Identify classes/IDs for ads, share widgets, related article sidebars, and comments (e.g., `.box-question`, `.choose-another-book`, `ins.adsbygoogle`, `.CommentBox`) that must be stripped via `.decompose()`.
2. **Image Sources:** Verify whether images use `src`, `data-src`, or lazy loading attributes. Verify whether paths are relative (`/uploads/...`) or absolute.
3. **Formulas & Math Syntax:** Check whether equations are formatted via MathJax delimiters (`\( ... \)`, `$$ ... $$`), custom spans (e.g., `.math-tex`), or embedded raster images.
4. **Formatting & Colors:** Verify preserved inline CSS attributes (`color`, `background-color`, borders, definitions, formula highlight callouts).

### STAGE 3: Implement Refined Crawler & Run Single-Topic Pilot
Based on Stage 2 diagnostics, implement `crawler.py`:
1. **DOM Cleaning (Sanitization):** Decompose ads, navigation cruft, and external scripts while preserving `<b>`, `<strong>`, `<i>`, `<em>`, `<u>`, `<sub>`, `<sup>`, `<table>`, `<ul>`, `<ol>`, and necessary inline style attributes.
2. **Image Normalization:** Convert all image sources to absolute URLs (`https://loigiaihay.com/...`), remove `loading="lazy"` tags, and apply CSS `max-width: 100%; height: auto;`.
3. **Consolidation Template:**
   - Generate a single HTML5 template per topic.
   - Inject the MathJax CDN script into `<head>`:
     `<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>`
   - Define print-optimized CSS (`@media print`):
     - `page-break-before: always;` between consecutive lessons.
     - `-webkit-print-color-adjust: exact; print-color-adjust: exact;` to preserve colored highlight boxes on paper and PDF.
     - Clean typography and clear heading hierarchies.
4. **Pilot Run:** Execute `crawler.py` restricted to **Topic 1 only**. Inspect the generated HTML file to verify equation rendering, image loading, pagination boundaries, and visual cleanliness.

### STAGE 4: Full Deployment
Once Topic 1 passes verification:
1. Lift the topic limiter and iterate through all `subject-item` nodes under `#event_1_columns`.
2. Apply reasonable request delays (`time.sleep`) and retry logic with timeouts.
3. Save each consolidated topic to `output_html/<topic_slug>.html`, and export a structured dataset backup to `output_data/curriculum_dataset.json`.
`​`​`

---

## 4. Key Target DOM Specifics & Sanitization Notes

* **Ancillary Selectors:** `loigiaihay.com` frequently injects curriculum textbook switchers (`.choose-another-book` for Cánh Diều, Kết Nối Tri Thức, Chân Trời Sáng Tạo), question recommendation sidebars (`.box-question`), and comment containers (`.CommentBox`) inside or directly adjacent to the content container. Decompose these explicitly.
* **Print Color Preservation:** By default, WebKit and Blink print engines suppress background fills to reduce ink usage. The inclusion of `print-color-adjust: exact;` in the stylesheet is mandatory to keep theorem highlight backgrounds and colored annotation boxes intact.

Would you like the standalone HTML/CSS print template with embedded MathJax configuration pre-built for the agent to use directly?

Powered by Gemini Exporter (https://www.ai-chat-exporter.com)
