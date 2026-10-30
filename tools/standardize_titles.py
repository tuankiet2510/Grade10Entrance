import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

clean_titles = {
    'chuyen_de_1_phat_am_ae_e.md': 'Chuyên Đề 1: Phân Biệt Phát Âm Nguyên Âm /æ/ Và /e/',
    'chuyen_de_1_phat_am_ed_mastery.md': 'Chuyên Đề 1: Quy Tắc Phát Âm Đuôi -ed Và Ngoại Lệ Tính Từ',
    'chuyen_de_1_phat_am_s_es_mastery.md': 'Chuyên Đề 1: Quy Tắc Phát Âm Đuôi -s Và -es',
    'chuyen_de_1_phat_am_th.md': 'Chuyên Đề 1: Quy Tắc Phát Âm "th" (/θ/ và /ð/)',
    'chuyen_de_1_trong_am_mastery.md': 'Chuyên Đề 1: Quy Tắc Trọng Âm Từ Và Các Ngoại Lệ',
    'chuyen_de_2_10_cau_truc_bien_doi_cau.md': 'Chuyên Đề 2: 10 Cấu Trúc Viết Lại Câu Trọng Tâm Ôn Thi Vào 10',
    'chuyen_de_2_12_thi_mastery.md': 'Chuyên Đề 2: Hệ Thống 12 Thì Và Cách Phối Hợp Thì Trọng Tâm',
    'chuyen_de_2_cau_hoi_duoi_mastery.md': 'Chuyên Đề 2: Câu Hỏi Đuôi Và Các Trường Hợp Đặc Biệt',
    'chuyen_de_2_dong_tu_khuyet_thieu_mastery.md': 'Chuyên Đề 2: Động Từ Khuyết Thiếu (Modal Verbs)',
    'chuyen_de_2_gioi_tu_prepositions_mastery.md': 'Chuyên Đề 2: Giới Từ Thời Gian, Nơi Chốn Và Cụm Giới Từ',
    'chuyen_de_2_mao_tu_articles_mastery.md': 'Chuyên Đề 2: Mạo Từ (a, an, the) Và Trường Hợp Không Dùng Mạo Từ',
    'chuyen_de_2_menh_de_quan_he.md': 'Chuyên Đề 2: Mệnh Đề Quan Hệ Và Rút Gọn Mệnh Đề Quan Hệ',
    'chuyen_de_2_ving_to_v_mastery.md': 'Chuyên Đề 2: Danh Động Từ (V-ing) Và Động Từ Nguyên Mẫu (to-V)',
    'chuyen_de_2_word_form_va_su_hoa_hop.md': 'Chuyên Đề 2: Cấu Tạo Từ (Word Form) Và Sự Hòa Hợp Chủ - Vị',
    'chuyen_de_3_dong_nghia_trai_nghia_mastery.md': 'Chuyên Đề 3: Từ Đồng Nghĩa Và Từ Trái Nghĩa',
    'chuyen_de_3_phrasal_verbs_mastery.md': 'Chuyên Đề 3: 50 Cụm Động Từ (Phrasal Verbs) Thường Gặp',
    'chuyen_de_4_giai_ma_bien_bao_va_giao_tiep.md': 'Chuyên Đề 4: Biển Báo Công Cộng Và Tình Huống Giao Tiếp',
    'chuyen_de_5_huong_dan_viet_doan_van_nghi_luan.md': 'Chuyên Đề 5: Hướng Dẫn Viết Đoạn Văn Nghị Luận 100 - 120 Từ',
    'chuyen_de_6_trong_tam_12_units_global_success_9.md': 'Chuyên Đề 6: Tổng Ôn Trọng Tâm 12 Units SGK Tiếng Anh 9'
}

for fname, title in clean_titles.items():
    path = os.path.join('EnglishDocs', 'docs', 'lessons', fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Replace first # Heading
    c = re.sub(r'^#\s+.*$', f'# {title}', c, count=1, flags=re.MULTILINE)
    
    # Replace frontmatter title if present
    c = re.sub(r'^(title:\s*["\']).*?(["\'])$', f'\\g<1>{title}\\g<2>', c, count=1, flags=re.MULTILINE)
    
    with open(path, 'w', encoding='utf-8') as fp:
        fp.write(c)
    print(f"Standardized: {fname} -> {title}")
