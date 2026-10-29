import os
import re
import sys
import json
import time
import unicodedata
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

BASE_URL = "https://loigiaihay.com"
START_URL = "https://loigiaihay.com/tu-dien-mon-toan-lop-9-c2298.html"
QUIZ_API_URL = "https://vungoi-api.loigiaihay.com/admin/v1/lessons/quizzes/{concept_id}"
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImxlbmdrZW5nOTYiLCJpZCI6IjVkNmUzODdlNzM4ZDYyMDFiMDhhZWRlZCIsImlzR3Vlc3QiOmZhbHNlLCJpc190ZXN0Ijp0cnVlLCJpYXQiOjE2NjczNzk4MDYsImV4cCI6MTk4Mjk0OTA2Nn0.25ypGYc-syOJRvKdqg6E0rxYmh4VaRHe8nD2ZZ89yZ4"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}

API_HEADERS = {
    "User-Agent": HEADERS["User-Agent"],
    "Origin": "https://loigiaihay.com",
    "Referer": "https://loigiaihay.com/",
    "x-access-token": API_TOKEN,
    "content-type": "application/json"
}

def sanitize_filename(name):
    # Remove accents and invalid characters for filenames
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    name = re.sub(r'[^a-zA-Z0-9_\-\s]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    return name

def fetch_quizzes_for_concept(concept_id):
    if not concept_id:
        return []
    try:
        url = QUIZ_API_URL.format(concept_id=concept_id)
        resp = requests.get(url, headers=API_HEADERS, timeout=12)
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, list):
                return data
    except Exception as e:
        print(f"    [!] Error fetching quiz for concept {concept_id}: {e}")
    return []

def clean_theory_html(main_content_tag):
    if not main_content_tag:
        return ""

    # Remove search bars, scripts, forms, quizzes (will be re-injected cleanly), ads
    for selector in [
        '.wiki-header-search',
        '#edict-frm',
        'form',
        'script',
        '#preroot',
        '.lgh-concept-quiz',
        '#root',
        'ins.adsbygoogle',
        '.box-question',
        '.choose-another-book',
        '.CommentBox',
        '.share-box',
        '.btn-feedback'
    ]:
        for el in main_content_tag.select(selector):
            el.decompose()

    # Remove section 3 heading if present (since quiz will be rendered cleanly)
    for h in main_content_tag.find_all(['h2', 'h3', 'h4']):
        text = h.get_text(strip=True).lower()
        if 'bài tập vận dụng' in text or 'bai tap van dung' in text:
            h.decompose()

    # Fix relative image URLs
    for img in main_content_tag.find_all('img'):
        src = img.get('src') or img.get('data-src') or ''
        if src:
            img['src'] = urljoin(BASE_URL, src)
        if 'data-src' in img.attrs:
            del img['data-src']
        if 'loading' in img.attrs:
            del img['loading']
        img['style'] = "max-width: 100%; height: auto; display: block; margin: 10px auto;"

    return str(main_content_tag)

def extract_text_content(items):
    if not items:
        return ""
    if isinstance(items, str):
        return items
    if isinstance(items, (int, float)):
        return str(items)
    parts = []
    if isinstance(items, list):
        for item in items:
            if isinstance(item, dict):
                val = item.get('content', '')
                if val is not None:
                    parts.append(str(val))
            elif item is not None:
                parts.append(str(item))
    elif isinstance(items, dict):
        val = items.get('content', '')
        if val is not None:
            parts.append(str(val))
    return "".join(parts)

