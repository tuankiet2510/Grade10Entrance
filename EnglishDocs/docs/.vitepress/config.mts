import { defineConfig } from 'vitepress'
import fs from 'node:fs'
import path from 'node:path'

const MODULE_NAMES: Record<string, string> = {
  "chuyen_de_1": "Phần 1: Ngữ Âm & Trọng Âm",
  "chuyen_de_2": "Phần 2: Ngữ Pháp & Cấu Trúc Trọng Tâm",
  "chuyen_de_3": "Phần 3: Từ Vựng Chọn Lọc",
  "guide": "Tài Liệu Phương Pháp",
  "exams": "Bộ Đề Tuyển Sinh Vào 10",
  "math": "Chuyên Đề Toán 9 Vào 10",
  "literature": "Chuyên Đề Ngữ Văn 9 Vào 10"
}

function formatFolderName(name: string): string {
  if (MODULE_NAMES[name]) return MODULE_NAMES[name]
  const clean = name.replace(/^\d+[-_]/, '').replace(/[-_]/g, ' ')
  const prefix = name.match(/^(\d+)[-_]/)?.[1]
  const capitalized = clean.charAt(0).toUpperCase() + clean.slice(1)
  return prefix ? `${parseInt(prefix)}. ${capitalized}` : capitalized
}

