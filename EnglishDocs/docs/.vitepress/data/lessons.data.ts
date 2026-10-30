import { createContentLoader } from 'vitepress'

const MODULE_NAMES: Record<string, string> = {
  "chuyen_de_1": "Chuyên đề 1: Ngữ Âm & Trọng Âm",
  "chuyen_de_2": "Chuyên đề 2: Ngữ Pháp & Cấu Trúc",
  "chuyen_de_3": "Chuyên đề 3: Từ Vựng Chọn Lọc",
  "chuyen_de_4": "Chuyên đề 4: Biển Báo & Giao Tiếp",
  "chuyen_de_5": "Chuyên đề 5: Viết Luận & Đoạn Văn",
  "chuyen_de_6": "Chuyên đề 6: 12 Units SGK Lớp 9",
  "exams": "Bộ Đề Tuyển Sinh Vào 10"
}

export interface LessonMeta {
  title: string
  url: string
  category: string
  description: string
  readingTime: number
  wordCount: number
  sourceType: string
  isExam: boolean
  duration?: number
  totalQuestions?: number
}

declare const data: LessonMeta[]
export { data }

export default createContentLoader(['lessons/**/*.md', 'exams/**/*.md'], {
  includeSrc: true,
  transform(raw): LessonMeta[] {
    return raw
      .filter(({ url }) => {
        if (!url || url.endsWith('/lessons/') || url.endsWith('/exams/') || url.toLowerCase().endsWith('/readme.html')) return false
        // Lọc bỏ file devlog guide.md và các thư mục tạm / UUID Notion / superpowers
        if (url.includes('/guide') || url.includes('c674a7bc') || url.includes('ExportBlock') || url.includes('superpowers')) return false
        return true
      })
      .map(({ url, frontmatter, src }) => {
        const parts = url.split('/')
        const fileName = parts[parts.length - 1] || ''

        let catKey = 'general'
        if (fileName.startsWith('chuyen_de_1')) catKey = 'chuyen_de_1'
        else if (fileName.startsWith('chuyen_de_2') || fileName.startsWith('de_cuong')) catKey = 'chuyen_de_2'
        else if (fileName.startsWith('chuyen_de_3')) catKey = 'chuyen_de_3'
        else if (fileName.startsWith('chuyen_de_4')) catKey = 'chuyen_de_4'
        else if (fileName.startsWith('chuyen_de_5')) catKey = 'chuyen_de_5'
        else if (fileName.startsWith('chuyen_de_6') || fileName.startsWith('unit_')) catKey = 'chuyen_de_6'
        else if (fileName.includes('exam') || fileName.includes('de_thi') || fileName.includes('qng') || fileName.includes('36_cau') || fileName.includes('45_cau')) catKey = 'exams'

        const isExam = url.includes('/exams/') || catKey === 'exams'
        let category = frontmatter.category
        if (!category || category === 'Ngữ Pháp Trọng Tâm' || category === 'Tài Liệu Phương Pháp' || category === 'Cẩm Nang Phương Pháp' || category === 'Tài Liệu Phương Pháp Học Tập') {
          category = MODULE_NAMES[catKey] || (isExam ? 'Bộ Đề Tuyển Sinh Vào 10' : 'Chuyên đề 2: Ngữ Pháp & Cấu Trúc')
        }

        let title = frontmatter.title
        if (!title && src) {
          const match = src.match(/^#\s+(.+)$/m)
          if (match) title = match[1].replace(/[\x60*]/g, '').trim()
        }
        if (!title) {
          title = fileName.replace('.html', '').replace(/[-_]/g, ' ') || 'Tài liệu'
        }

        const wordCount = (src || '').trim().split(/\s+/).length
        const readingTime = Math.max(1, Math.ceil(wordCount / 200))

        let duration = frontmatter.duration || (isExam ? (fileName.includes('2026_2027') ? 90 : 60) : undefined)
        let totalQuestions = frontmatter.total || (isExam ? (fileName.includes('36_cau') ? 36 : (fileName.includes('45_cau') ? 45 : 36)) : undefined)

        let description = frontmatter.description
        if (!description && src) {
          const cleanSrc = src.replace(/^---[\s\S]*?---/, '')
          const lines = cleanSrc.split('\n')
          for (const rawLine of lines) {
            let line = rawLine.trim()
            if (!line || line.startsWith('#') || line.startsWith('```') || line.startsWith('|') || line.startsWith('---')) continue

            line = line.replace(/^>\s*(\[![\w-]+\])?\s*/i, '')
            line = line.replace(/\*\*([^*]+)\*\*/g, '$1')
            line = line.replace(/\*([^*]+)\*/g, '$1')
            line = line.replace(/`([^`]+)`/g, '$1')
            line = line.replace(/^[-*]\s+/, '')
            line = line.trim()

            if (line.length > 25) {
              description = line.slice(0, 160) + (line.length > 160 ? '...' : '')
              break
            }
          }
        }

        // Làm sạch mô tả tránh lặp từ
        if (description) {
          description = description.replace(/rèn luyện luyện tập/g, 'luyện thi')
        }

        return {
          title,
          description: description || 'Tài liệu ôn tập chuyên sâu môn Tiếng Anh vào lớp 10 chuẩn GDPT mới.',
          category,
          readingTime,
          wordCount,
          sourceType: frontmatter.source_type || 'markdown',
          isExam,
          duration,
          totalQuestions,
          url
        }
      })
      .sort((a, b) => a.url.localeCompare(b.url, undefined, { numeric: true }))
  }
})
