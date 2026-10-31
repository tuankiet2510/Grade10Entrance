# -*- coding: utf-8 -*-
path = r'f:\OnThiC3\EnglishDocs\docs\math\index.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '<div class="math-hero-stats">'
idx = content.find(target)
target_end = '## 🎯 Bộ Đề Thi Tuyển Sinh & Chuyên Đề Nâng Cao (PDF)'
idx_end = content.find(target_end)

if idx != -1 and idx_end != -1:
    replacement = '''<div class="math-hero-stats">
  <div class="stat-box">
    <div class="stat-number">48</div>
    <div class="stat-label">Chuyên đề trọng tâm</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">257</div>
    <div class="stat-label">Bài học lý thuyết</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">8</div>
    <div class="stat-label">Đề thi Online có giải</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">17</div>
    <div class="stat-label">Đề thi &amp; Chuyên đề PDF</div>
  </div>
</div>

<div class="custom-block tip">
  <p class="custom-block-title">💡 Tính năng in ấn &amp; học tập di động</p>
  <p>Toàn bộ 48 chuyên đề và 8 bộ đề thi trực tuyến môn Toán được tối ưu hóa hiển thị công thức MathJax chuẩn mực, sắc nét trên mọi thiết bị (iPhone, iPad, Android, Laptop). Trong mỗi đề thi đều có lời giải chi tiết từng bước và bảng phân tích phương pháp giải.</p>
</div>

---

## 📖 Cẩm Nang Công Thức & Bản Đồ Chuyên Đề

<div class="pdf-exam-grid">
  <div class="pdf-card" style="border: 2px solid var(--vp-c-brand-1);">
    <div class="pdf-card-badge" style="background: var(--vp-c-brand-1); color: #fff;">Sổ tay bỏ túi • Tra cứu nhanh</div>
    <h3 class="pdf-card-title">📖 Sổ Tay Toàn Bộ Công Thức Toán 9 (Tập 1 &amp; Tập 2)</h3>
    <p class="pdf-card-desc">Hệ thống hóa 100% công thức: Căn thức, Hệ phương trình, Hàm số, Viète, Thống kê, Xác suất, Lượng giác, Đường tròn, Tứ giác nội tiếp, Hình trụ - nón - cầu.</p>
    <div class="pdf-card-actions">
      <a href="./so_tay_cong_thuc_toan_9" class="pdf-btn view-btn" style="background: var(--vp-c-brand-1); color: #fff;">
        Xem Sổ Tay Công Thức ↗
      </a>
    </div>
  </div>

  <div class="pdf-card">
    <div class="pdf-card-badge">Tài liệu tuyển sinh 2026 - 2027</div>
    <h3 class="pdf-card-title">12 Chuyên Đề Trọng Tâm Ôn Thi Vào Lớp 10 Môn Toán</h3>
    <p class="pdf-card-desc">Bản đồ phân loại cấu trúc đề thi tuyển sinh 10 THPT công lập (Rút gọn biểu thức, Hệ PT, Viète, Parabol, BĐT, Tứ giác nội tiếp...).</p>
    <div class="pdf-card-actions">
      <a href="./12_chuyen_de_on_thi_vao_10_toan" class="pdf-btn view-btn">
        Xem Bản Đồ 12 Chuyên Đề ↗
      </a>
    </div>
  </div>
</div>

---

## 📝 Bộ Đề Thi Trực Tuyến Có Lời Giải Chi Tiết (Làm Trực Tiếp Online)

Tất cả đề thi đều được biên soạn bám sát ma trận đề thi tuyển sinh lớp 10 mới nhất, trình bày lời giải chi tiết từng bước, tích hợp công thức MathJax sắc nét.

<div class="pdf-exam-grid">
  <div class="pdf-card">
    <div class="pdf-card-badge">Khảo sát năng lực • 90 Phút</div>
    <h3 class="pdf-card-title">📝 Đề Kiểm Tra Giữa Học Kỳ 1 Toán 9</h3>
    <p class="pdf-card-desc">12 câu trắc nghiệm + 5 bài tự luận: Rút gọn căn thức, hệ phương trình bậc nhất hai ẩn, tỉ số lượng giác góc nhọn và BĐT điểm 10.</p>
    <div class="pdf-card-actions">
      <a href="./de_thi_giua_hoc_ky_1_toan_9" class="pdf-btn view-btn">
        Làm Đề &amp; Xem Lời Giải ↗
      </a>
    </div>
  </div>

  <div class="pdf-card">
    <div class="pdf-card-badge">Học kỳ 1 • 90 Phút</div>
    <h3 class="pdf-card-title">📝 Đề Kiểm Tra Cuối Học Kỳ 1 Toán 9</h3>
    <p class="pdf-card-desc">12 câu trắc nghiệm + 5 bài tự luận: Biến đổi căn thức, đồ thị hàm số bậc nhất, hệ phương trình, bài toán đo góc thực tế và tiếp tuyến đường tròn.</p>
    <div class="pdf-card-actions">
      <a href="./de_thi_hoc_ky_1_toan_9" class="pdf-btn view-btn">
        Làm Đề &amp; Xem Lời Giải ↗
      </a>
    </div>
  </div>

  <div class="pdf-card">
    <div class="pdf-card-badge">Học kỳ 2 • 90 Phút</div>
    <h3 class="pdf-card-title">📝 Đề Kiểm Tra Giữa Học Kỳ 2 Toán 9</h3>
    <p class="pdf-card-desc">12 câu trắc nghiệm + 5 bài tự luận: Hệ hai phương trình, Parabol y = ax², phương trình bậc hai, hệ thức Viète, tứ giác nội tiếp và cực trị.</p>
    <div class="pdf-card-actions">
      <a href="./de_thi_giua_hoc_ky_2_toan_9" class="pdf-btn view-btn">
        Làm Đề &amp; Xem Lời Giải ↗
      </a>
    </div>
  </div>

  <div class="pdf-card">
    <div class="pdf-card-badge">Tổng ôn cả năm • 90 Phút</div>
    <h3 class="pdf-card-title">📝 Đề Kiểm Tra Cuối Học Kỳ 2 Toán 9</h3>
    <p class="pdf-card-desc">12 câu trắc nghiệm + 5 bài tự luận: Toàn bộ phạm vi kiến thức Toán 9, Thống kê, Xác suất, Tứ giác nội tiếp, Hình trụ - nón - cầu và BĐT Cauchy.</p>
    <div class="pdf-card-actions">
      <a href="./de_thi_hoc_ky_2_toan_9" class="pdf-btn view-btn">
        Làm Đề &amp; Xem Lời Giải ↗
      </a>
    </div>
  </div>

  <div class="pdf-card" style="border: 2px solid var(--vp-c-brand-1);">
    <div class="pdf-card-badge" style="background: var(--vp-c-brand-1); color: #fff;">Đề Tuyển Sinh 10 • 120 Phút</div>
    <h3 class="pdf-card-title">🏛️ Đề Tuyển Sinh Vào 10 - Tỉnh Quảng Ngãi</h3>
    <p class="pdf-card-desc">Chuẩn cấu trúc 5 bài tự luận Sở GD&amp;ĐT Quảng Ngãi: Rút gọn căn thức, Parabol &amp; Viète, bài toán thực tế chuyển động xe tải - xe khách, đường tròn 3 ý, BĐT điểm 10.</p>
    <div class="pdf-card-actions">
      <a href="./de_thi_tuyen_sinh_vao_10_toan_quang_ngai" class="pdf-btn view-btn" style="background: var(--vp-c-brand-1); color: #fff;">
        Làm Đề &amp; Xem Lời Giải ↗
      </a>
    </div>
  </div>

  <div class="pdf-card" style="border: 2px solid var(--vp-c-brand-1);">
    <div class="pdf-card-badge" style="background: var(--vp-c-brand-1); color: #fff;">Đề Tuyển Sinh 10 • 120 Phút</div>
    <h3 class="pdf-card-title">🏛️ Đề Tuyển Sinh Vào 10 - TP. Hà Nội</h3>
    <p class="pdf-card-desc">Chuẩn cấu trúc Sở GD&amp;ĐT Hà Nội: 5 bài tự luận gồm biểu thức chứa căn, bài toán năng suất đơn hàng, thể tích thùng nước hình trụ, Viète, hình học đường tròn và Cauchy ngược dấu.</p>
    <div class="pdf-card-actions">
      <a href="./de_thi_tuyen_sinh_vao_10_toan_ha_noi" class="pdf-btn view-btn" style="background: var(--vp-c-brand-1); color: #fff;">
        Làm Đề &amp; Xem Lời Giải ↗
      </a>
    </div>
  </div>

  <div class="pdf-card" style="border: 2px solid var(--vp-c-brand-1);">
    <div class="pdf-card-badge" style="background: var(--vp-c-brand-1); color: #fff;">Đề Tuyển Sinh 10 • 120 Phút</div>
    <h3 class="pdf-card-title">🏛️ Đề Tuyển Sinh Vào 10 - TP. Hồ Chí Minh</h3>
    <p class="pdf-card-desc">Chuẩn mô hình toán thực tế TP.HCM: 8 bài toán ứng dụng (Parabol, Viète, lãi suất ngân hàng, hàm nhiệt độ F-C, nồng độ muối, nón lá hình học, chiết khấu mua sắm, hình học đường tròn).</p>
    <div class="pdf-card-actions">
      <a href="./de_thi_tuyen_sinh_vao_10_toan_tphcm" class="pdf-btn view-btn" style="background: var(--vp-c-brand-1); color: #fff;">
        Làm Đề &amp; Xem Lời Giải ↗
      </a>
    </div>
  </div>

  <div class="pdf-card" style="border: 2px solid var(--vp-c-brand-1);">
    <div class="pdf-card-badge" style="background: var(--vp-c-brand-1); color: #fff;">Đề Tuyển Sinh 10 • 120 Phút</div>
    <h3 class="pdf-card-title">🏛️ Đề Tuyển Sinh Vào 10 - TP. Đà Nẵng</h3>
    <p class="pdf-card-desc">Chuẩn cấu trúc Sở GD&amp;ĐT Đà Nẵng: 5 bài tự luận gồm căn thức đại số, hệ phương trình &amp; Vi-ét, tiếp xúc Parabol, toán thực tế ca nô xuôi - ngược dòng và hình học phẳng.</p>
    <div class="pdf-card-actions">
      <a href="./de_thi_tuyen_sinh_vao_10_toan_da_nang" class="pdf-btn view-btn" style="background: var(--vp-c-brand-1); color: #fff;">
        Làm Đề &amp; Xem Lời Giải ↗
      </a>
    </div>
  </div>
</div>

---

'''
    new_content = content[:idx] + replacement + content[idx_end:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Updated EnglishDocs/docs/math/index.md successfully')
else:
    print('Error finding targets:', idx, idx_end)