function extractMarkdownTitle(filePath: string, fallbackName: string): string {
  try {
    const content = fs.readFileSync(filePath, 'utf-8')
    const fmMatch = content.match(/^---\r?\n[\s\S]*?title:\s*(.*?)\r?\n[\s\S]*?---/)
    const h1Match = content.match(/^#\s+(.+)$/m)
    const raw = fmMatch ? fmMatch[1] : (h1Match ? h1Match[1] : fallbackName)
    return raw.trim().replace(/^['"](.*)['"]$/, '$1').replace(/[\x60*]/g, '').trim()
  } catch {
    return fallbackName
  }
}

// Hàm đệ quy quét thư mục đa tầng để dựng Sidebar
function scanDirectoryRecursive(dirPath: string, urlPrefix: string): any[] {
  if (!fs.existsSync(dirPath)) return []
  const entries = fs.readdirSync(dirPath, { withFileTypes: true })
    .filter(e => !e.name.startsWith('.') && !e.name.includes('c674a7bc') && !e.name.includes('ExportBlock') && e.name !== 'superpowers')
    .sort((a, b) => a.name.localeCompare(b.name, undefined, { numeric: true }))

  const items: any[] = []
  const flatFiles: any[] = []

  for (const entry of entries) {
    const fullPath = path.join(dirPath, entry.name)
    if (entry.isDirectory()) {
      const children = scanDirectoryRecursive(fullPath, `${urlPrefix}/${entry.name}`)
      if (children.length > 0) {
        items.push({
          text: formatFolderName(entry.name),
          collapsed: false,
          items: children
        })
      }
    } else if (entry.isFile() && entry.name.endsWith('.md') && entry.name.toLowerCase() !== 'readme.md') {
      const slug = entry.name.replace(/\.md$/, '')
      flatFiles.push({
        text: extractMarkdownTitle(fullPath, slug),
        link: `${urlPrefix}/${slug}`,
        rawName: entry.name
      })
    }
  }

  // Tự động gom nhóm chuyên đề theo tiền tố nếu tài liệu ở cùng cấp
  if (flatFiles.length > 0) {
    const groups: Record<string, any[]> = {}
    for (const f of flatFiles) {
      let gKey = 'Tài liệu bổ trợ'
      if (f.rawName.startsWith('chuyen_de_1')) gKey = 'Phần 1: Ngữ Âm & Trọng Âm'
      else if (f.rawName.startsWith('chuyen_de_2')) gKey = 'Phần 2: Ngữ Pháp & Cấu Trúc'
      else if (f.rawName.startsWith('chuyen_de_3')) gKey = 'Phần 3: Từ Vựng Chọn Lọc'
      else if (f.rawName.startsWith('chuyen_de_4')) gKey = 'Phần 4: Biển Báo & Giao Tiếp Thực Tế'
      else if (f.rawName.startsWith('chuyen_de_5')) gKey = 'Phần 5: Kỹ Năng Viết Luận & Đoạn Văn'
      else if (f.rawName.startsWith('chuyen_de_6')) gKey = 'Phần 6: Trọng Tâm 12 Units SGK Lớp 9'
      else if (f.rawName.startsWith('guide')) gKey = 'Cẩm Nang Phương Pháp'
      else if (f.rawName.startsWith('de_cuong')) gKey = '📘 Đề Cương Ôn Tập Giữa Kỳ'
      else if (f.rawName.includes('quang_ngai') || f.rawName.includes('da_nang')) gKey = '🏛️ Đề Thi Chính Thức Sở GD&ĐT'
      else if (f.rawName.includes('hoc_ky') || f.rawName.includes('giua_hoc_ky')) gKey = '📖 Đề Thi Giữa Kỳ & Học Kỳ Lớp 9'
      else if (f.rawName.includes('36_cau')) gKey = '📚 Bộ Đề Form 36 Câu (Quảng Ngãi)'
      else if (f.rawName.includes('45_cau')) gKey = '📝 Bộ Đề Form 45 Câu Tuyển Sinh'

      if (!groups[gKey]) groups[gKey] = []
      groups[gKey].push({ text: f.text, link: f.link })
    }

    if (Object.keys(groups).length > 1) {
      for (const [gTitle, gItems] of Object.entries(groups)) {
        items.push({
          text: gTitle,
          collapsed: false,
          items: gItems
        })
      }
    } else {
      items.push(...flatFiles.map(f => ({ text: f.text, link: f.link })))
    }
  }

  return items
}

// Sidebar riêng cho Toán 9 (48 chuyên đề + 12 CĐ + Đề giữa kì)
function buildMathSidebar(dirPath: string): any[] {
  if (!fs.existsSync(dirPath)) return []
  const files = fs.readdirSync(dirPath)
    .filter(f => f.endsWith('.md') && f !== 'index.md' && f !== 'README.md' && !f.includes('chuyen_de') && !f.includes('de_thi'))
    .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }))

  const overview = [
    { text: '📐 Tổng quan & Đề thi PDF', link: '/math/' },
    { text: '🌟 12 Chuyên Đề Trọng Tâm Thi Vào 10', link: '/math/12_chuyen_de_on_thi_vao_10_toan' },
    { text: '📝 Đề Kiểm Tra Giữa Học Kỳ 1 Toán 9', link: '/math/de_thi_giua_hoc_ky_1_toan_9' }
  ]

  // Gom theo cụm chuyên đề để sidebar gọn gàng
  const g1 = { text: 'Chuyên đề 01 - 10: Đại số & Căn bậc hai', collapsed: false, items: [] as any[] }
  const g2 = { text: 'Chuyên đề 11 - 20: Căn bậc ba, Lượng giác & Đường tròn', collapsed: true, items: [] as any[] }
  const g3 = { text: 'Chuyên đề 21 - 30: Phương trình bậc hai, Viete & Thống kê', collapsed: true, items: [] as any[] }
  const g4 = { text: 'Chuyên đề 31 - 40: Xác suất, Góc & Hình khối không gian', collapsed: true, items: [] as any[] }
  const g5 = { text: 'Chuyên đề 41 - 48: Hình học không gian & Ứng dụng thực tế', collapsed: true, items: [] as any[] }

  for (const file of files) {
    const fullPath = path.join(dirPath, file)
    const slug = file.replace(/\.md$/, '')
    const title = extractMarkdownTitle(fullPath, slug)
    const numMatch = file.match(/^(\d+)/)
    const num = numMatch ? parseInt(numMatch[1], 10) : 0
    const entry = { text: title, link: `/math/${slug}` }

    if (num >= 1 && num <= 10) g1.items.push(entry)
    else if (num >= 11 && num <= 20) g2.items.push(entry)
    else if (num >= 21 && num <= 30) g3.items.push(entry)
    else if (num >= 31 && num <= 40) g4.items.push(entry)
    else if (num > 0) g5.items.push(entry)
  }

  return [...overview, g1, g2, g3, g4, g5]
}

