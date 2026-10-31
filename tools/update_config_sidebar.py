# -*- coding: utf-8 -*-
config_path = r'f:\OnThiC3\EnglishDocs\docs\.vitepress\config.mts'
with open(config_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """  const overview = [
    { text: '📐 Tổng quan & Đề thi PDF', link: '/math/' },
    { text: '📖 Sổ Tay Toàn Bộ Công Thức Toán 9', link: '/math/so_tay_cong_thuc_toan_9' },
    { text: '🌟 12 Chuyên Đề Trọng Tâm Thi Vào 10', link: '/math/12_chuyen_de_on_thi_vao_10_toan' },
    { text: '📝 Đề Kiểm Tra Giữa Học Kỳ 1 Toán 9', link: '/math/de_thi_giua_hoc_ky_1_toan_9' }
  ]"""

replacement = """  const overview = [
    { text: '📐 Tổng quan & Đề thi PDF', link: '/math/' },
    { text: '📖 Sổ Tay Toàn Bộ Công Thức Toán 9', link: '/math/so_tay_cong_thuc_toan_9' },
    { text: '🌟 12 Chuyên Đề Trọng Tâm Thi Vào 10', link: '/math/12_chuyen_de_on_thi_vao_10_toan' }
  ]

  const onlineExams = {
    text: '📝 Bộ Đề Thi Trực Tuyến Có Lời Giải',
    collapsed: false,
    items: [
      { text: '📝 Đề Giữa Học Kỳ 1 Toán 9', link: '/math/de_thi_giua_hoc_ky_1_toan_9' },
      { text: '📝 Đề Cuối Học Kỳ 1 Toán 9', link: '/math/de_thi_hoc_ky_1_toan_9' },
      { text: '📝 Đề Giữa Học Kỳ 2 Toán 9', link: '/math/de_thi_giua_hoc_ky_2_toan_9' },
      { text: '📝 Đề Cuối Học Kỳ 2 Toán 9', link: '/math/de_thi_hoc_ky_2_toan_9' },
      { text: '🏛️ Đề Tuyển Sinh Vào 10 - Quảng Ngãi', link: '/math/de_thi_tuyen_sinh_vao_10_toan_quang_ngai' },
      { text: '🏛️ Đề Tuyển Sinh Vào 10 - Hà Nội', link: '/math/de_thi_tuyen_sinh_vao_10_toan_ha_noi' },
      { text: '🏛️ Đề Tuyển Sinh Vào 10 - TP.HCM', link: '/math/de_thi_tuyen_sinh_vao_10_toan_tphcm' },
      { text: '🏛️ Đề Tuyển Sinh Vào 10 - Đà Nẵng', link: '/math/de_thi_tuyen_sinh_vao_10_toan_da_nang' }
    ]
  }"""

target_ret = "return [...overview, g1, g2, g3, g4, g5]"
replacement_ret = "return [...overview, onlineExams, g1, g2, g3, g4, g5]"

if target in text:
    text = text.replace(target, replacement)
    text = text.replace(target_ret, replacement_ret)
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated config.mts successfully!")
else:
    print("Target not found, checking with normalize...")
    text_norm = text.replace('\r\n', '\n')
    target_norm = target.replace('\r\n', '\n')
    if target_norm in text_norm:
        text_norm = text_norm.replace(target_norm, replacement.replace('\r\n', '\n'))
        text_norm = text_norm.replace(target_ret, replacement_ret)
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(text_norm)
        print("Updated config.mts with normalized newlines!")
    else:
        print("Target still not found!")

