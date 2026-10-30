import os
import re

files_to_fix = [
    r"f:\OnThiC3\EnglishDocs\docs\lessons\chuyen_de_2_12_thi_mastery.md",
    r"f:\OnThiC3\EnglishDocs\docs\lessons\chuyen_de_4_giai_ma_bien_bao_va_giao_tiep.md",
    r"f:\OnThiC3\EnglishDocs\docs\lessons\chuyen_de_5_huong_dan_viet_doan_van_nghi_luan.md",
    r"f:\OnThiC3\EnglishDocs\docs\lessons\chuyen_de_6_trong_tam_12_units_global_success_9.md",
    r"f:\OnThiC3\EnglishDocs\docs\exams\index.md"
]

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern for GitHub alerts:
    # > [!TYPE] Title
    # > Body line 1
    # > Body line 2
    def replace_alert(match):
        alert_type = match.group(1).upper()
        first_line = match.group(2).strip()
        body = match.group(3)
        
        container_type = "info"
        if alert_type in ["TIP", "GREEN"]:
            container_type = "tip"
        elif alert_type in ["WARNING", "CAUTION", "YELLOW", "ORANGE"]:
            container_type = "warning"
        elif alert_type in ["DANGER", "RED"]:
            container_type = "danger"
        elif alert_type in ["IMPORTANT", "BLUE", "PURPLE"]:
            container_type = "info"

        # clean body lines from leading '> '
        cleaned_body = []
        for line in body.splitlines():
            line = re.sub(r"^>\s?", "", line)
            cleaned_body.append(line)
        body_text = "\n".join(cleaned_body).strip()
        
        title_text = first_line.replace("**", "").replace("*", "").strip()
        if body_text:
            return f"::: {container_type} {title_text}\n{body_text}\n:::"
        else:
            return f"::: {container_type} {title_text}\n:::"

    pattern = re.compile(r"^>\s*\[!([A-Za-z]+)\]\s*(.*?)\n((?:>.*(?:\n|$))*)", re.MULTILINE)
    new_content = pattern.sub(replace_alert, content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed alerts in: {os.path.basename(file_path)}")
