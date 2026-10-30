import os
import re
import glob

def clean_file_content(content):
    # Mapping of pretentious AI slops / buzzwords to clean, modest, natural educational Vietnamese
    replacements = [
        # Titles & Headers
        (r'CẨM NANG 10 CẤU TRÚC BIẾN ĐỔI CÂU \(SENTENCE TRANSFORMATION MASTERY\) ÔN THI VÀO 10', '10 Cấu Trúc Viết Lại Câu Trọng Tâm Ôn Thi Vào Lớp 10'),
        (r'CẨM NANG GIỚI TỪ \(PREPOSITIONS: TIME, PLACE & COLLOCATIONS\) ÔN THI VÀO 10', 'Chuyên Đề Giới Từ Trọng Tâm Ôn Thi Vào Lớp 10'),
        (r'CẨM NANG MẠO TỪ \(ARTICLES: A, AN, THE & ZERO ARTICLE\) ÔN THI VÀO 10', 'Chuyên Đề Mạo Từ Trọng Tâm Ôn Thi Vào Lớp 10'),
        (r'CẨM NANG TỪ ĐỒNG NGHĨA & TRÁI NGHĨA \(SYNONYMS & ANTONYMS MASTERY\)', 'Chuyên Đề Từ Đồng Nghĩa & Trái Nghĩa'),
        (r'CẨM NANG 50 CỤM ĐỘNG TỪ \(PHRASAL VERBS\) TỦ ÔN THI VÀO 10', '50 Cụm Động Từ Thường Gặp Ôn Thi Vào Lớp 10'),
        (r'CẨM NANG VIẾT ĐOẠN VĂN 100 - 120 TỪ THI VÀO 10', 'Hướng Dẫn Viết Đoạn Văn 100 - 120 Từ Thi Vào Lớp 10'),
        (r'Cẩm Nang Phương Pháp', 'Tài Liệu Phương Pháp Học Tập'),
        (r'Cẩm Nang Ôn Thi Vào 10', 'Tài Liệu Ôn Tập Vào Lớp 10'),
        (r'Cẩm nang ôn thi vào 10', 'Tài liệu ôn thi vào lớp 10'),
        (r'cẩm nang ôn thi vào 10', 'tài liệu ôn thi vào lớp 10'),
        (r'Cẩm nang', 'Tài liệu'),
        (r'cẩm nang', 'tài liệu'),

        # English mastery buzzwords in headings
        (r'WORD STRESS MASTERY', 'Quy Tắc Trọng Âm'),
        (r'QUESTION TAGS MASTERY', 'Câu Hỏi Đuôi'),
        (r'MODAL VERBS MASTERY', 'Động Từ Khuyết Thiếu'),
        (r'RELATIVE CLAUSES MASTERY', 'Mệnh Đề Quan Hệ'),
        (r'SYNONYMS & ANTONYMS MASTERY', 'Từ Đồng Nghĩa & Trái Nghĩa'),
        (r'SENTENCE TRANSFORMATION MASTERY', 'Viết Lại Câu'),
        (r'\bMASTERY\b', 'Trọng Tâm'),

        # Exaggerated claims & buzzwords
        (r'BẢN CHẤT VÀ NGUYÊN TẮC CỐT LÕI', 'Kiến thức trọng tâm'),
        (r'BẢN CHẤT VÀ NGUYÊN TẮC', 'Kiến thức trọng tâm'),
        (r'BẢN CHẤT CỐT LÕI', 'Kiến thức trọng tâm'),
        (r'BẢN CHẤT', 'Kiến thức'),
        (r'QUY TẮC BẤT BIẾN CỦA BỊ ĐỘNG', 'Quy tắc chuyển sang câu bị động'),
        (r'QUY TẮC BẤT BIẾN', 'Quy tắc cơ bản'),
        (r'2 QUY TẮC SỐNG CÒN', '2 Quy tắc quan trọng'),
        (r'3 QUY TẮC VÀNG', '3 Quy tắc cơ bản'),
        (r'4 QUY TẮC VÀNG', '4 Quy tắc cơ bản'),
        (r'VỊ TRÍ VÀNG', 'Vị trí thường gặp'),
        (r'BẮT MẠCH TỪ LOẠI', 'Xác định từ loại trong câu'),
        (r'CÂU THẦN CHÚ TIẾNG VIỆT BẤT HỦ', 'Mẹo ghi nhớ bằng tiếng Việt'),
        (r'BỘ THẦN CHÚ TIẾNG VIỆT BẤT HỦ', 'Mẹo ghi nhớ bằng tiếng Việt'),
        (r'BỘ THẦN CHÚ TIẾNG VIỆT 5 GIÂY', 'Mẹo ghi nhớ nhanh'),
        (r'BỘ THẦN CHÚ TIẾNG VIỆT', 'Mẹo ghi nhớ bằng tiếng Việt'),
        (r'CÂU THẦN CHÚ', 'Mẹo ghi nhớ'),
        (r'câu thần chú', 'mẹo ghi nhớ'),
        (r'THẦN CHÚ', 'Mẹo nhớ'),
        (r'thần chú', 'mẹo nhớ'),

        # Speed claims & Algorithm jargon for middle schoolers
        (r'SƠ ĐỒ THUẬT TOÁN NHẬN DIỆN NHANH DẠNG VIẾT LẠI CÂU', 'Sơ đồ tóm tắt các dạng viết lại câu'),
        (r'SƠ ĐỒ THUẬT TOÁN 3 BƯỚC PHÂN LOẠI PHÁT ÂM ĐUÔI -S / -ES', 'Sơ đồ 3 bước phân loại phát âm đuôi -s / -es'),
        (r'SƠ ĐỒ THUẬT TOÁN PHÂN LOẠI PHÁT ÂM "TH" TRONG 3 GIÂY', 'Sơ đồ phân loại phát âm "th"'),
        (r'SƠ ĐỒ THUẬT TOÁN 3 BƯỚC XỬ LÝ TRỌNG ÂM ĐỀ THI VÀO 10', 'Sơ đồ 3 bước xác định trọng âm'),
        (r'SƠ ĐỒ THUẬT TOÁN 3 BƯỚC TẠO CÂU HỎI ĐUÔI', 'Sơ đồ 3 bước tạo câu hỏi đuôi'),
        (r'SƠ ĐỒ THUẬT TOÁN 3 BƯỚC CHỌN MẠO TỪ TRONG 3 GIÂY', 'Sơ đồ 3 bước chọn mạo từ'),
        (r'SƠ ĐỒ THUẬT TOÁN CHỌN ĐẠI TỪ QUAN HỆ TRONG 3 GIÂY', 'Sơ đồ chọn đại từ quan hệ'),
        (r'SƠ ĐỒ THUẬT TOÁN PHÂN LOẠI DẠNG ĐỘNG TỪ TRONG 3 GIÂY', 'Sơ đồ phân loại dạng động từ V-ing và To-V'),
        (r'SƠ ĐỒ THUẬT TOÁN 3 BƯỚC', 'Sơ đồ 3 bước'),
        (r'SƠ ĐỒ THUẬT TOÁN', 'Sơ đồ tóm tắt'),
        (r'sơ đồ thuật toán', 'sơ đồ tóm tắt'),
        (r'thuật toán', 'quy trình'),
        (r'TRONG 3 GIÂY', ''),
        (r'TRONG 5 GIÂY', ''),
        (r'trong 3 giây', ''),
        (r'trong 5 giây', ''),

        # Traps & Ambush language
        (r'BẪY GÀI 100% CỦA ĐỀ THI TUYỂN SINH VÀO 10', 'Lỗi sai thường gặp khi làm bài thi'),
        (r'BẪY GÀI 100% THÍ SINH ĐỀU MẮC', 'Lỗi sai phổ biến cần lưu ý'),
        (r'BẪY GÀI 100%', 'Lỗi sai thường gặp'),
        (r'BẪY NGƯỜI VIỆT HAY SAI \(VIETLISH TRAPS\)', 'Lỗi sai thường gặp và cách tránh'),
        (r'BẪY NGƯỜI VIỆT HAY SAI \(VIETLISH TRAP\)', 'Lỗi sai thường gặp và cách tránh'),
        (r'BẪY NGƯỜI VIỆT HAY SAI', 'Lỗi sai thường gặp'),
        (r'VIETLISH TRAPS', 'Lỗi sai thường gặp'),
        (r'VIETLISH TRAP', 'Lỗi sai thường gặp'),
        (r'BẪY TÂM LÝ KINH ĐIỂN', 'Lỗi sai do nhầm lẫn'),
        (r'BẪY NGOẠI LỆ KINH ĐIỂN', 'Ngoại lệ thường gặp'),
        (r'CẶP ĐỘNG TỪ ĐỔI NGHĨA KINH ĐIỂN', 'Các cặp động từ đổi nghĩa cần lưu ý'),
        (r'BẪY PHÒNG THI DỄ MẤT ĐIỂM', 'Lỗi sai phòng thi cần tránh'),
        (r'HAY GÀI BẪY NHẤT', 'thường gây nhầm lẫn nhất'),
        (r'hay gài bẫy nhất', 'thường gây nhầm lẫn nhất'),
        (r'gài bẫy', 'gây nhầm lẫn'),
        (r'CHẮC CHẮN GÀI TRONG ĐỀ THI', 'thường gặp trong đề thi'),
        (r'CHẮC CHẮN RA THI', 'thường xuất hiện trong đề thi'),
        (r'bẫy', 'lỗi sai'),
        (r'Bẫy', 'Lỗi sai'),
        (r'BẪY', 'LƯU Ý'),

        # Thực chiến & Military jargon in education
        (r'THỰC CHIẾN PHÒNG THI', 'Luyện tập làm bài'),
        (r'thực chiến phòng thi', 'luyện tập làm bài'),
        (r'Module Luyện Đề Thi Thực Chiến', 'phần Luyện Đề Thi'),
        (r'Bảng Điểm Thực Chiến Phòng Thi', 'Bảng Điểm Làm Bài'),
        (r'KẾT QUẢ PHÒNG THI THỬ', 'KẾT QUẢ BÀI THI'),
        (r'THỰC CHIẾN', 'LUYỆN TẬP'),
        (r'Thực chiến', 'Luyện tập'),
        (r'thực chiến', 'luyện tập'),
        (r'Link Thực Chiến', 'Làm bài thi'),

        # Academic pretension & overly difficult linguistics terms for 9th graders
        (r'giữ nguyên 100% nghĩa gốc \(Semantic Equivalence\) nhưng thay đổi cấu trúc ngữ pháp \(Syntactic Structure\)', 
         'giữ nguyên nghĩa gốc của câu nhưng thay đổi cấu trúc ngữ pháp'),
        (r'\(Semantic Equivalence\)', ''),
        (r'\(Syntactic Structure\)', ''),
        (r'Chìa khóa ăn điểm tuyệt đối', 'Điểm cần lưu ý'),
        (r'ăn trọn 4\.0 điểm', 'đạt điểm tối đa phần'),
        (r'Ăn trọn điểm', 'Đạt điểm tối đa'),
        (r'ăn trọn điểm', 'đạt điểm tối đa'),
        (r'cốt tử', 'quan trọng'),
        (r'Bảo chứng', 'Hỗ trợ'),
        (r'bảo chứng', 'hỗ trợ'),
        (r'Bí quyết', 'Phương pháp'),
        (r'bí quyết', 'phương pháp'),
        (r'bách chiến', 'luyện thi'),
        (r'thần tốc', 'hiệu quả'),
        (r'GIẢI MÃ BIỂN BÁO', 'BIỂN BÁO'),
        (r'CÔNG CỘNG KINH ĐIỂN', 'CÔNG CỘNG THƯỜNG GẶP'),
        (r'CHỌN ĐÁP ÁN TỨC THỜI', 'CHỌN ĐÁP ÁN ĐÚNG'),
        (r'ĐIỂM 10/10', 'ĐẠT ĐIỂM CAO'),
        (r'TỦ ÔN THI VÀO 10', 'thường gặp ôn thi vào 10'),
        (r'TỦ ÔN VÀO 10', 'thường gặp ôn vào 10'),
        (r'tủ ôn thi', 'trọng tâm ôn thi')
    ]

    new_content = content
    for pattern, repl in replacements:
        new_content = re.sub(pattern, repl, new_content)

    return new_content

