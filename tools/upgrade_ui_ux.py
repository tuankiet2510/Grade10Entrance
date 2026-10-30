import os
import re
import glob

def upgrade_custom_css():
    css_path = 'EnglishDocs/docs/.vitepress/theme/custom.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the old block to replace (from Headings to end of Notion-style callout blocks)
    # Using regex to match from Headings comment to before Details & Summary
    pattern = r'/\* Headings with Outfit Font \*/[\s\S]*?(?=/\* Details & Summary)'

    new_css_segment = '''/* Headings with Outfit Font */
.vp-doc h1,
.vp-doc h2,
.vp-doc h3,
.vp-doc h4 {
  font-family: 'Outfit', var(--vp-font-family-base);
  letter-spacing: -0.015em;
  font-weight: 700;
}

.vp-doc h1 {
  font-size: 2.15rem;
  line-height: 1.3;
  margin-bottom: 1.5rem;
  background: linear-gradient(135deg, var(--vp-c-text-1) 30%, var(--vp-c-brand-1));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.dark .vp-doc h1 {
  background: linear-gradient(135deg, #ffffff 40%, #60a5fa);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.vp-doc h2 {
  font-size: 1.5rem;
  margin-top: 2rem;
  margin-bottom: 1rem;
  padding-bottom: 0.4rem;
  border-bottom: 1.5px solid var(--vp-c-divider);
  color: var(--vp-c-text-1);
}

.dark .vp-doc h2 {
  color: #f8fafc;
  border-bottom: 1.5px solid rgba(255, 255, 255, 0.12);
}

.vp-doc h3 {
  font-size: 1.25rem;
  margin-top: 1.75rem;
  margin-bottom: 0.75rem;
  color: #1e40af;
  font-weight: 700;
}

.dark .vp-doc h3 {
  color: #93c5fd; /* Soft luminous sky blue with high contrast on dark background */
}

/* Text & Paragraphs */
.vp-doc p,
.vp-doc li {
  line-height: 1.75 !important;
  font-size: 1rem !important;
  color: var(--vp-c-text-1) !important;
}

/* IPA and Inline Code Highlighting - WCAG AAA Compliant */
.vp-doc :not(pre) > code {
  font-family: var(--vp-font-family-mono);
  font-size: 0.88em;
  padding: 0.18em 0.48em;
  border-radius: 6px;
  background: #f1f5f9;
  color: #0f172a;
  font-weight: 600;
  border: 1px solid #cbd5e1;
  letter-spacing: -0.01em;
}

.dark .vp-doc :not(pre) > code {
  background: #1e293b;
  color: #f8fafc; /* Crisp pure white on dark slate - 13.2:1 contrast */
  font-weight: 600;
  border: 1px solid #475569;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

/* Study4 Style Tables - Clean, Clear, High-Contrast */
.vp-doc table {
  width: 100% !important;
  display: table !important;
  border-collapse: separate !important;
  border-spacing: 0 !important;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider) !important;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03);
  margin: 1.5rem 0 !important;
}

.vp-doc th {
  background: #f8fafc !important;
  font-weight: 700 !important;
  color: #0f172a !important;
  padding: 0.85rem 1rem !important;
  border-bottom: 2px solid #cbd5e1 !important;
  text-align: left;
  font-size: 0.92rem;
}

.vp-doc td {
  padding: 0.85rem 1rem !important;
  border-bottom: 1px solid #e2e8f0 !important;
  font-size: 0.92rem;
  line-height: 1.6;
  color: #1e293b;
}

.vp-doc tr:last-child td {
  border-bottom: none !important;
}

.vp-doc tr:nth-child(even) {
  background: #f8fafc;
}

.vp-doc tr:hover {
  background: #f1f5f9;
}

/* Dark Mode Tables */
.dark .vp-doc table {
  border-color: rgba(255, 255, 255, 0.12) !important;
  background: #0b0f19;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
}

.dark .vp-doc th {
  background: #1e293b !important;
  color: #f8fafc !important;
  border-bottom: 2px solid rgba(255, 255, 255, 0.15) !important;
}

.dark .vp-doc td {
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
  color: #f1f5f9 !important;
}

.dark .vp-doc tr:nth-child(even) {
  background: #0f172a !important;
}

.dark .vp-doc tr:nth-child(odd) {
  background: #0b0f19 !important;
}

.dark .vp-doc tr:hover {
  background: rgba(59, 130, 246, 0.1) !important;
}

/* BLOCKQUOTES - High Contrast in Both Themes */
.vp-doc blockquote {
  margin: 1.25rem 0;
  padding: 1rem 1.35rem;
  border-left: 4px solid var(--vp-c-brand-1);
  background: #f8fafc;
  border-radius: 0 10px 10px 0;
  color: #0f172a;
  font-style: normal;
  border-top: 1px solid #e2e8f0;
  border-right: 1px solid #e2e8f0;
  border-bottom: 1px solid #e2e8f0;
}

.dark .vp-doc blockquote {
  background: #111827;
  border-left-color: #60a5fa;
  color: #f1f5f9;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  border-right: 1px solid rgba(255, 255, 255, 0.08);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

/* VITEPRESS CUSTOM CONTAINERS (Clean, High-Contrast, WCAG AAA) */
.vp-doc .custom-block {
  margin: 1.5rem 0 !important;
  padding: 1.1rem 1.4rem !important;
  border-radius: 12px !important;
  border-left-width: 5px !important;
  font-size: 0.96rem !important;
  line-height: 1.7 !important;
}

.vp-doc .custom-block .custom-block-title {
  font-family: 'Outfit', var(--vp-font-family-base) !important;
  font-weight: 700 !important;
  font-size: 1.02rem !important;
  margin-bottom: 0.5rem !important;
  display: flex !important;
  align-items: center !important;
  gap: 0.45rem !important;
}

/* INFO CONTAINER (Blue) */
:root:not(.dark) .vp-doc .custom-block.info {
  background: #eff6ff !important;
  border-left-color: #2563eb !important;
  border-top: 1px solid #dbeafe !important;
  border-right: 1px solid #dbeafe !important;
  border-bottom: 1px solid #dbeafe !important;
  color: #1e3a8a !important;
}
:root:not(.dark) .vp-doc .custom-block.info .custom-block-title {
  color: #1d4ed8 !important;
}

.dark .vp-doc .custom-block.info {
  background: rgba(30, 58, 138, 0.25) !important;
  border-left-color: #60a5fa !important;
  border-top: 1px solid rgba(59, 130, 246, 0.2) !important;
  border-right: 1px solid rgba(59, 130, 246, 0.2) !important;
  border-bottom: 1px solid rgba(59, 130, 246, 0.2) !important;
  color: #e0f2fe !important;
}
.dark .vp-doc .custom-block.info .custom-block-title {
  color: #93c5fd !important;
}

/* TIP CONTAINER (Green / Emerald) */
:root:not(.dark) .vp-doc .custom-block.tip {
  background: #f0fdf4 !important;
  border-left-color: #16a34a !important;
  border-top: 1px solid #dcfce7 !important;
  border-right: 1px solid #dcfce7 !important;
  border-bottom: 1px solid #dcfce7 !important;
  color: #14532d !important;
}
:root:not(.dark) .vp-doc .custom-block.tip .custom-block-title {
  color: #15803d !important;
}

.dark .vp-doc .custom-block.tip {
  background: rgba(6, 78, 59, 0.25) !important;
  border-left-color: #34d399 !important;
  border-top: 1px solid rgba(16, 185, 129, 0.2) !important;
  border-right: 1px solid rgba(16, 185, 129, 0.2) !important;
  border-bottom: 1px solid rgba(16, 185, 129, 0.2) !important;
  color: #d1fae5 !important;
}
.dark .vp-doc .custom-block.tip .custom-block-title {
  color: #6ee7b7 !important;
}

/* WARNING CONTAINER (Amber / Yellow) */
:root:not(.dark) .vp-doc .custom-block.warning {
  background: #fffbeb !important;
  border-left-color: #d97706 !important;
  border-top: 1px solid #fef3c7 !important;
  border-right: 1px solid #fef3c7 !important;
  border-bottom: 1px solid #fef3c7 !important;
  color: #78350f !important;
}
:root:not(.dark) .vp-doc .custom-block.warning .custom-block-title {
  color: #b45309 !important;
}

.dark .vp-doc .custom-block.warning {
  background: rgba(120, 53, 15, 0.25) !important;
  border-left-color: #fbbf24 !important;
  border-top: 1px solid rgba(245, 158, 11, 0.2) !important;
  border-right: 1px solid rgba(245, 158, 11, 0.2) !important;
  border-bottom: 1px solid rgba(245, 158, 11, 0.2) !important;
  color: #fef3c7 !important;
}
.dark .vp-doc .custom-block.warning .custom-block-title {
  color: #fde68a !important;
}

/* DANGER CONTAINER (Red / Crimson) */
:root:not(.dark) .vp-doc .custom-block.danger {
  background: #fef2f2 !important;
  border-left-color: #dc2626 !important;
  border-top: 1px solid #fee2e2 !important;
  border-right: 1px solid #fee2e2 !important;
  border-bottom: 1px solid #fee2e2 !important;
  color: #881337 !important;
}
:root:not(.dark) .vp-doc .custom-block.danger .custom-block-title {
  color: #b91c1c !important;
}

.dark .vp-doc .custom-block.danger {
  background: rgba(127, 29, 29, 0.25) !important;
  border-left-color: #f87171 !important;
  border-top: 1px solid rgba(239, 68, 68, 0.2) !important;
  border-right: 1px solid rgba(239, 68, 68, 0.2) !important;
  border-bottom: 1px solid rgba(239, 68, 68, 0.2) !important;
  color: #fee2e2 !important;
}
.dark .vp-doc .custom-block.danger .custom-block-title {
  color: #fca5a5 !important;
}

'''

    new_content, count = re.subn(pattern, new_css_segment, content, count=1)
    if count == 0:
        print("Warning: Pattern not found in custom.css!")
        return False
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully upgraded custom.css!")
    return True