def render_quizzes_html(quizzes):
    if not quizzes:
        return ""

    html = ['<div class="exercise-section">', '<h3 class="exercise-header">📝 BÀI TẬP VẬN DỤNG CÓ LỜI GIẢI</h3>']
    for idx, q in enumerate(quizzes):
        q_num = idx + 1
        q_obj = q.get('question', {})
        contents = q_obj.get('content', [])
        q_html = extract_text_content(contents)

        answers = q_obj.get('answers', [])
        sol_detail = q.get('solution_detail', [])
        sol_html = extract_text_content(sol_detail)

        html.append(f'<div class="quiz-item">')
        html.append(f'  <div class="quiz-title"><strong>Câu {q_num}:</strong></div>')
        html.append(f'  <div class="quiz-question-body">{q_html}</div>')

        if answers:
            html.append('  <div class="quiz-answers-grid">')
            for a_idx, ans in enumerate(answers):
                letter = chr(65 + a_idx)
                a_parts = extract_text_content(ans.get('text', []))
                html.append(f'    <div class="quiz-answer-opt"><span class="opt-label">{letter}.</span> {a_parts}</div>')
            html.append('  </div>')

        if sol_html:
            html.append('  <details class="quiz-solution-box" open>')
            html.append('    <summary><strong>💡 Lời giải chi tiết</strong></summary>')
            html.append(f'    <div class="quiz-solution-content">{sol_html}</div>')
            html.append('  </details>')

        html.append('</div>')

    html.append('</div>')
    return "\n".join(html)

