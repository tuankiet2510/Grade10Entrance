<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { withBase } from 'vitepress'
import { data as lessons, type LessonMeta } from '../../data/lessons.data.ts'

const searchQuery = ref('')
const selectedCategory = ref('Tất cả')
const showBackToTop = ref(false)

const CATEGORY_ORDER = [
  'Tất cả',
  'Bộ Đề Tuyển Sinh Vào 10',
  'Chuyên đề 1: Ngữ Âm & Trọng Âm',
  'Chuyên đề 2: Ngữ Pháp & Cấu Trúc',
  'Chuyên đề 3: Từ Vựng Chọn Lọc',
  'Chuyên đề 4: Biển Báo & Giao Tiếp',
  'Chuyên đề 5: Viết Luận & Đoạn Văn',
  'Chuyên đề 6: 12 Units SGK Lớp 9'
]

const CATEGORY_ICONS: Record<string, string> = {
  'Tất cả': '✨ Tất cả',
  'Bộ Đề Tuyển Sinh Vào 10': '🎯 Đề Thi Tuyển Sinh',
  'Chuyên đề 1: Ngữ Âm & Trọng Âm': '🗣️ Ngữ Âm & Trọng Âm',
  'Chuyên đề 2: Ngữ Pháp & Cấu Trúc': '📐 Ngữ Pháp & Cấu Trúc',
  'Chuyên đề 3: Từ Vựng Chọn Lọc': '📚 Từ Vựng Chọn Lọc',
  'Chuyên đề 4: Biển Báo & Giao Tiếp': '🛑 Biển Báo & Giao Tiếp',
  'Chuyên đề 5: Viết Luận & Đoạn Văn': '✍️ Viết Đoạn Văn',
  'Chuyên đề 6: 12 Units SGK Lớp 9': '📘 12 Units SGK 9'
}

function getCategoryLabel(cat: string): string {
  return CATEGORY_ICONS[cat] || cat
}

// Đếm số lượng bài cho từng danh mục
const categoryCounts = computed(() => {
  const counts: Record<string, number> = { 'Tất cả': lessons.length }
  for (const l of lessons) {
    counts[l.category] = (counts[l.category] || 0) + 1
  }
  return counts
})

const categories = computed(() => {
  const cats = new Set(lessons.map(l => l.category))
  const foundCats = Array.from(cats)

  return CATEGORY_ORDER.filter(c => c === 'Tất cả' || foundCats.includes(c)).concat(
    foundCats.filter(c => !CATEGORY_ORDER.includes(c))
  )
})

const filteredLessons = computed(() => {
  return lessons.filter(lesson => {
    const matchesCat = selectedCategory.value === 'Tất cả' || lesson.category === selectedCategory.value
    const query = searchQuery.value.toLowerCase().trim()
    if (!query) return matchesCat

    return lesson.title.toLowerCase().includes(query) ||
           lesson.description.toLowerCase().includes(query) ||
           lesson.category.toLowerCase().includes(query)
  })
})

