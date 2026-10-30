import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import LessonCatalog from './components/LessonCatalog.vue'
import QuizItem from './components/QuizItem.vue'
import ExamHeader from './components/ExamHeader.vue'
import ExamScoreboard from './components/ExamScoreboard.vue'
import LayoutToggles from './components/LayoutToggles.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'layout-bottom': () => h(LayoutToggles)
    })
  },
  enhanceApp({ app, router }) {
    app.component('LessonCatalog', LessonCatalog)
    app.component('QuizItem', QuizItem)
    app.component('ExamHeader', ExamHeader)
    app.component('ExamScoreboard', ExamScoreboard)
    app.component('LayoutToggles', LayoutToggles)

    if (typeof window !== 'undefined') {
      import('mermaid').then(m => {
        let isRendering = false
        let observerAttached = false

        const renderDiagrams = (force = false) => {
          if (isRendering) return
          isRendering = true

          setTimeout(() => {
            try {
              const isDark = document.documentElement.classList.contains('dark')
              m.default.initialize({
                startOnLoad: false,
                theme: 'base',
                flowchart: {
                  curve: 'basis',
                  nodeSpacing: 16,
                  rankSpacing: 24,
                  padding: 10,
                  useMaxWidth: true
                },
                themeVariables: isDark ? {
                  darkMode: true,
                  background: '#111827',
                  primaryColor: '#1e293b',
                  primaryTextColor: '#f8fafc',
                  primaryBorderColor: '#3b82f6',
                  lineColor: '#64748b',
                  secondaryColor: '#0f172a',
                  secondaryTextColor: '#f8fafc',
                  secondaryBorderColor: '#10b981',
                  tertiaryColor: '#1e1b4b',
                  tertiaryTextColor: '#f8fafc',
                  tertiaryBorderColor: '#8b5cf6',
                  textColor: '#f8fafc',
                  mainBkg: '#1e293b',
                  nodeBorder: '#3b82f6',
                  nodeTextColor: '#f8fafc',
                  edgeLabelBackground: '#1e293b',
                  fontFamily: "'Plus Jakarta Sans', -apple-system, sans-serif",
                  fontSize: '13px'
                } : {
                  darkMode: false,
                  background: '#f8fafc',
                  primaryColor: '#eff6ff',
                  primaryTextColor: '#0f172a',
                  primaryBorderColor: '#2563eb',
                  lineColor: '#94a3b8',
                  secondaryColor: '#f0fdf4',
                  secondaryTextColor: '#065f46',
                  secondaryBorderColor: '#10b981',
                  tertiaryColor: '#fffbeb',
                  tertiaryTextColor: '#92400e',
                  tertiaryBorderColor: '#f59e0b',
                  textColor: '#0f172a',
                  mainBkg: '#ffffff',
                  nodeBorder: '#cbd5e1',
                  nodeTextColor: '#0f172a',
                  edgeLabelBackground: '#ffffff',
                  fontFamily: "'Plus Jakarta Sans', -apple-system, sans-serif",
                  fontSize: '13px'
                }
              })

              const elements = document.querySelectorAll('.mermaid')
              if (elements.length > 0) {
                elements.forEach(el => {
                  if (!el.getAttribute('data-original-code')) {
                    el.setAttribute('data-original-code', el.textContent || '')
                  } else if (force) {
                    el.removeAttribute('data-processed')
                    el.innerHTML = el.getAttribute('data-original-code') || ''
                  }
                })

                m.default.run({ nodes: elements }).then(() => {
                  const isDarkNow = document.documentElement.classList.contains('dark')
                  document.querySelectorAll('.mermaid svg').forEach(svg => {
                    const elSvg = svg as HTMLElement
                    elSvg.style.maxWidth = 'min(100%, 750px)'
                    elSvg.style.height = 'auto'
                    elSvg.style.margin = '0 auto'
                    elSvg.style.display = 'block'

                    svg.querySelectorAll('.node').forEach(node => {
                      const shape = node.querySelector('rect, circle, polygon, path.basic') as HTMLElement | null
                      const textEls = node.querySelectorAll('.label, .label *, text, tspan')

                      if (!shape) return

                      const styleAttr = shape.getAttribute('style') || ''
                      const fillAttr = shape.getAttribute('fill') || ''
                      const combined = (styleAttr + ' ' + fillAttr).toLowerCase()

                      const isRoot = combined.includes('#2563eb') || combined.includes('37, 99, 235') || combined.includes('rgb(37,99,235)')
                      const isBlue = combined.includes('#eff6ff') || combined.includes('239, 246, 255') || combined.includes('rgb(239,246,255)')
                      const isGreen = combined.includes('#dcfce7') || combined.includes('#f0fdf4') || combined.includes('220, 252, 231') || combined.includes('240, 253, 244')
                      const isAmber = combined.includes('#fef3c7') || combined.includes('#fefce8') || combined.includes('#fffbeb') || combined.includes('254, 243, 199') || combined.includes('254, 252, 232')
                      const isPurple = combined.includes('#ede9fe') || combined.includes('#faf5ff') || combined.includes('237, 233, 254')
                      const isRose = combined.includes('#fee2e2') || combined.includes('#fef2f2') || combined.includes('#fff1f2') || combined.includes('254, 226, 226')
                      const isSlate = combined.includes('#f1f5f9') || combined.includes('241, 245, 249')

                      if (isDarkNow) {
                        if (isRoot) {
                          shape.style.fill = '#1d4ed8'
                          shape.style.stroke = '#60a5fa'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#ffffff'; el.style.fill = '#ffffff'; el.style.fontWeight = '700' })
                        } else if (isBlue) {
                          shape.style.fill = '#172554'
                          shape.style.stroke = '#3b82f6'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#bfdbfe'; el.style.fill = '#bfdbfe'; el.style.fontWeight = '700' })
                        } else if (isGreen) {
                          shape.style.fill = '#052e16'
                          shape.style.stroke = '#10b981'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#a7f3d0'; el.style.fill = '#a7f3d0'; el.style.fontWeight = '700' })
                        } else if (isAmber) {
                          shape.style.fill = '#451a03'
                          shape.style.stroke = '#f59e0b'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#fde68a'; el.style.fill = '#fde68a'; el.style.fontWeight = '700' })
                        } else if (isPurple) {
                          shape.style.fill = '#2e1065'
                          shape.style.stroke = '#a855f7'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#e9d5ff'; el.style.fill = '#e9d5ff'; el.style.fontWeight = '700' })
                        } else if (isRose) {
                          shape.style.fill = '#4c0519'
                          shape.style.stroke = '#f43f5e'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#fecdd3'; el.style.fill = '#fecdd3'; el.style.fontWeight = '700' })
                        } else if (isSlate) {
                          shape.style.fill = '#1e293b'
                          shape.style.stroke = '#64748b'
                          shape.style.strokeWidth = '1.5px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#f8fafc'; el.style.fill = '#f8fafc'; el.style.fontWeight = '600' })
                        } else {
                          shape.style.fill = '#1e293b'
                          shape.style.stroke = '#3b82f6'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#f8fafc'; el.style.fill = '#f8fafc'; el.style.fontWeight = '600' })
                        }
                      } else {
                        // Light mode
                        if (isRoot) {
                          shape.style.fill = '#2563eb'
                          shape.style.stroke = '#1d4ed8'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#ffffff'; el.style.fill = '#ffffff'; el.style.fontWeight = '700' })
                        } else if (isBlue) {
                          shape.style.fill = '#eff6ff'
                          shape.style.stroke = '#3b82f6'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#1e3a8a'; el.style.fill = '#1e3a8a'; el.style.fontWeight = '700' })
                        } else if (isGreen) {
                          shape.style.fill = '#f0fdf4'
                          shape.style.stroke = '#16a34a'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#14532d'; el.style.fill = '#14532d'; el.style.fontWeight = '700' })
                        } else if (isAmber) {
                          shape.style.fill = '#fffbeb'
                          shape.style.stroke = '#d97706'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#78350f'; el.style.fill = '#78350f'; el.style.fontWeight = '700' })
                        } else if (isPurple) {
                          shape.style.fill = '#faf5ff'
                          shape.style.stroke = '#9333ea'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#4c1d95'; el.style.fill = '#4c1d95'; el.style.fontWeight = '700' })
                        } else if (isRose) {
                          shape.style.fill = '#fff1f2'
                          shape.style.stroke = '#e11d48'
                          shape.style.strokeWidth = '2px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#881337'; el.style.fill = '#881337'; el.style.fontWeight = '700' })
                        } else if (isSlate) {
                          shape.style.fill = '#f8fafc'
                          shape.style.stroke = '#94a3b8'
                          shape.style.strokeWidth = '1.5px'
                          textEls.forEach(t => { const el = t as HTMLElement; el.style.color = '#0f172a'; el.style.fill = '#0f172a'; el.style.fontWeight = '700' })
                        }
                      }
                    })

                    svg.querySelectorAll('.edgeLabel, .edgeLabel span, .edgeLabel p').forEach(el => {
                      const h = el as HTMLElement
                      h.style.backgroundColor = isDarkNow ? '#0b1120' : '#f8fafc'
                      h.style.color = isDarkNow ? '#94a3b8' : '#475569'
                      h.style.fill = isDarkNow ? '#94a3b8' : '#475569'
                    })
                  })
                }).catch(err => {
                  console.warn('Mermaid rendering error:', err)
                }).finally(() => {
                  isRendering = false
                })
              } else {
                isRendering = false
              }
            } catch (e) {
              isRendering = false
            }
          }, 80)
        }

        router.onAfterRouteChanged = () => renderDiagrams(false)
        window.addEventListener('load', () => renderDiagrams(false))

        if (!observerAttached) {
          observerAttached = true
          const observer = new MutationObserver((mutations) => {
            for (const mutation of mutations) {
              if (mutation.attributeName === 'class') {
                renderDiagrams(true)
                break
              }
            }
          })
          observer.observe(document.documentElement, {
            attributes: true,
            attributeFilter: ['class']
          })
        }
      }).catch(err => {
        console.warn('Mermaid chưa được cài đặt hoặc bỏ qua:', err)
      })
    }
  }
}

