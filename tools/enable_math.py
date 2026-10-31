config_path = r"f:\OnThiC3\EnglishDocs\docs\.vitepress\config.mts"

with open(config_path, "r", encoding="utf-8") as f:
    content = f.read()

target = "  markdown: {\n    lineNumbers: true,"
replacement = "  markdown: {\n    math: true,\n    lineNumbers: true,"

if target in content:
    content = content.replace(target, replacement)
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Added math: true to config.mts")
else:
    # try with \r\n
    target_crlf = "  markdown: {\r\n    lineNumbers: true,"
    replacement_crlf = "  markdown: {\r\n    math: true,\r\n    lineNumbers: true,"
    if target_crlf in content:
        content = content.replace(target_crlf, replacement_crlf)
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Added math: true to config.mts (CRLF)")
    else:
        print("Target not found!")