function resetFilters() {
  searchQuery.value = ''
  selectedCategory.value = 'Tất cả'
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function handleScroll() {
  showBackToTop.value = window.scrollY > 300
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <div class="catalog-container">
    <!-- KHỐI TÌM KIẾM & BỘ LỌC DANH MỤC -->
    <div class="filter-bar">
      <!-- Ô TÌM KIẾM -->
      <div class="search-box">
        <span class="search-icon" aria-hidden="true">🔍</span>
        <input 
          v-model="searchQuery" 
          type="search" 
          placeholder="Tìm bài học, ngữ pháp, đề thi, chuyên đề..." 
          class="search-input"
          autocomplete="off"
          spellcheck="false"
        />
        <button 
          v-if="searchQuery" 
          class="clear-btn" 
          title="Xóa tìm kiếm" 
          aria-label="Xóa tìm kiếm"
          @click="searchQuery = ''"
        >
          ✕
        </button>
      </div>

      <!-- THANH DANH MỤC (Cuộn ngang mượt mà trên điện thoại) -->
      <div class="category-scroll-wrapper">
        <div class="category-pills" role="tablist" aria-label="Bộ lọc danh mục">
          <button 
            v-for="cat in categories" 
            :key="cat"
            role="tab"
            :aria-selected="selectedCategory === cat"
            :class="['pill-btn', { active: selectedCategory === cat }]"
            @click="selectedCategory = cat"
          >
            <span class="pill-title">{{ getCategoryLabel(cat) }}</span>
            <span class="pill-count">{{ categoryCounts[cat] || 0 }}</span>
          </button>
        </div>
      </div>
    </div>

    <!-- THANH TRẠNG THÁI HIỂN THỊ KẾT QUẢ -->
    <div class="catalog-summary">
      <div class="summary-left">
        <span>Hiển thị <strong>{{ filteredLessons.length }}</strong> / {{ lessons.length }} tài liệu</span>
        <span v-if="selectedCategory !== 'Tất cả'" class="current-filter-badge">
          {{ selectedCategory }}
        </span>
      </div>
      <button 
        v-if="selectedCategory !== 'Tất cả' || searchQuery" 
        class="reset-filter-btn"
        @click="resetFilters"
      >
        ↺ Đặt lại bộ lọc
      </button>
    </div>

    <!-- LƯỚI THẺ BÀI HỌC & ĐỀ THI -->
    <div v-if="filteredLessons.length > 0" class="lessons-grid">
      <a 
        v-for="item in filteredLessons" 
        :key="item.url" 
        :href="withBase(item.url)" 
        :class="['lesson-card', { 'is-exam-card': item.isExam }]"
      >
        <div class="card-header">
          <span :class="['badge', 'category-badge', { 'exam-badge': item.isExam }]">
            {{ item.isExam ? '📝 Đề thi tuyển sinh' : item.category }}
          </span>
          <span class="badge time-badge">
            <template v-if="item.isExam">
              ⏱ {{ item.duration || 60 }} phút
            </template>
            <template v-else>
              📖 {{ item.readingTime }} phút đọc
            </template>
          </span>
        </div>

        <h3 class="card-title">{{ item.title }}</h3>
        
        <p class="card-desc">{{ item.description }}</p>

        <div class="card-footer">
          <span class="action-link">
            <template v-if="item.isExam">
              Làm bài thi <span class="arrow">→</span>
            </template>
            <template v-else>
              Học bài <span class="arrow">→</span>
            </template>
          </span>
          <span class="card-tag">
            <template v-if="item.isExam">
              {{ item.totalQuestions || 36 }} câu trắc nghiệm
            </template>
            <template v-else>
              Lý thuyết & Bài tập
            </template>
          </span>
        </div>
      </a>
    </div>

    <!-- TRẠNG THÁI KHÔNG TÌM THẤY KẾT QUẢ -->
    <div v-else class="empty-state">
      <span class="empty-icon">🔍</span>
      <h3 class="empty-title">Không tìm thấy tài liệu phù hợp</h3>
      <p class="empty-desc">Không có bài học hay đề thi nào khớp với từ khóa "<strong>{{ searchQuery }}</strong>".</p>
      <button class="reset-search-btn" @click="resetFilters">
        Xem tất cả tài liệu
      </button>
    </div>

    <!-- NÚT LÊN ĐẦU TRANG CHO DI ĐỘNG -->
    <button 
      v-show="showBackToTop" 
      class="catalog-back-to-top" 
      title="Lên đầu trang"
      aria-label="Lên đầu trang"
      @click="scrollToTop"
    >
      ↑
    </button>
  </div>
</template>

<style scoped>
.catalog-container {
  margin-top: 1rem;
  width: 100%;
  box-sizing: border-box;
}

/* KHỐI BỘ LỌC */
.filter-bar {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.25rem;
}

/* Ô TÌM KIẾM - ĐẠT CHUẨN 16px TRÁNH AUTO-ZOOM TRÊN IPHONE SAFARI */
.search-box {
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
}

.search-icon {
  position: absolute;
  left: 1rem;
  font-size: 1rem;
  opacity: 0.55;
  pointer-events: none;
}

.search-input {
  width: 100%;
  height: 46px;
  padding: 0 2.5rem 0 2.65rem;
  border-radius: 12px;
  border: 1.5px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  /* BẮT BUỘC >= 16px để iOS Safari không tự ý phóng to (zoom in) gây tuột/vỡ giao diện */
  font-size: 16px !important;
  font-family: var(--vp-font-family-base);
  outline: none;
  box-sizing: border-box;
  transition: all 0.2s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
}

.search-input:focus {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 0 0 3px var(--vp-c-brand-soft);
  background: var(--vp-c-bg);
}

.clear-btn {
  position: absolute;
  right: 0.75rem;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: none;
  font-size: 0.88rem;
  color: var(--vp-c-text-3);
  cursor: pointer;
  border-radius: 50%;
  transition: all 0.15s ease;
}

.clear-btn:hover {
  background: var(--vp-c-divider);
  color: var(--vp-c-text-1);
}

/* THANH DANH MỤC: Cuộn ngang mượt mà trên Mobile, bao bọc gọn trên Desktop */
.category-scroll-wrapper {
  width: 100%;
  overflow: hidden;
}

.category-pills {
  display: flex;
  gap: 0.5rem;
  padding: 2px 2px 6px 2px;
  /* Mặc định trên desktop: wrap tự nhiên */
  flex-wrap: wrap;
}

/* TỐI ƯU HÓA MOBILE (IPHONE & ANDROID): CUỘN NGANG 1 DÒNG DUY NHẤT */
@media (max-width: 840px) {
  .category-scroll-wrapper {
    margin: 0 -12px;
    padding: 0 12px;
    width: calc(100% + 24px);
  }

  .category-pills {
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
    scroll-snap-type: x mandatory;
    gap: 0.45rem;
    padding-bottom: 8px;
  }

  .category-pills::-webkit-scrollbar {
    display: none;
  }

  .pill-btn {
    flex-shrink: 0 !important;
    scroll-snap-align: start;
    white-space: nowrap !important;
  }
}

.pill-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.45rem 0.85rem;
  border-radius: 9999px;
  font-size: 0.84rem;
  border: 1.5px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  font-weight: 500;
  user-select: none;
}

.pill-btn:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
  transform: translateY(-1px);
}

