import re

config_path = r"f:\OnThiC3\EnglishDocs\docs\.vitepress\config.mts"
with open(config_path, "r", encoding="utf-8") as f:
    config_content = f.read()

# 1. Update buildMathSidebar
old_math_overview = """  const overview = [
    { text: '📐 Tổng quan & Đề thi PDF', link: '/math/' },
    { text: '🌟 12 Chuyên Đề Trọng Tâm Thi Vào 10', link: '/math/12_chuyen_de_on_thi_vao_10_toan' },
    { text: '📝 Đề Kiểm Tra Giữa Học Kỳ 1 Toán 9', link: '/math/de_thi_giua_hoc_ky_1_toan_9' }
  ]"""

new_math_overview = """  const overview = [
    { text: '📐 Tổng quan & Đề thi PDF', link: '/math/' },
    { text: '📖 Sổ Tay Toàn Bộ Công Thức Toán 9', link: '/math/so_tay_cong_thuc_toan_9' },
    { text: '🌟 12 Chuyên Đề Trọng Tâm Thi Vào 10', link: '/math/12_chuyen_de_on_thi_vao_10_toan' },
    { text: '📝 Đề Kiểm Tra Giữa Học Kỳ 1 Toán 9', link: '/math/de_thi_giua_hoc_ky_1_toan_9' }
  ]"""

config_content = config_content.replace(
    ".filter(f => f.endsWith('.md') && f !== 'index.md' && f !== 'README.md' && !f.includes('chuyen_de') && !f.includes('de_thi'))",
    ".filter(f => f.endsWith('.md') && f !== 'index.md' && f !== 'README.md' && !f.includes('chuyen_de') && !f.includes('de_thi') && !f.includes('so_tay'))"
)
config_content = config_content.replace(old_math_overview, new_math_overview)

# 2. Update buildLiteratureSidebar
old_lit_func = """// Sidebar cho Ngữ Văn 9
function buildLiteratureSidebar(dirPath: string): any[] {
  return [
    { text: '📖 Trung Tâm Ôn Luyện Ngữ Văn 9', link: '/literature/' },"""

new_lit_func = """// Sidebar cho Ngữ Văn 9
function buildLiteratureSidebar(dirPath: string): any[] {
  return [
    { text: '📖 Trung Tâm Ôn Luyện Ngữ Văn 9', link: '/literature/' },
    { text: '📘 Sổ Tay Tổng Hợp Kiến Thức Ngữ Văn 9', link: '/literature/so_tay_kien_thuc_ngu_van_9' },"""

config_content = config_content.replace(old_lit_func, new_lit_func)

# 3. Add buildScienceSidebar function right after buildLiteratureSidebar
science_func = """
// Sidebar cho KHTN 9 (Vật lí, Hóa học, Sinh học)
function buildScienceSidebar(dirPath: string): any[] {
  return [
    { text: '🔬 Trung Tâm Ôn Luyện KHTN 9', link: '/science/' },
    {
      text: 'Sổ Tay Công Thức & Kiến Thức KHTN 9',
      collapsed: false,
      items: [
        { text: '⚡ Sổ Tay Công Thức & Lý Thuyết Vật Lí 9', link: '/science/01_vat_li_9_cong_thuc_va_ly_thuyet' },
        { text: '🧪 Sổ Tay Lý Thuyết & Phương Trình Hóa Học 9', link: '/science/02_hoa_hoc_9_ly_thuyet_va_phuong_trinh' },
        { text: '🧬 Sổ Tay Di Truyền & Sinh Thái Học Sinh Học 9', link: '/science/03_sinh_hoc_9_di_truyen_va_sinh_thai' }
      ]
    }
  ]
}
"""

if "function buildScienceSidebar" not in config_content:
    config_content = config_content.replace("export default defineConfig({", science_func + "\nexport default defineConfig({")

# 4. Add nav and sidebar entries
old_nav = """      { text: 'Ngữ Văn 9 📖', link: '/literature/' },
      { text: 'Tiếng Anh 9 (Lý thuyết) 🇬🇧', link: '/catalog' },"""

new_nav = """      { text: 'Ngữ Văn 9 📖', link: '/literature/' },
      { text: 'Tiếng Anh 9 (Lý thuyết) 🇬🇧', link: '/catalog' },
      { text: 'KHTN 9 (Lý - Hóa - Sinh) 🔬', link: '/science/' },"""

config_content = config_content.replace(old_nav, new_nav)