def build_topic_html(topic_title, topic_index, lessons_data):
    lessons_html = []
    for l_idx, lesson in enumerate(lessons_data):
        page_break_class = "lesson-page-break" if l_idx > 0 else ""
        quizzes_html = render_quizzes_html(lesson.get('quizzes', []))
        
        lesson_block = f"""
        <article class="lesson-article {page_break_class}">
            <header class="lesson-header">
                <span class="lesson-badge">Bài {l_idx + 1}</span>
                <h2 class="lesson-title">{lesson['title']}</h2>
            </header>
            <div class="theory-section">
                {lesson['theory_html']}
            </div>
            {quizzes_html}
        </article>
        """
        lessons_html.append(lesson_block)

    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic_title} - Ôn Thi Toán 9</title>
    <!-- MathJax 3 config -->
    <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
      }},
      svg: {{ fontCache: 'global' }}
    }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root {{
            --primary: #1e3a8a;
            --primary-light: #eff6ff;
            --accent: #2563eb;
            --text-main: #1f2937;
            --text-muted: #4b5563;
            --border-color: #e5e7eb;
            --bg-quiz: #f8fafc;
            --bg-solution: #f0fdf4;
            --border-solution: #bbf7d0;
        }}

        * {{
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            color: var(--text-main);
            line-height: 1.6;
            margin: 0;
            padding: 20px 40px;
            background-color: #f3f4f6;
        }}

        .document-wrapper {{
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            padding: 40px 50px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }}

        .topic-header-banner {{
            text-align: center;
            border-bottom: 3px double var(--primary);
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}

        .topic-header-banner .doc-subtitle {{
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--accent);
            font-weight: 700;
            margin-bottom: 6px;
        }}

        .topic-header-banner h1 {{
            font-size: 26px;
            color: var(--primary);
            margin: 0 0 10px 0;
        }}

        .lesson-article {{
            margin-bottom: 40px;
        }}

        .lesson-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
            border-left: 5px solid var(--accent);
            padding-left: 14px;
            background: var(--primary-light);
            padding-top: 8px;
            padding-bottom: 8px;
            border-radius: 0 4px 4px 0;
        }}

        .lesson-badge {{
            background: var(--primary);
            color: #ffffff;
            font-size: 13px;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 4px;
            white-space: nowrap;
        }}

        .lesson-title {{
            font-size: 20px;
            color: var(--primary);
            margin: 0;
        }}

        .theory-section {{
            font-size: 16px;
            margin-bottom: 25px;
        }}

        .theory-section h3 {{
            color: #1e40af;
            font-size: 17px;
            margin-top: 18px;
            margin-bottom: 8px;
        }}

        .theory-section p {{
            margin: 6px 0;
        }}

        .exercise-section {{
            background: var(--bg-quiz);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 20px 24px;
            margin-top: 25px;
        }}

        .exercise-header {{
            font-size: 18px;
            color: var(--primary);
            margin-top: 0;
            margin-bottom: 18px;
            border-bottom: 1px solid #cbd5e1;
            padding-bottom: 8px;
        }}

        .quiz-item {{
            margin-bottom: 22px;
            padding-bottom: 18px;
            border-bottom: 1px dashed #cbd5e1;
        }}

        .quiz-item:last-child {{
            margin-bottom: 0;
            padding-bottom: 0;
            border-bottom: none;
        }}

        .quiz-title {{
            color: #1e3a8a;
            font-size: 16px;
            margin-bottom: 6px;
        }}

        .quiz-question-body p {{
            margin: 4px 0;
        }}

        .quiz-answers-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 8px 16px;
            margin: 12px 0 14px 0;
        }}

        @media (max-width: 600px) {{
            .quiz-answers-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        .quiz-answer-opt {{
            display: flex;
            align-items: baseline;
            gap: 6px;
            background: #ffffff;
            padding: 6px 10px;
            border-radius: 4px;
            border: 1px solid #e2e8f0;
        }}

        .quiz-answer-opt .opt-label {{
            font-weight: 700;
            color: var(--accent);
        }}

        .quiz-answer-opt p {{
            margin: 0;
            display: inline;
        }}

        .quiz-solution-box {{
            background: var(--bg-solution);
            border: 1px solid var(--border-solution);
            border-radius: 4px;
            padding: 10px 14px;
            margin-top: 10px;
        }}

        .quiz-solution-box summary {{
            cursor: pointer;
            color: #166534;
            font-weight: 600;
        }}

        .quiz-solution-content {{
            margin-top: 8px;
            font-size: 15px;
            color: #14532d;
        }}

        .quiz-solution-content p {{
            margin: 4px 0;
        }}

        /* Print styles */
        @media print {{
            body {{
                background: #ffffff !important;
                padding: 0 !important;
            }}

            .document-wrapper {{
                box-shadow: none !important;
                padding: 0 !important;
                max-width: 100% !important;
            }}

            .lesson-page-break {{
                page-break-before: always !important;
                break-before: page !important;
            }}

            .quiz-item {{
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }}

            .quiz-solution-box {{
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }}

            details.quiz-solution-box {{
                display: block !important;
            }}

            details.quiz-solution-box summary {{
                display: block !important;
            }}
        }}
    </style>
</head>
<body>
    <div class="document-wrapper">
        <header class="topic-header-banner">
            <div class="doc-subtitle">Tài Liệu Ôn Thi Toán 9 - Chuyên Đề &amp; Bài Tập</div>
            <h1>Chủ đề {topic_index:02d}: {topic_title}</h1>
        </header>

        {''.join(lessons_html)}
    </div>
</body>
</html>
"""
    return full_html

def crawl_loigiaihay(topic_limit=None):
    os.makedirs("output_html", exist_ok=True)
    os.makedirs("output_data", exist_ok=True)

    print(f"[*] Accessing START_URL: {START_URL}")
    resp = requests.get(START_URL, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    container = soup.find("div", id="event_1_columns")
    if not container:
        print("[!] Target container #event_1_columns not found.")
        return

    subjects = container.find_all("div", class_=lambda c: c and "subject-item" in c)
    total_found = len(subjects)
    print(f"[+] Total topics discovered: {total_found}")

    if topic_limit:
        subjects = subjects[:topic_limit]
        print(f"[*] Running in limited mode: processing first {len(subjects)} topic(s).")

    all_dataset = []
    json_path = os.path.join("output_data", "curriculum_dataset.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                all_dataset = json.load(f)
        except Exception:
            all_dataset = []

    saved_slugs = {item.get("slug") for item in all_dataset}

    for t_idx, subject in enumerate(subjects, start=1):
        h2_tag = subject.find("h2")
        strong_tag = h2_tag.find("strong") if h2_tag else None
        topic_title = strong_tag.get_text(strip=True) if strong_tag else f"Chu_de_{t_idx}"
        topic_slug = f"{t_idx:02d}_{sanitize_filename(topic_title)}"
        output_file = os.path.join("output_html", f"{topic_slug}.html")

        print(f"\n=======================================================")
        print(f"[*] [{t_idx}/{len(subjects)}] Đang xử lý Chủ đề: {topic_title}")
        print(f"=======================================================")

        if os.path.exists(output_file) and os.path.getsize(output_file) > 2000 and topic_slug in saved_slugs:
            print(f"    [i] Chủ đề đã có sẵn file HTML: {output_file}. Bỏ qua cào lại.")
            continue

        wrap_divs = subject.find_all("div", class_=lambda c: c and "wrap-width50or100" in c)
        article_links = []
        for div in wrap_divs:
            for a in div.find_all("a", href=True):
                span = a.find("span")
                link_title = span.get_text(strip=True) if span else a.get("title", a.get_text(strip=True))
                full_url = urljoin(BASE_URL, a["href"])
                article_links.append({"title": link_title, "url": full_url})

        print(f"    -> Tìm thấy {len(article_links)} bài học.")

        try:
            topic_lessons_data = []

            for a_idx, art in enumerate(article_links, start=1):
                art_title = art["title"]
                art_url = art["url"]
                print(f"    ({a_idx}/{len(article_links)}) Tải bài: {art_title}")

                # Extract concept ID from URL or page
                concept_match = re.search(r'-a(\d+)\.html', art_url)
                concept_id = concept_match.group(1) if concept_match else None

                theory_html = ""
                quizzes = []

                try:
                    art_resp = requests.get(art_url, headers=HEADERS, timeout=15)
                    if art_resp.status_code == 200:
                        art_soup = BeautifulSoup(art_resp.text, "html.parser")
                        main_content = (
                            art_soup.find(id="main-content")
                            or art_soup.find(class_="main-content")
                            or art_soup.find("div", id="box-content")
                        )

                        # Also check conceptid attribute in tag if regex failed
                        if not concept_id:
                            quiz_div = art_soup.find(attrs={"conceptid": True})
                            if quiz_div:
                                concept_id = quiz_div.get("conceptid")

                        theory_html = clean_theory_html(main_content)
                    else:
                        print(f"        [!] Lỗi tải bài học ({art_resp.status_code}): {art_url}")
                except Exception as e:
                    print(f"        [!] Ngoại lệ khi tải bài học: {e}")

                # Fetch quizzes via API
                if concept_id:
                    quizzes = fetch_quizzes_for_concept(concept_id)
                    print(f"        -> Lấy được {len(quizzes)} câu hỏi bài tập vận dụng (concept_id={concept_id}).")
                else:
                    print(f"        -> Không xác định được concept_id.")

                topic_lessons_data.append({
                    "lesson_index": a_idx,
                    "title": art_title,
                    "url": art_url,
                    "concept_id": concept_id,
                    "theory_html": theory_html,
                    "quizzes": quizzes
                })

                time.sleep(0.3)

            # Build consolidated HTML for this topic
            topic_html = build_topic_html(topic_title, t_idx, topic_lessons_data)

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(topic_html)

            print(f"[✓] Đã xuất file HTML Chủ đề: {output_file}")

            # Update dataset incrementally
            all_dataset = [item for item in all_dataset if item.get("slug") != topic_slug]
            all_dataset.append({
                "topic_index": t_idx,
                "topic_title": topic_title,
                "slug": topic_slug,
                "html_file": output_file,
                "lessons": topic_lessons_data
            })
            all_dataset.sort(key=lambda x: x.get("topic_index", 0))

            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(all_dataset, f, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"[!] Lỗi khi xử lý chủ đề {topic_title}: {e}")
            import traceback
            traceback.print_exc()

    print(f"\n[✓] Đã lưu dữ liệu JSON dự phòng hoàn chỉnh tại: {json_path}")
    print("[SUCCESS] Hoàn tất quá trình cào dữ liệu!")

if __name__ == "__main__":
    limit = 1
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "all":
            limit = None
        else:
            try:
                limit = int(sys.argv[1])
            except ValueError:
                limit = 1
    crawl_loigiaihay(topic_limit=limit)
