# 🎓 Cẩm Nang Ôn Thi Vào 10 - Grade 10 Entrance Portal

> Hệ thống tài liệu ôn luyện tuyển sinh vào lớp 10 toàn diện, chuẩn hóa theo chương trình GDPT mới (Toán 9 & Tiếng Anh 9). Nền tảng được xây dựng theo kiến trúc **Docs-as-Code** (VitePress + Vue 3), hỗ trợ giao diện responsive tối ưu cho thiết bị di động (iPhone X, iPhone 12/13/14/15, iPad, Desktop) và xuất bản in ấn chuẩn mực.

🌐 **Website Trực Tuyến (GitHub Pages):**  
👉 **[https://tuankiet2510.github.io/Grade10Entrance/](https://tuankiet2510.github.io/Grade10Entrance/)**

---

## 📌 Tổng Quan Hệ Thống Tài Liệu

### 📐 1. Môn Toán Lớp 9 (Chương Trình Mới)
* **48 Chuyên đề trọng tâm:** Đầy đủ từ Phương trình, Hệ phương trình, Căn bậc hai, Căn bậc ba, Bất đẳng thức đến Lượng giác, Đường tròn, Tứ giác nội tiếp và Hình khối không gian.
* **257 Bài học lý thuyết:** Khái niệm, công thức, phương pháp giải toán rõ ràng, không chứa nội dung máy móc AI.
* **856+ Bài tập vận dụng:** Đầy đủ 4 phương án trắc nghiệm chuẩn mực cùng **hộp lời giải chi tiết từng bước** (`solution_detail`).
* **Hiển thị công thức MathJax 3:** Kết xuất mượt mà trên Safari iOS, Chrome, Firefox, không bị tràn hay vỡ ký hiệu.
* **17 Bộ đề thi & Chuyên đề PDF chất lượng cao:**
  * Đề thi tuyển sinh chính thức Sở GD&ĐT Quảng Ngãi (2023 - 2024, 2025 - 2026, 2026 - 2027) & Đề chuyên Toán Lê Khiết.
  * Đề thi tuyển sinh các tỉnh Lâm Đồng, Vĩnh Long, Đà Nẵng, Hà Nội (Lômônôxốp, Lương Thế Vinh).
  * Chuyên đề Bất Đẳng Thức chọn lọc, Hình học thi chuyên và Nguyên lý Bất Biến trong suy luận logic.

### 🇬🇧 2. Môn Tiếng Anh Lớp 9 (Global Success & Đề Thi)
* **Phần 1 - Ngữ âm & Trọng âm:** Thần chú nhớ phát âm `/s/`, `/es/`, `/ed/`, nguyên âm và quy tắc trọng âm 2, 3 âm tiết.
* **Phần 2 - Ngữ pháp & Cấu trúc:** 12 thì trọng tâm, câu điều kiện, câu bị động, câu gián tiếp, mệnh đề quan hệ, câu hỏi đuôi, động từ khuyết thiếu, mạo từ và giới từ.
* **Phần 3 - Từ vựng & Cụm từ:** Phrasal Verbs, Collocations, Từ đồng nghĩa - trái nghĩa và trọng tâm 12 Units Global Success 9.
* **Phần 4, 5 - Kỹ năng mở rộng:** Giải mã biển báo giao tiếp thực tế và phương pháp viết đoạn văn nghị luận xã hội.
* **Bộ đề luyện thi tương tác (26 Đề thi thử):**
  * Đề thi chính thức Sở GD&ĐT các năm.
  * Bộ đề Form 36 câu (Quảng Ngãi) & Form 45 câu chuẩn tuyển sinh.
  * Hệ thống làm bài trắc nghiệm tương tác: bấm giờ thi, nộp bài, tính điểm và xem giải thích tức thì.

---

## 📱 Thiết Kế Đáp Ứng Chuẩn Mobile (iPhone X, iPhone 12/13/14+)
* **Apple Safe Area Insets:** Bố cục tự động căn lề theo `env(safe-area-inset-top)` và `env(safe-area-inset-bottom)`, tránh bị che khuất bởi tai thỏ (Notch) hay thanh vuốt Home.
* **Chống tràn ngang:** Bảng biểu dữ liệu (`table`) và công thức toán học (`MathJax`) tự động bật thanh cuộn ngang cảm ứng (`-webkit-overflow-scrolling: touch`).
* **Chuẩn kích thước vùng chạm (Touch Targets):** Tất cả các nút bấm, thẻ bài tập và liên kết đều đạt tối thiểu `44x44px` theo Apple Human Interface Guidelines.
* **Bản in ấn thông minh (`@media print`):** Tự động ngắt trang bài học (`page-break-before: always`), giữ nguyên màu sắc highlight khi xuất ra PDF.

---

## 🛠️ Cấu Trúc Mã Nguồn

```text
OnThiC3/
├── .github/
│   └── workflows/
│       └── deploy.yml            # CI/CD tự động build & deploy lên GitHub Pages
├── EnglishDocs/                  # Nền tảng Docs-as-Code (VitePress)
│   ├── docs/
│   │   ├── .vitepress/           # Cấu hình VitePress, theme và custom CSS
│   │   ├── math/                 # 48 Markdown trang chuyên đề Toán tích hợp
│   │   ├── lessons/              # Hệ thống lý thuyết Tiếng Anh
│   │   ├── exams/                # 26 Bộ đề thi trắc nghiệm Tiếng Anh
│   │   ├── public/               # Tài nguyên tĩnh (math-topics HTML, math-pdf)
│   │   ├── catalog.md            # Mục lục tổng quan
│   │   └── index.md              # Trang chủ cổng luyện thi
│   └── package.json
├── MathDocs/                     # Kho đề thi và chuyên đề Toán gốc (PDF)
├── output_html/                  # 48 Tệp HTML chuyên đề Toán 9 độc lập
├── output_data/                  # Dữ liệu JSON dự phòng (curriculum_dataset.json)
├── crawler.py                    # Script cào và chuẩn hóa dữ liệu
└── README.md
```

---

## 🚀 Hướng Dẫn Phát Triển Cục Bộ (Local Development)

```bash
# 1. Cài đặt dependencies
cd EnglishDocs
npm install

# 2. Chạy môi trường xem thử cục bộ
npm run docs:dev

# 3. Đóng gói bản phát hành sản phẩm
npm run docs:build
npm run docs:preview
```

---

## 📜 Giấy Phép & Tác Quyền
Dự án được xây dựng và chia sẻ phục vụ mục đích học tập, ôn luyện thi vào lớp 10 THPT. Dữ liệu đề thi và câu hỏi được tổng hợp và chuẩn hóa từ các nguồn chính thống và Sở GD&ĐT.
