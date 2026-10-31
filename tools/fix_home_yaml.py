home_path = r"f:\OnThiC3\EnglishDocs\docs\index.md"
with open(home_path, "r", encoding="utf-8") as f:
    content = f.read()

target = "    details: Sổ tay công thức & phương trình tích hợp 3 phân môn: Động lượng & Thấu kính, Dãy hoạt động kim loại & Hóa hữu cơ, Di truyền Mendel & Cơ chế ADN-Protein."
replacement = '    details: "Sổ tay công thức & phương trình tích hợp 3 phân môn: Động lượng & Thấu kính, Dãy hoạt động kim loại & Hóa hữu cơ, Di truyền Mendel & Cơ chế ADN-Protein."'

content = content.replace(target, replacement)
with open(home_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed YAML quote in index.md")

