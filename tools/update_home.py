home_path = r"f:\OnThiC3\EnglishDocs\docs\index.md"
with open(home_path, "r", encoding="utf-8") as f:
    home_content = f.read()

old_actions = """    - theme: alt
      text: Tiếng Anh 9 🇬🇧
      link: /catalog
    - theme: alt
      text: Luyện Đề Thi Thử 🎯
      link: /exams/"""

new_actions = """    - theme: alt
      text: Tiếng Anh 9 🇬🇧
      link: /catalog
    - theme: alt
      text: KHTN 9 (Lý - Hóa - Sinh) 🔬
      link: /science/
    - theme: alt
      text: Luyện Đề Thi Thử 🎯
      link: /exams/"""

home_content = home_content.replace(old_actions, new_actions)

old_features = """features:
  - icon: 📐
    title: 12 Chuyên Đề & 48 Bài Toán 9
    details: Phân loại theo cấu trúc thi vào 10 THPT công lập. Rút gọn căn thức, Hệ phương trình, Viète, Parabol, Bất đẳng thức đến Lượng giác và Hình học phẳng.
  - icon: 📖
    title: Ngữ Văn 9 Đổi Mới GDPT 2018
    details: Phương pháp đạt điểm tối đa phần Đọc hiểu ngữ liệu ngoài SGK, công thức viết đoạn văn NLXH 200 chữ và tài liệu phân tích tác phẩm thơ/truyện hiện đại.
  - icon: 🇬🇧
    title: Tiếng Anh 9 Chuẩn Global Success
    details: Hệ thống hóa từ vựng 12 Units, 4 chuyên đề ngữ pháp cốt lõi (Wh+to V, Phrasal verbs, So sánh kép, Modal verbs) và mẹo ngữ âm - trọng âm."""

new_features = """features:
  - icon: 📐
    title: 12 Chuyên Đề & 48 Bài Toán 9
    details: Phân loại theo cấu trúc thi vào 10 THPT công lập. Sổ tay toàn bộ công thức Toán 9, Rút gọn căn thức, Hệ phương trình, Viète, Parabol, Bất đẳng thức đến Lượng giác và Hình học phẳng.
  - icon: 📖
    title: Ngữ Văn 9 Đổi Mới GDPT 2018
    details: Sổ tay kiến thức 10 bài học SGK Kết nối tri thức, phương pháp Đọc hiểu ngữ liệu ngoài SGK, công thức viết đoạn văn NLXH 200 chữ và phân tích tác phẩm.
  - icon: 🇬🇧
    title: Tiếng Anh 9 Chuẩn Global Success
    details: Sổ tay ghi chú 12 Units SGK, toàn bộ chuyên đề ngữ pháp then chốt (Wh+to V, Phrasal verbs, So sánh kép, Modal verbs) và quy tắc ngữ âm - trọng âm.
  - icon: 🔬
    title: Khoa Học Tự Nhiên 9 (Lý - Hóa - Sinh)
    details: Sổ tay công thức & phương trình tích hợp 3 phân môn: Động lượng & Thấu kính, Dãy hoạt động kim loại & Hóa hữu cơ, Di truyền Mendel & Cơ chế ADN-Protein."""

home_content = home_content.replace(old_features, new_features)

with open(home_path, "w", encoding="utf-8") as f:
    f.write(home_content)
print("Updated index.md successfully!")