// Sidebar cho Ngữ Văn 9
function buildLiteratureSidebar(dirPath: string): any[] {
  return [
    { text: '📖 Trung Tâm Ôn Luyện Ngữ Văn 9', link: '/literature/' },
    {
      text: '4 Chuyên Đề Cốt Lõi',
      collapsed: false,
      items: [
        { text: 'Chuyên đề 1: Kỹ Năng Đọc Hiểu Văn Bản', link: '/literature/01_phuong_phap_doc_hieu_van_ban' },
        { text: 'Chuyên đề 2: Cẩm Nang Nghị Luận Xã Hội (200 chữ)', link: '/literature/02_chuyen_de_nghi_luan_xa_hoi' },
        { text: 'Chuyên đề 3: Kỹ Năng Nghị Luận Văn Học Lớp 9', link: '/literature/03_chuyen_de_nghi_luan_van_hoc' },
        { text: 'Chuyên đề 4: Tổng Ôn Toàn Bộ Tiếng Việt Lớp 9', link: '/literature/04_tong_on_tieng_viet_lop_9' }
      ]
    },
    {
      text: 'Bộ Đề Thi & Barem Điểm Chi Tiết',
      collapsed: false,
      items: [
        { text: '📝 Đề Kiểm Tra Giữa Học Kỳ 1 Ngữ Văn 9', link: '/literature/de_thi_giua_hoc_ky_1_ngu_van_9' },
        { text: '🏛️ Đề Minh Họa Tuyển Sinh Vào 10 (Hà Nội & TP.HCM)', link: '/literature/de_thi_tuyen_sinh_vao_10_ngu_van_ha_noi_tphcm' }
      ]
    }
  ]
}

export default defineConfig({
  base: '/Grade10Entrance/',
  title: "Tài Liệu Ôn Tập Vào Lớp 10",
  description: "Tài liệu ôn thi vào lớp 10 môn Toán, Ngữ văn và Tiếng Anh - Toán học, Ngữ văn & Tiếng Anh chuẩn GDPT mới",
  lang: 'vi-VN',
  lastUpdated: true,
  cleanUrls: true,
  ignoreDeadLinks: true,

  markdown: {
    lineNumbers: true,
    theme: {
      light: 'github-light',
      dark: 'one-dark-pro'
    },
    config(md) {
      const defaultFence = md.renderer.rules.fence!
      md.renderer.rules.fence = (tokens, idx, options, env, slf) => {
        const token = tokens[idx]
        const info = (token.info || '').trim()
        if (info.toLowerCase() === 'mermaid') {
          return `<pre class="mermaid">${token.content}</pre>`
        }
        return defaultFence(tokens, idx, options, env, slf)
      }
    }
  },

  themeConfig: {
    siteTitle: "Tài Liệu Ôn Tập",
    nav: [
      { text: 'Trang chủ', link: '/' },
      { text: 'Toán 9 (12 CĐ & 48 Bài) 📐', link: '/math/' },
      { text: 'Ngữ Văn 9 📖', link: '/literature/' },
      { text: 'Tiếng Anh 9 (Lý thuyết) 🇬🇧', link: '/catalog' },
      { text: 'Luyện Đề Tuyển Sinh 🎯', link: '/exams/' }
    ],
    sidebar: {
      '/math/': buildMathSidebar(path.resolve(__dirname, '../math')),
      '/literature/': buildLiteratureSidebar(path.resolve(__dirname, '../literature')),
      '/lessons/': scanDirectoryRecursive(path.resolve(__dirname, '../lessons'), '/lessons'),
      '/exams/': scanDirectoryRecursive(path.resolve(__dirname, '../exams'), '/exams')
    },
    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: { buttonText: 'Tìm kiếm tài liệu (Ctrl+K)...', buttonAriaLabel: 'Tìm kiếm' },
              modal: {
                noResultsText: 'Không tìm thấy nội dung phù hợp',
                resetButtonTitle: 'Xóa tìm kiếm',
                footer: { selectText: 'chọn', navigateText: 'di chuyển', closeText: 'đóng' }
              }
            }
          }
        }
      }
    },
    outline: {
      level: [2, 3],
      label: 'Mục lục bài viết'
    },
    docFooter: {
      prev: '← Bài trước',
      next: 'Bài kế tiếp →'
    }
  }
})
