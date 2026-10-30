import re

config_path = r"f:\OnThiC3\EnglishDocs\docs\.vitepress\config.mts"
with open(config_path, "r", encoding="utf-8") as f:
    config_content = f.read()

config_content = config_content.replace(
    "else if (f.rawName.startsWith('chuyen_de_6')) gKey = 'Phần 6: Trọng Tâm 12 Units SGK Lớp 9'",
    "else if (f.rawName.startsWith('chuyen_de_6') || f.rawName.startsWith('unit_')) gKey = 'Phần 6: 12 Units SGK Global Success 9'"
)

with open(config_path, "w", encoding="utf-8") as f:
    f.write(config_content)
print("Updated config.mts")

lessons_path = r"f:\OnThiC3\EnglishDocs\docs\.vitepress\data\lessons.data.ts"
with open(lessons_path, "r", encoding="utf-8") as f:
    lessons_content = f.read()

lessons_content = lessons_content.replace(
    "else if (fileName.startsWith('chuyen_de_6')) catKey = 'chuyen_de_6'",
    "else if (fileName.startsWith('chuyen_de_6') || fileName.startsWith('unit_')) catKey = 'chuyen_de_6'"
)

with open(lessons_path, "w", encoding="utf-8") as f:
    f.write(lessons_content)
print("Updated lessons.data.ts")