def upgrade_quiz_item():
    quiz_path = 'EnglishDocs/docs/.vitepress/theme/components/QuizItem.vue'
    with open(quiz_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Enhance dark mode styles for QuizItem components
    # Specifically target .quiz-target-char, .quiz-inline-code, .opt-ipa, .prompt-code, .explanation-body
    replacements = [
        (
            ''':deep(.quiz-target-char) {
  text-decoration: underline 2.5px var(--vp-c-brand-1);
  text-underline-offset: 3px;
  color: var(--vp-c-brand-1);
  font-weight: 700;
}''',
            ''':deep(.quiz-target-char) {
  text-decoration: underline 2.5px #2563eb;
  text-underline-offset: 3px;
  color: #1e40af;
  font-weight: 700;
}

.dark :deep(.quiz-target-char) {
  text-decoration-color: #38bdf8;
  color: #38bdf8;
}'''
        ),
        (
            ''':deep(.quiz-inline-code) {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  padding: 0.12rem 0.38rem;
  border-radius: 5px;
  font-size: 0.88em;
  font-family: var(--vp-font-family-mono);
}''',
            ''':deep(.quiz-inline-code) {
  background: #f1f5f9;
  color: #0f172a;
  border: 1px solid #cbd5e1;
  padding: 0.12rem 0.38rem;
  border-radius: 5px;
  font-size: 0.88em;
  font-family: var(--vp-font-family-mono);
}

.dark :deep(.quiz-inline-code) {
  background: #1e293b;
  color: #f8fafc;
  border-color: #475569;
}'''
        ),
        (
            '''.opt-ipa {
  font-size: 0.75rem;
  color: var(--vp-c-brand-1);
  font-family: var(--vp-font-family-mono);
}''',
            '''.opt-ipa {
  font-size: 0.75rem;
  color: #1e40af;
  font-family: var(--vp-font-family-mono);
}

.dark .opt-ipa {
  color: #38bdf8;
}'''
        ),
        (
            '''.prompt-code {
  background: var(--vp-c-bg);
  padding: 0.2rem 0.5rem;
  border-radius: 6px;
  color: var(--vp-c-brand-1);
  font-weight: 600;
}''',
            '''.prompt-code {
  background: #f1f5f9;
  padding: 0.2rem 0.5rem;
  border-radius: 6px;
  color: #1e40af;
  font-weight: 600;
  border: 1px solid #cbd5e1;
}

.dark .prompt-code {
  background: #1e293b;
  color: #38bdf8;
  border-color: #475569;
}'''
        ),
        (
            '''.explanation-body {
  margin-top: 0.75rem;
  padding: 0.95rem 1.15rem;
  background: var(--vp-c-bg);
  border-radius: 10px;
  border: 1px solid var(--vp-c-divider);
  font-size: 0.9rem;
  line-height: 1.65;
  color: var(--vp-c-text-1);
}''',
            '''.explanation-body {
  margin-top: 0.75rem;
  padding: 0.95rem 1.15rem;
  background: #f8fafc;
  border-radius: 10px;
  border: 1px solid #cbd5e1;
  font-size: 0.9rem;
  line-height: 1.65;
  color: #0f172a;
}

.dark .explanation-body {
  background: #0f172a;
  border-color: #334155;
  color: #f8fafc;
}'''
        )
    ]

    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"Warning in QuizItem.vue: Target snippet not found:\n{old[:40]}...")

    with open(quiz_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully upgraded QuizItem.vue!")
    return True

def convert_lesson_alerts():
    type_map = {
        'BLUE': 'info',
        'GREEN': 'tip',
        'YELLOW': 'warning',
        'RED': 'danger'
    }

    files = glob.glob('EnglishDocs/docs/lessons/*.md')
    total_converted = 0

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()

        new_lines = []
        i = 0
        file_conversions = 0

        while i < len(lines):
            line = lines[i]
            m = re.match(r'^>\s*\[!(BLUE|RED|GREEN|YELLOW)\]\s*(.*)$', line)
            if m:
                alert_type = type_map[m.group(1)]
                raw_title = m.group(2).strip()
                # Clean title: strip bold asterisks and trailing colon
                title = re.sub(r'^\*\*|\*\*$', '', raw_title)
                title = re.sub(r':$', '', title).strip()

                new_lines.append(f'::: {alert_type} {title}')
                i += 1
                while i < len(lines) and lines[i].startswith('>'):
                    # Strip leading '>' and optional space
                    content_line = lines[i][1:]
                    if content_line.startswith(' '):
                        content_line = content_line[1:]
                    new_lines.append(content_line)
                    i += 1
                new_lines.append(':::')
                file_conversions += 1
            else:
                new_lines.append(line)
                i += 1

        if file_conversions > 0:
            total_converted += file_conversions
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines) + '\n')
            print(f"Converted {file_conversions} alerts in {os.path.basename(file_path)}")

    print(f"Total alerts converted across all lessons: {total_converted}")

if __name__ == '__main__':
    upgrade_custom_css()
    upgrade_quiz_item()
    convert_lesson_alerts()