.pill-btn.active {
  background: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
  color: #ffffff;
  font-weight: 600;
  box-shadow: 0 3px 10px rgba(37, 99, 235, 0.25);
}

.pill-count {
  font-size: 0.72rem;
  padding: 0.1rem 0.4rem;
  border-radius: 9999px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-3);
  font-weight: 600;
}

.pill-btn.active .pill-count {
  background: rgba(255, 255, 255, 0.25);
  color: #ffffff;
}

/* THANH TRẠNG THÁI HIỂN THỊ KẾT QUẢ */
.catalog-summary {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.88rem;
  color: var(--vp-c-text-3);
  margin-bottom: 1.25rem;
  padding-bottom: 0.65rem;
  border-bottom: 1px solid var(--vp-c-divider);
  gap: 0.5rem;
  flex-wrap: wrap;
}

.summary-left {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.current-filter-badge {
  font-size: 0.75rem;
  padding: 0.15rem 0.5rem;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  border-radius: 6px;
  font-weight: 600;
}

.reset-filter-btn {
  background: transparent;
  border: none;
  font-size: 0.82rem;
  color: var(--vp-c-brand-1);
  cursor: pointer;
  font-weight: 600;
  padding: 0.2rem 0.4rem;
}

.reset-filter-btn:hover {
  text-decoration: underline;
}

/* LƯỚI THẺ BÀI HỌC VÀ ĐỀ THI */
.lessons-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.15rem;
  width: 100%;
  box-sizing: border-box;
}

@media (max-width: 640px) {
  .lessons-grid {
    grid-template-columns: 1fr !important;
    gap: 0.95rem;
  }
}

.lesson-card {
  display: flex;
  flex-direction: column;
  padding: 1.25rem 1.35rem;
  border-radius: 14px;
  border: 1.5px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  text-decoration: none !important;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
  box-sizing: border-box;
}

.lesson-card:hover {
  transform: translateY(-3px);
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 8px 24px rgba(37, 99, 235, 0.08);
  background: var(--vp-c-bg);
}

.lesson-card.is-exam-card {
  border-left: 4px solid var(--vp-c-brand-1);
}

.dark .lesson-card {
  background: #111827;
  border-color: rgba(255, 255, 255, 0.08);
}

.dark .lesson-card:hover {
  background: #172033;
  border-color: #3b82f6;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
  gap: 0.5rem;
}

.badge {
  font-size: 0.72rem;
  padding: 0.22rem 0.55rem;
  border-radius: 6px;
  font-weight: 600;
}

.category-badge {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  max-width: 65%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.category-badge.exam-badge {
  background: rgba(37, 99, 235, 0.12);
  color: #2563eb;
}

.dark .category-badge.exam-badge {
  background: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
}

.time-badge {
  color: var(--vp-c-text-3);
  font-weight: 500;
  white-space: nowrap;
  font-size: 0.75rem;
}

.card-title {
  margin: 0 0 0.5rem 0;
  font-family: 'Outfit', var(--vp-font-family-base);
  font-size: 1.12rem;
  color: var(--vp-c-text-1);
  font-weight: 700;
  line-height: 1.45;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-desc {
  font-size: 0.88rem;
  color: var(--vp-c-text-2);
  flex-grow: 1;
  margin-bottom: 1rem;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid var(--vp-c-divider);
  padding-top: 0.75rem;
}

.action-link {
  font-size: 0.86rem;
  font-weight: 600;
  color: var(--vp-c-brand-1);
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

.arrow {
  transition: transform 0.2s ease;
}

.lesson-card:hover .arrow {
  transform: translateX(4px);
}

.card-tag {
  font-size: 0.74rem;
  color: var(--vp-c-text-3);
}

/* EMPTY STATE */
.empty-state {
  text-align: center;
  padding: 3rem 1.5rem;
  background: var(--vp-c-bg-soft);
  border-radius: 16px;
  border: 1.5px dashed var(--vp-c-divider);
  margin: 2rem 0;
}

.empty-icon {
  font-size: 2.5rem;
  display: block;
  margin-bottom: 0.75rem;
  opacity: 0.6;
}

.empty-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  margin-bottom: 0.5rem;
}

.empty-desc {
  font-size: 0.92rem;
  color: var(--vp-c-text-2);
  margin-bottom: 1.25rem;
}

.reset-search-btn {
  padding: 0.65rem 1.25rem;
  border-radius: 8px;
  background: var(--vp-c-brand-1);
  color: #ffffff;
  border: none;
  font-weight: 600;
  font-size: 0.88rem;
  cursor: pointer;
}

/* NÚT BACK TO TOP CHO DI ĐỘNG */
.catalog-back-to-top {
  position: fixed;
  bottom: 24px;
  right: 20px;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--vp-c-brand-1);
  color: #ffffff;
  border: none;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
  font-size: 1.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 50;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.catalog-back-to-top:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(37, 99, 235, 0.45);
}

@media (max-width: 480px) {
  .lesson-card {
    padding: 1.1rem 1.15rem;
  }
}
</style>