def update_all_markdown():
    files = glob.glob('EnglishDocs/docs/**/*.md', recursive=True)
    count = 0
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            orig = fp.read()
        cleaned = clean_file_content(orig)
        if cleaned != orig:
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(cleaned)
            count += 1
            print(f"Cleaned AI slops in: {f}")
    print(f"Total markdown files updated: {count}")

def update_config_mts():
    path = 'EnglishDocs/docs/.vitepress/config.mts'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace('"Cẩm Nang Phương Pháp"', '"Tài Liệu Phương Pháp"')
    c = c.replace('title: "Cẩm Nang Ôn Thi Vào 10"', 'title: "Tài Liệu Ôn Tập Vào Lớp 10"')
    c = c.replace('siteTitle: "Cẩm Nang Ôn Thi Vào 10"', 'siteTitle: "Tài Liệu Ôn Tập"')
    c = c.replace('Cổng ôn luyện tuyển sinh vào lớp 10 toàn diện', 'Tài liệu ôn thi vào lớp 10 môn Toán, Ngữ văn và Tiếng Anh')
    c = c.replace("label: 'Mục lục trên trang'", "label: 'Mục lục bài viết'")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated config.mts successfully!")

def update_vue_components():
    components = [
        'EnglishDocs/docs/.vitepress/theme/components/ExamHeader.vue',
        'EnglishDocs/docs/.vitepress/theme/components/ExamScoreboard.vue',
        'EnglishDocs/docs/.vitepress/theme/components/LessonCatalog.vue',
        'EnglishDocs/docs/.vitepress/theme/components/QuizItem.vue',
        'EnglishDocs/docs/.vitepress/theme/composables/useExamStore.ts'
    ]
    for comp in components:
        if os.path.exists(comp):
            with open(comp, 'r', encoding='utf-8') as f:
                c = f.read()
            cleaned = clean_file_content(c)
            # Component specific cleanups
            cleaned = cleaned.replace("'Cẩm Nang Phương Pháp'", "'Phương Pháp Học Tập'")
            cleaned = cleaned.replace("title: 'Bảng Điểm Thực Chiến Phòng Thi'", "title: 'Bảng Điểm Làm Bài'")
            cleaned = cleaned.replace("ĐỒNG HỒ BẤM GIỜ THỰC CHIẾN", "ĐỒNG HỒ ĐẾM GIỜ LÀM BÀI")
            cleaned = cleaned.replace("KẾT QUẢ PHÒNG THI THỬ", "KẾT QUẢ BÀI THI")
            cleaned = cleaned.replace("câu bẫy từ vựng", "câu phân hóa từ vựng")
            if cleaned != c:
                with open(comp, 'w', encoding='utf-8') as f:
                    f.write(cleaned)
                print(f"Cleaned component: {comp}")

