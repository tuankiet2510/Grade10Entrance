---
title: "Chuyên đề 05: Phương trình tích"
description: "Tài liệu chi tiết chuyên đề Phương trình tích - Ôn thi vào 10 môn Toán"
---

# Chuyên đề 05: Phương trình tích

<div class="custom-block tip" style="margin-bottom: 1.5rem;">
  <p class="custom-block-title">Thông tin chuyên đề</p>
  <p><strong>📖 Số lượng bài học:</strong> 2 bài &nbsp;|&nbsp; <strong>📝 Bài tập vận dụng:</strong> 10 câu có lời giải chi tiết</p>
  <p>Tài liệu được biên soạn chuẩn hóa theo chương trình GDPT mới, giữ nguyên đầy đủ công thức MathJax, hình học và bài tập tự luyện.</p>
</div>

<div class="math-action-bar">
  <a :href="topicUrl" target="_blank" class="math-action-btn primary-btn">
    Mở bản in ấn / Xem toàn màn hình ↗
  </a>
  <a href="/math/" class="math-action-btn secondary-btn">
    ← Quay lại danh mục Toán
  </a>
</div>

<div class="math-topic-embed-container">
  <iframe 
    :src="topicUrl" 
    title="Chuyên đề 05: Phương trình tích"
    class="math-topic-iframe"
    loading="lazy">
  </iframe>
</div>

<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'

const { site } = useData()
const topicUrl = computed(() => `${site.value.base}math-topics/05_Phuong_trinh_tich.html`)
</script>

<style>
.math-action-bar {
  margin: 1.25rem 0;
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}
.math-action-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 18px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 14px;
  text-decoration: none !important;
  transition: all 0.2s ease;
  min-height: 44px;
}
.primary-btn {
  background: var(--vp-c-brand-1, #2563eb);
  color: #ffffff !important;
}
.primary-btn:hover {
  background: var(--vp-c-brand-2, #1d4ed8);
  transform: translateY(-1px);
}
.secondary-btn {
  background: var(--vp-c-bg-mute, #f1f5f9);
  color: var(--vp-c-text-1, #1e293b) !important;
  border: 1px solid var(--vp-c-border, #e2e8f0);
}
.secondary-btn:hover {
  background: var(--vp-c-bg-soft, #e2e8f0);
}
.math-topic-embed-container {
  width: 100%;
  height: 82vh;
  min-height: 650px;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--vp-c-border, #e2e8f0);
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  margin-top: 1.5rem;
  background: #ffffff;
}
.math-topic-iframe {
  width: 100%;
  height: 100%;
  border: none;
}
@media (max-width: 768px) {
  .math-topic-embed-container {
    height: 70vh;
    min-height: 480px;
  }
  .math-action-bar {
    flex-direction: column;
  }
  .math-action-btn {
    width: 100%;
    text-align: center;
  }
}
</style>