old_sidebar = """      '/math/': buildMathSidebar(path.resolve(__dirname, '../math')),
      '/literature/': buildLiteratureSidebar(path.resolve(__dirname, '../literature')),
      '/lessons/': scanDirectoryRecursive(path.resolve(__dirname, '../lessons'), '/lessons'),"""

new_sidebar = """      '/math/': buildMathSidebar(path.resolve(__dirname, '../math')),
      '/literature/': buildLiteratureSidebar(path.resolve(__dirname, '../literature')),
      '/science/': buildScienceSidebar(path.resolve(__dirname, '../science')),
      '/lessons/': scanDirectoryRecursive(path.resolve(__dirname, '../lessons'), '/lessons'),"""

config_content = config_content.replace(old_sidebar, new_sidebar)

with open(config_path, "w", encoding="utf-8") as f:
    f.write(config_content)
print("Updated config.mts successfully!")

# 5. Update math/index.md to add card for so_tay_cong_thuc_toan_9
math_index_path = r"f:\OnThiC3\EnglishDocs\docs\math\index.md"
with open(math_index_path, "r", encoding="utf-8") as f:
    math_content = f.read()

math_card = """  <div class="pdf-card" style="border: 2px solid var(--vp-c-brand-1);">
    <div class="pdf-card-badge" style="background: var(--vp-c-brand-1); color: #fff;">Sổ tay bỏ túi • Tra cứu nhanh</div>
    <h3 class="pdf-card-title">📖 Sổ Tay Toàn Bộ Công Thức Toán 9 (Tập 1 &amp; Tập 2)</h3>
    <p class="pdf-card-desc">Hệ thống hóa 100% công thức: Căn thức, Hệ phương trình, Hàm số, Viète, Thống kê, Xác suất, Lượng giác, Đường tròn, Tứ giác nội tiếp, Hình trụ - nón - cầu.</p>
    <div class="pdf-card-actions">
      <a href="./so_tay_cong_thuc_toan_9" class="pdf-btn view-btn" style="background: var(--vp-c-brand-1); color: #fff;">
        Xem Sổ Tay Công Thức ↗
      </a>
    </div>
  </div>
"""

if "so_tay_cong_thuc_toan_9" not in math_content:
    math_content = math_content.replace('<div class="pdf-exam-grid">\n  <div class="pdf-card">', '<div class="pdf-exam-grid">\n' + math_card + '\n  <div class="pdf-card">')
    with open(math_index_path, "w", encoding="utf-8") as f:
        f.write(math_content)
    print("Updated math/index.md successfully!")

# 6. Update literature/index.md to add card for so_tay_kien_thuc_ngu_van_9
lit_index_path = r"f:\OnThiC3\EnglishDocs\docs\literature\index.md"
with open(lit_index_path, "r", encoding="utf-8") as f:
    lit_content = f.read()

lit_card = """  <div class="pdf-card" style="border: 2px solid var(--vp-c-brand-1); grid-column: 1 / -1;">
    <div class="pdf-card-badge" style="background: var(--vp-c-brand-1); color: #fff;">Sổ tay cốt lõi • Đổi mới GDPT 2018</div>
    <h3 class="pdf-card-title">📘 Sổ Tay Tổng Hợp Kiến Thức Ngữ Văn 9 (Bộ Sách Kết Nối Tri Thức)</h3>
    <p class="pdf-card-desc">Hệ thống 10 bài học SGK Kết nối tri thức, công thức xử lý Đọc hiểu ngoài SGK, bảng 10 biện pháp tu từ, tổng ôn toàn diện Tiếng Việt 9 và cẩm nang viết đoạn văn NLXH 200 chữ.</p>
    <div class="pdf-card-actions">
      <a href="./so_tay_kien_thuc_ngu_van_9" class="pdf-btn view-btn" style="background: var(--vp-c-brand-1); color: #fff;">
        Mở Sổ Tay Ngữ Văn 9 ↗
      </a>
    </div>
  </div>
"""

if "so_tay_kien_thuc_ngu_van_9" not in lit_content:
    lit_content = lit_content.replace('<div class="pdf-exam-grid">\n  <div class="pdf-card">', '<div class="pdf-exam-grid">\n' + lit_card + '\n  <div class="pdf-card">')
    with open(lit_index_path, "w", encoding="utf-8") as f:
        f.write(lit_content)
    print("Updated literature/index.md successfully!")