def update_custom_css_responsive():
    css_path = 'EnglishDocs/docs/.vitepress/theme/custom.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    # 1. Fix Table display to block and overflow-x: auto so it never breaks layout on iPhone
    css = re.sub(
        r'/\* Study4 Style Tables - Clean, Clear, High-Contrast \*/\s*\.vp-doc table\s*\{[^}]*\}',
        '''/* Responsive Tables - Clean, Clear, High-Contrast */
.vp-doc table {
  width: 100% !important;
  display: block !important;
  overflow-x: auto !important;
  -webkit-overflow-scrolling: touch !important;
  border-collapse: separate !important;
  border-spacing: 0 !important;
  border-radius: 12px;
  border: 1px solid var(--vp-c-divider) !important;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03);
  margin: 1.5rem 0 !important;
}''',
        css
    )

    # 2. Add extra responsive rules at the end of custom.css
    mobile_fixes = '''
/* Additional Mobile & iPhone Responsive Fixes */
@media (max-width: 640px) {
  .vp-doc table {
    min-width: 100% !important;
    font-size: 0.86rem !important;
  }
  
  .vp-doc th,
  .vp-doc td {
    padding: 0.65rem 0.75rem !important;
  }

  .options-grid {
    grid-template-columns: 1fr !important;
    gap: 0.55rem !important;
  }

  .study4-quiz-card {
    padding: 1rem 0.95rem !important;
    margin: 1.15rem 0 !important;
    border-radius: 10px !important;
  }

  .transform-input-row {
    flex-direction: column !important;
    gap: 0.5rem !important;
  }

  .show-answer-btn {
    width: 100% !important;
    text-align: center !important;
    padding: 0.75rem 1rem !important;
  }

  .exam-meta-grid {
    grid-template-columns: 1fr !important;
    gap: 0.75rem !important;
  }

  .scoreboard-bar {
    flex-direction: column !important;
    align-items: stretch !important;
    gap: 0.75rem !important;
    padding: 0.85rem !important;
  }

  .bar-right .submit-exam-btn {
    width: 100% !important;
    justify-content: center !important;
  }

  .lessons-grid {
    grid-template-columns: 1fr !important;
  }
}
'''
    if '/* Additional Mobile & iPhone Responsive Fixes */' not in css:
        css += '\n' + mobile_fixes

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated custom.css responsive rules successfully!")

if __name__ == '__main__':
    update_config_mts()
    update_vue_components()
    update_all_markdown()
    update_custom_css_responsive()

