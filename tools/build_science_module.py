import os

SCIENCE_DIR = r"f:\OnThiC3\EnglishDocs\docs\science"
os.makedirs(SCIENCE_DIR, exist_ok=True)

# 1. index.md
science_index = r"""---
title: "Trung Tâm Ôn Luyện Khoa Học Tự Nhiên 9 - Kết Nối Tri Thức"
description: "Sổ tay toàn diện công thức và kiến thức trọng tâm 3 phân môn Vật lí, Hóa học và Sinh học lớp 9 theo chương trình GDPT 2018 bộ sách Kết nối tri thức với cuộc sống."
---

# 🔬 Trung Tâm Ôn Luyện Khoa Học Tự Nhiên 9 (Kết Nối Tri Thức)

<div class="math-hero-stats">
  <div class="stat-box">
    <div class="stat-number">3</div>
    <div class="stat-label">Phân môn tích hợp (Lý - Hóa - Sinh)</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">100%</div>
    <div class="stat-label">Chuẩn SGK Kết Nối Tri Thức</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">120+</div>
    <div class="stat-label">Công thức &amp; Phương trình cốt lõi</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">Ôn Thi 10</div>
    <div class="stat-label">Đề khảo sát &amp; Thi tuyển sinh</div>
  </div>
</div>

::: info Định hướng phân môn Khoa học tự nhiên 9
Môn **Khoa học tự nhiên 9** là sự tích hợp logic và chặt chẽ của 3 phân môn nền tảng:
- **Vật lí 9:** Động lượng và cơ năng; Khúc xạ ánh sáng và Thấu kính; Điện học và Định luật Ohm; Cảm ứng điện từ và Máy biến thế.
- **Hóa học 9:** Dãy hoạt động hóa học của Kim loại; Phi kim và Bảng tuần hoàn; Hợp chất hữu cơ (Hiđrocacbon, Rượu etylic, Axit axetic, Chất béo, Cacbohidrat, Polime).
- **Sinh học 9:** Di truyền học Mendel; Nhiễm sắc thể và Phân bào (Nguyên phân, Giảm phân); Di truyền phân tử (ADN - ARN - Protein); Đột biến sinh học; Hệ sinh thái và Bảo vệ môi trường.
:::

---

## 📚 3 Sổ Tay Chuyên Đề Trọng Tâm KHTN 9

<div class="pdf-exam-grid">
  <div class="pdf-card">
    <div class="pdf-card-badge">Phân Môn Vật Lí • Sổ tay công thức</div>
    <h3 class="pdf-card-title">Sổ Tay Công Thức &amp; Lý Thuyết Vật Lí 9</h3>
    <p class="pdf-card-desc">Tổng hợp toàn bộ công thức: Động lượng, Cơ năng, Khúc xạ ánh sáng, Thấu kính hội tụ/phân kỳ, Định luật Ohm, Điện năng tiêu thụ, Công suất hao phí truyền tải điện.</p>
    <div class="pdf-card-actions">
      <a href="./01_vat_li_9_cong_thuc_va_ly_thuyet" class="pdf-btn view-btn">Xem Sổ Tay Vật Lí ↗</a>
    </div>
  </div>

  <div class="pdf-card">
    <div class="pdf-card-badge">Phân Môn Hóa Học • Phản ứng &amp; Phương trình</div>
    <h3 class="pdf-card-title">Sổ Tay Lý Thuyết &amp; Phương Trình Hóa Học 9</h3>
    <p class="pdf-card-desc">Bảng tính tan, Dãy hoạt động hóa học của kim loại, Phương trình điều chế &amp; phản ứng đặc trưng của Metan, Etilen, Axetilen, Rượu etylic, Axit axetic, Este hóa và Tính toán mol mới (24.79L).</p>
    <div class="pdf-card-actions">
      <a href="./02_hoa_hoc_9_ly_thuyet_va_phuong_trinh" class="pdf-btn view-btn">Xem Sổ Tay Hóa Học ↗</a>
    </div>
  </div>

  <div class="pdf-card">
    <div class="pdf-card-badge">Phân Môn Sinh Học • Di truyền &amp; Sinh thái</div>
    <h3 class="pdf-card-title">Sổ Tay Di Truyền &amp; Sinh Thái Học Sinh Học 9</h3>
    <p class="pdf-card-desc">Quy luật di truyền Mendel, Bảng đối chiếu Nguyên phân &amp; Giảm phân, Cơ chế nhân đôi ADN, Phiên mã, Dịch mã tổng hợp Protein, Các dạng đột biến và Cấu trúc Hệ sinh thái.</p>
    <div class="pdf-card-actions">
      <a href="./03_sinh_hoc_9_di_truyen_va_sinh_thai" class="pdf-btn view-btn">Xem Sổ Tay Sinh Học ↗</a>
    </div>
  </div>
</div>
"""

with open(os.path.join(SCIENCE_DIR, "index.md"), "w", encoding="utf-8") as f:
    f.write(science_index)
print("Created science/index.md")

# 2. 01_vat_li_9_cong_thuc_va_ly_thuyet.md
vat_li_content = r"""---
title: "Sổ Tay Công Thức & Lý Thuyết Vật Lí 9 (KHTN 9 - Kết Nối Tri Thức)"
category: "Khoa Học Tự Nhiên 9"
description: "Tổng hợp toàn bộ công thức và lý thuyết phân môn Vật lí 9: Cơ học, Quang học khúc xạ & thấu kính, Điện học định luật Ohm, Cảm ứng điện từ và truyền tải điện năng."
---

# ⚡ Sổ Tay Công Thức & Lý Thuyết Vật Lí 9 (Kết Nối Tri Thức)

::: info Định hướng ôn tập phân môn Vật lí lớp 9
Phân môn Vật lí trong bộ sách KHTN 9 Kết nối tri thức bao gồm 4 mảng kiến thức trụ cột:
1. **Cơ học & Năng lượng:** Động lượng, Động năng, Thế năng và Định luật bảo toàn cơ năng.
2. **Quang học:** Hiện tượng khúc xạ ánh sáng, Phản xạ toàn phần, Thấu kính hội tụ & Thấu kính phân kỳ.
3. **Điện học:** Định luật Ohm cho toàn mạch, Đoạn mạch nối tiếp và song song, Điện năng tiêu thụ và Công suất điện.
4. **Từ học & Năng lượng điện:** Cảm ứng điện từ, Dòng điện xoay chiều, Máy biến áp và Bài toán hao phí truyền tải điện năng.
:::

---

## I. CƠ HỌC: ĐỘNG LƯỢNG & NĂNG LƯỢNG CƠ HỌC

### 1. Động lượng (Momentum)
- **Định nghĩa:** Động lượng $\vec{p}$ của một vật khối lượng $m$ chuyển động với vận tốc $\vec{v}$ là đại lượng vectơ cùng hướng với vận tốc:
  $$\vec{p} = m \cdot \vec{v} \implies p = m \cdot v$$
  *(Đơn vị: $\text{kg}\cdot\text{m/s}$)*
- **Định luật bảo toàn động lượng:** Trong một hệ kín (không chịu ngoại lực tác dụng), tổng động lượng của hệ trước và sau va chạm luôn được bảo toàn:
  $$\vec{p}_1 + \vec{p}_2 = \vec{p}'_1 + \vec{p}'_2$$

### 2. Cơ năng (Mechanical Energy)
- **Động năng ($W_đ$):** Năng lượng do vật chuyển động mà có:
  $$W_đ = \dfrac{1}{2}m v^2$$
- **Thế năng trọng trường ($W_t$):** Năng lượng tương tác giữa Trái Đất và vật ở độ cao $h$:
  $$W_t = m \cdot g \cdot h$$
  *(với $g \approx 9.8 \text{ m/s}^2$ hoặc $10 \text{ m/s}^2$)*
- **Cơ năng toàn phần ($W$):**
  $$W = W_đ + W_t = \dfrac{1}{2}m v^2 + mgh$$
- **Định luật bảo toàn cơ năng:** Khi một vật chỉ chịu tác dụng của trọng lực, cơ năng của vật là một đại lượng bảo toàn:
  $$W = \text{const} \Longleftrightarrow W_{đ1} + W_{t1} = W_{đ2} + W_{t2}$$

---

## II. QUANG HỌC: KHÚC XẠ ÁNH SÁNG & THẤU KÍNH

### 1. Hiện tượng khúc xạ ánh sáng & Định luật khúc xạ
- **Định luật khúc xạ ánh sáng:**
  - Tia khúc xạ nằm trong mặt phẳng tới và ở bên kia pháp tuyến so với tia tới.
  - Tỉ số giữa $\sin$ góc tới ($i$) và $\sin$ góc khúc xạ ($r$) luôn không đổi đối với hai môi trường trong suốt nhất định:
    $$n_1 \sin i = n_2 \sin r \quad \text{hay} \quad \dfrac{\sin i}{\sin r} = \dfrac{n_2}{n_1} = n_{21}$$

### 2. Hiện tượng phản xạ toàn phần
- **Điều kiện để xảy ra hiện tượng phản xạ toàn phần:**
  1. Ánh sáng truyền từ môi trường chiết quang hơn sang môi trường chiết quang kém hơn ($n_1 > n_2$).
  2. Góc tới $i \ge i_{gh}$ (với góc giới hạn $\sin i_{gh} = \dfrac{n_2}{n_1}$).

### 3. Thấu kính hội tụ (TKHT) và Thấu kính phân kỳ (TKPK)

| Đặc điểm | Thấu kính hội tụ (Rìa mỏng) | Thấu kính phân kỳ (Rìa dày) |
| :--- | :--- | :--- |
| **Ký hiệu** | Mũi tên hướng ra ngoài ($\updownarrow$) | Mũi tên hướng vào trong ($\downleftrightarrow$) |
| **Chùm tia tới song song**| Cho chùm tia ló hội tụ tại tiêu điểm $F'$ | Cho chùm tia ló phân kỳ loe rộng ra |
| **Đặc điểm ảnh tạo bởi vật thật**| - $d > 2f$: Ảnh **thật, ngược chiều, nhỏ hơn vật**<br>- $d = 2f$: Ảnh **thật, ngược chiều, bằng vật**<br>- $f < d < 2f$: Ảnh **thật, ngược chiều, lớn hơn vật**<br>- $d < f$: Ảnh **ảo, cùng chiều, lớn hơn vật** | Luôn cho **ảnh ảo, cùng chiều và nhỏ hơn vật**, nằm trong khoảng tiêu cự. |

#### Công thức Thấu kính dùng giải bài toán hình học:
$$\dfrac{1}{f} = \dfrac{1}{d} + \dfrac{1}{d'} \quad \text{và} \quad k = \dfrac{A'B'}{AB} = \dfrac{d'}{d}$$
> *Quy ước dấu:*
> - Ảnh thật: $d' > 0$; Ảnh ảo: $d' < 0$.
> - Thấu kính hội tụ: $f > 0$; Thấu kính phân kỳ: $f < 0$.

---

## III. ĐIỆN HỌC: ĐỊNH LUẬT OHM & ĐOẠN MẠCH

```mermaid
flowchart LR
    A["ĐIỆN HỌC LỚP 9"] --> B["Đoạn mạch nối tiếp<br/>I = I₁ = I₂<br/>U = U₁ + U₂<br/>R = R₁ + R₂"]
    A --> C["Đoạn mạch song song<br/>I = I₁ + I₂<br/>U = U₁ = U₂<br/>1/R = 1/R₁ + 1/R₂"]
    A --> D["Công & Công suất điện<br/>P = U·I = I²·R<br/>A = P·t = U·I·t<br/>Q = I²·R·t (Joule-Lenz)"]
```

### 1. Định luật Ohm cho đoạn mạch
$$I = \dfrac{U}{R} \implies U = I \cdot R, \quad R = \dfrac{U}{I}$$

### 2. Bảng so sánh Đoạn mạch nối tiếp và Đoạn mạch song song

| Đại lượng | Đoạn mạch gồm $R_1$ nối tiếp $R_2$ | Đoạn mạch gồm $R_1$ song song $R_2$ |
| :--- | :--- | :--- |
| **Cường độ dòng điện ($I$)** | $I = I_1 = I_2$ | $I = I_1 + I_2$ |
| **Hiệu điện thế ($U$)** | $U = U_1 + U_2$ | $U = U_1 = U_2$ |
| **Điện trở tương đương ($R_{tđ}$)**| $R_{tđ} = R_1 + R_2$ | $\dfrac{1}{R_{tđ}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} \implies R_{tđ} = \dfrac{R_1 \cdot R_2}{R_1 + R_2}$ |
| **Tỉ lệ dòng / áp** | $\dfrac{U_1}{U_2} = \dfrac{R_1}{R_2}$ (tỉ lệ thuận) | $\dfrac{I_1}{I_2} = \dfrac{R_2}{R_1}$ (tỉ lệ nghịch) |

### 3. Điện trở của dây dẫn
$$R = \rho \cdot \dfrac{l}{S}$$
- $\rho$: Điện trở suất của chất liệu làm dây dẫn ($\Omega \cdot \text{m}$).
- $l$: Chiều dài dây dẫn ($\text{m}$).
- $S$: Tiết diện dây dẫn ($\text{m}^2$). Với dây tiết diện tròn: $S = \pi \cdot r^2 = \pi \cdot \dfrac{d^2}{4}$.

### 4. Công suất điện & Điện năng tiêu thụ
- **Công suất điện:** $P = U \cdot I = I^2 \cdot R = \dfrac{U^2}{R}$ *(Đơn vị: Oát - W)*.
- **Công của dòng điện (Điện năng tiêu thụ):**
  $$A = P \cdot t = U \cdot I \cdot t = I^2 \cdot R \cdot t$$
  *(Đơn vị: Jun - $\text{J}$; hoặc kilôoát giờ - $\text{kW}\cdot\text{h}$, với $1 \text{ kW}\cdot\text{h} = 3\,600\,000 \text{ J}$)*.
- **Định luật Joule - Lenz (Nhiệt lượng tỏa ra trên dây dẫn):**
  $$Q = I^2 \cdot R \cdot t$$

---

## IV. CẢM ỨNG ĐIỆN TỪ & MÁY BIẾN ÁP

### 1. Hiện tượng cảm ứng điện từ
- Dòng điện cảm ứng xuất hiện trong cuộn dây dẫn kín khi **số đường sức từ xuyên qua tiết diện $S$ của cuộn dây dẫn đó biến thiên** (tăng lên hoặc giảm đi).

### 2. Máy biến áp (Máy biến thế)
- Cấu tạo: Gồm cuộn sơ cấp ($N_1$ vòng) nối với nguồn điện và cuộn thứ cấp ($N_2$ vòng) lấy điện ra.
- **Công thức máy biến áp:**
  $$\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$$
  - Nếu $N_2 > N_1 \implies U_2 > U_1$: **Máy tăng áp**.
  - Nếu $N_2 < N_1 \implies U_2 < U_1$: **Máy hạ áp**.

### 3. Công suất hao phí do tỏa nhiệt trên đường dây truyền tải điện
$$P_{hp} = \dfrac{R \cdot P^2}{U^2}$$
- $P$: Công suất điện cần truyền tải ($\text{W}$).
- $U$: Hiệu điện thế ở hai đầu đường dây truyền tải ($\text{V}$).
- $R$: Điện trở tổng cộng của đường dây tải điện ($\Omega$).

::: tip KẾT LUẬN QUAN TRỌNG ĐỀ THI:
Để giảm hao phí trên đường dây tải điện, biện pháp hiệu quả và kinh tế nhất là **tăng hiệu điện thế $U$** đặt vào hai đầu đường dây truyền tải (dùng máy tăng áp). Vì $P_{hp}$ tỉ lệ nghịch với $U^2$, nên khi **$U$ tăng lên $n$ lần thì công suất hao phí giảm đi $n^2$ lần**.
:::
"""

with open(os.path.join(SCIENCE_DIR, "01_vat_li_9_cong_thuc_va_ly_thuyet.md"), "w", encoding="utf-8") as f:
    f.write(vat_li_content)
print("Created science/01_vat_li_9_cong_thuc_va_ly_thuyet.md")

# 3. 02_hoa_hoc_9_ly_thuyet_va_phuong_trinh.md
hoa_hoc_content = r"""---
title: "Sổ Tay Lý Thuyết & Phương Trình Hóa Học 9 (KHTN 9 - Kết Nối Tri Thức)"
category: "Khoa Học Tự Nhiên 9"
description: "Tổng hợp toàn bộ công thức tính toán mol chuẩn mới (24.79L), dãy hoạt động hóa học của kim loại, tính chất phi kim, hợp chất hữu cơ (metan, etilen, axetilen, rượu etylic, axit axetic, chất béo) SGK KHTN 9 Kết nối tri thức."
---

# 🧪 Sổ Tay Lý Thuyết & Phương Trình Hóa Học 9 (Kết Nối Tri Thức)

::: info Định hướng ôn tập phân môn Hóa học lớp 9
Phân môn Hóa học trong KHTN 9 Kết nối tri thức tập trung vào 3 khối kiến thức:
1. **Các công thức tính toán hóa học:** Áp dụng điều kiện chuẩn mới theo quy chuẩn IUPAC/GDPT 2018 ($V = n \times 24.79$).
2. **Hóa học vô cơ:** Dãy hoạt động hóa học của kim loại, tính chất hóa học của kim loại, phi kim, bảng tuần hoàn các nguyên tố hóa học.
3. **Hóa học hữu cơ:** Hiđrocacbon (*Metan, Etilen, Axetilen*), Dẫn xuất hiđrocacbon (*Rượu etylic, Axit axetic, Phản ứng este hóa, Chất béo, Cacbohidrat và Polime*).
:::

---

## I. CÁC CÔNG THỨC TÍNH TOÁN HÓA HỌC CỐT LÕI

| Đại lượng | Công thức tính | Chú thích & Đơn vị chuẩn |
| :--- | :--- | :--- |
| **Số mol theo khối lượng** | $n = \dfrac{m}{M}$ | $m$: khối lượng chất (g), $M$: khối lượng mol (g/mol) |
| **Số mol chất khí (ĐKC mới)**| $n = \dfrac{V}{24.79} \implies V = n \times 24.79$ | $V$: thể tích khí (lít) ở $25^\circ\text{C}, 1 \text{ bar}$ *(GDPT 2018)* |
| **Nồng độ phần trăm** | $C\% = \dfrac{m_{ct}}{m_{dd}} \cdot 100\%$ | $m_{ct}$: khối lượng chất tan (g)<br>$m_{dd} = m_{ct} + m_{dm} = D \times V_{dd}$ |
| **Nồng độ mol** | $C_M = \dfrac{n}{V_{dd}}$ | $n$: số mol (mol), $V_{dd}$: thể tích dung dịch (lít) |
| **Độ rượu** | $Đ_r = \dfrac{V_{\text{rượu nguyên chất}}}{V_{\text{hỗn hợp rượu + nước}}} \cdot 100^\circ$ | $V_{\text{rượu}} = \dfrac{m_{\text{rượu}}}{D_{\text{rượu}}}$ (với $D \approx 0.8 \text{ g/ml}$) |
| **Hiệu suất phản ứng ($H$)** | $H = \dfrac{m_{\text{thực tế}}}{m_{\text{lý thuyết}}} \cdot 100\%$ | Dùng tính lượng sản phẩm hoặc chất phản ứng |

---

## II. DÃY HOẠT ĐỘNG HÓA HỌC CỦA KIM LOẠI

$$\mathbf{K > Na > Ca > Mg > Al > Zn > Fe > Ni > Sn > Pb > (H) > Cu > Hg > Ag > Pt > Au}$$

> 💡 **Thần chú ghi nhớ:**  
> **K**hi (**K**) **N**ào (**Na**) **C**ần (**Ca**) **M**ay (**Mg**) **Á**o (**Al**) **G**iáp (**Zn**) **S**ắt (**Fe**) **N**ên (**Ni**) **S**ang (**Sn**) **P**hố (**Pb**) **H**ỏi (**H**) **C**ửa (**Cu**) **H**àng (**Hg**) **Á** (**Ag**) **P**hi (**Pt**) **Â**u (**Au**).

### Ý nghĩa của Dãy hoạt động hóa học:
1. **Mức độ hoạt động giảm dần** từ trái qua phải.
2. **Kim loại đứng trước Mg (K, Na, Ca, Ba):** Tác dụng mãnh liệt với nước ở nhiệt độ thường tạo thành dung dịch kiềm (bazo) và giải phóng khí $H_2$:
   $$2\text{Na} + 2\text{H}_2\text{O} \longrightarrow 2\text{NaOH} + \text{H}_2\uparrow$$
3. **Kim loại đứng trước H:** Tác dụng với dung dịch axit loãng ($HCl, H_2SO_4$ loãng) giải phóng khí $H_2$:
   $$\text{Fe} + 2\text{HCl} \longrightarrow \text{FeCl}_2 + \text{H}_2\uparrow$$
4. **Kim loại đứng trước đẩy kim loại đứng sau** ra khỏi dung dịch muối (trừ K, Na, Ca, Ba):
   $$\text{Fe} + \text{CuSO}_4 \longrightarrow \text{FeSO}_4 + \text{Cu}\downarrow$$

---

## III. HỢP CHẤT HỮU CƠ: HIĐROCACBON

| Chất | Công thức phân tử & Cấu tạo | Đặc điểm liên kết | Phản ứng đặc trưng & Phương trình hóa học |
| :--- | :--- | :--- | :--- |
| **Metan** | $\text{CH}_4$<br>$\text{H}-\text{C}(\text{H}_2)-\text{H}$ | Chỉ có **liên kết đơn** bền vững | **Phản ứng thế** với Clo khi có ánh sáng:<br>$\text{CH}_4 + \text{Cl}_2 \xrightarrow{as} \text{CH}_3\text{Cl} + \text{HCl}$ |
| **Etilen** | $\text{C}_2\text{H}_4$<br>$\text{CH}_2 = \text{CH}_2$ | Có **1 liên kết đôi** (chứa 1 liên kết $\pi$ kém bền) | **Phản ứng cộng** làm mất màu dung dịch Brom:<br>$\text{CH}_2=\text{CH}_2 + \text{Br}_2 \longrightarrow \text{CH}_2\text{Br}-\text{CH}_2\text{Br}$<br>*(Đibrômetan - không màu)* |
| **Axetilen**| $\text{C}_2\text{H}_2$<br>$\text{CH} \equiv \text{CH}$ | Có **1 liên kết ba** (chứa 2 liên kết kém bền) | **Phản ứng cộng Brom theo 2 giai đoạn**:<br>$\text{CH}\equiv\text{CH} + 2\text{Br}_2 \longrightarrow \text{CHBr}_2-\text{CHBr}_2$ |

> 💡 **Phản ứng cháy của Hiđrocacbon:**
> Mọi hiđrocacbon khi cháy hoàn toàn trong khí oxi đều sinh ra khí cacbonic ($\text{CO}_2$) và hơi nước ($\text{H}_2\text{O}$), tỏa nhiều nhiệt:
> $$\text{CH}_4 + 2\text{O}_2 \xrightarrow{t^\circ} \text{CO}_2 + 2\text{H}_2\text{O}$$

---

## IV. DẪN XUẤT CỦA HIĐROCACBON

### 1. Rượu Etylic (Ethanol: $\text{C}_2\text{H}_5\text{OH}$)
- **Đặc điểm cấu tạo:** Có nhóm hiđroxyl (**$-\text{OH}$**) liên kết với gốc etyl.
- **Tính chất hóa học:**
  - Tác dụng với kim loại kiềm ($\text{Na}, \text{K}$) giải phóng khí $H_2$:
    $$2\text{C}_2\text{H}_5\text{OH} + 2\text{Na} \longrightarrow 2\text{C}_2\text{H}_5\text{ONa} + \text{H}_2\uparrow$$
  - Phản ứng cháy:
    $$\text{C}_2\text{H}_5\text{OH} + 3\text{O}_2 \xrightarrow{t^\circ} 2\text{CO}_2 + 3\text{H}_2\text{O}$$

### 2. Axit Axetic (Ethanoic acid: $\text{CH}_3\text{COOH}$)
- **Đặc điểm cấu tạo:** Có nhóm cacboxyl (**$-\text{COOH}$**), tạo nên tính chất axit.
- **Tính chất hóa học:**
  - Làm đổi màu quỳ tím sang màu đỏ.
  - Tác dụng với kim loại trước H: $2\text{CH}_3\text{COOH} + \text{Zn} \longrightarrow (\text{CH}_3\text{COO})_2\text{Zn} + \text{H}_2\uparrow$
  - Tác dụng với oxit bazo và bazo: $\text{CH}_3\text{COOH} + \text{NaOH} \longrightarrow \text{CH}_3\text{COONa} + \text{H}_2\text{O}$
  - Tác dụng với muối cacbonat: $2\text{CH}_3\text{COOH} + \text{CaCO}_3 \longrightarrow (\text{CH}_3\text{COO})_2\text{Ca} + \text{CO}_2\uparrow + \text{H}_2\text{O}$

### 3. Phản ứng Este hóa (Trọng tâm đề thi)
Phản ứng thuận nghịch giữa rượu etylic và axit axetic với xúc tác axit sunfuric đặc đun nóng:
$$\text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH} \overset{\text{H}_2\text{SO}_4 \text{ đặc}, t^\circ}{\rightleftharpoons} \text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O}$$
*(Sản phẩm $\text{CH}_3\text{COOC}_2\text{H}_5$ là **Etyl axetat** - chất lỏng mùi thơm hoa quả, ít tan trong nước, nổi lên trên)*.

### 4. Chất béo, Cacbohidrat & Polime

| Hợp chất | Công thức tổng quát | Phản ứng hóa học đặc trưng | Ứng dụng thực tế |
| :--- | :--- | :--- | :--- |
| **Chất béo** | $(\text{RCOO})_3\text{C}_3\text{H}_5$ | **Phản ứng xà phòng hóa** (tác dụng với dung dịch kiềm khi đun nóng):<br>$(\text{RCOO})_3\text{C}_3\text{H}_5 + 3\text{NaOH} \xrightarrow{t^\circ} 3\text{RCOONa} + \text{C}_3\text{H}_5(\text{OH})_3$<br>*(xà phòng + glixerol)* | Sản xuất xà phòng, cung cấp năng lượng cho cơ thể. |
| **Glucozơ** | $\text{C}_6\text{H}_{12}\text{O}_6$ | **Phản ứng tráng bạc** (tác dụng với dung dịch $\text{AgNO}_3$ trong $\text{NH}_3$ tạo lớp bạc sáng bóng) | Tráng gương, sản xuất ruột phích, truyền dịch y tế. |
| **Tinh bột & Xenlulozơ**| $(\text{C}_6\text{H}_{10}\text{O}_5)_n$| - Tinh bột tác dụng với dung dịch Iot cho **màu xanh lam đặc trưng**.<br>- Thủy phân nhờ xúc tác axit hoặc men tạo glucozơ. | Lương thực, sản xuất cồn, giấy, sợi may mặc. |
"""

with open(os.path.join(SCIENCE_DIR, "02_hoa_hoc_9_ly_thuyet_va_phuong_trinh.md"), "w", encoding="utf-8") as f:
    f.write(hoa_hoc_content)
print("Created science/02_hoa_hoc_9_ly_thuyet_va_phuong_trinh.md")

# 4. 03_sinh_hoc_9_di_truyen_va_sinh_thai.md
sinh_hoc_content = r"""---
title: "Sổ Tay Di Truyền & Sinh Thái Học Sinh Học 9 (KHTN 9 - Kết Nối Tri Thức)"
category: "Khoa Học Tự Nhiên 9"
description: "Tổng hợp toàn bộ kiến thức phân môn Sinh học 9: Quy luật di truyền Mendel, phân bào nguyên phân và giảm phân, cơ chế phân tử ADN - ARN - Protein, đột biến và hệ sinh thái SGK KHTN 9 Kết nối tri thức."
---

# 🧬 Sổ Tay Di Truyền & Sinh Thái Học Sinh Học 9 (Kết Nối Tri Thức)

::: info Định hướng ôn tập phân môn Sinh học lớp 9
Phân môn Sinh học trong bộ sách KHTN 9 Kết nối tri thức gồm 2 mảng kiến thức lớn:
1. **Di truyền và Biến dị:** Quy luật Mendel, Nhiễm sắc thể & Các hình thức phân bào, Cơ sở phân tử của sự di truyền (ADN, ARN, mã di truyền, tổng hợp Protein) và Các dạng đột biến.
2. **Sinh vật và Môi trường:** Các nhân tố sinh thái, Quần thể sinh vật, Quần xã sinh vật, Hệ sinh thái (chuỗi và lưới thức ăn) và Ý thức bảo vệ sinh quyển.
:::

---

## I. QUY LUẬT DI TRUYỀN MENDEL

### 1. Các thuật ngữ cơ bản cần nắm vững
- **Tính trạng:** Những đặc điểm về hình thái, cấu tạo, sinh lí của cơ thể sinh vật (ví dụ: hạt vàng, thân cao).
- **Cặp tính trạng tương phản:** Hai trạng thái biểu hiện trái ngược nhau của cùng một loại tính trạng (ví dụ: hạt trơn - hạt nhăn).
- **Gen (Alen):** Nhân tố di truyền quy định tính trạng. Alen trội ký hiệu bằng chữ in hoa ($A$), alen lặn ký hiệu bằng chữ in thường ($a$).
- **Kiểu gen:** Toàn bộ các gen trong tế bào cơ thể ($AA$: đồng hợp trội, $Aa$: dị hợp, $aa$: đồng hợp lặn).
- **Kiểu hình:** Tập hợp toàn bộ các tính trạng của cơ thể được biểu hiện ra bên ngoài.

### 2. Quy luật phân li (Lai một cặp tính trạng)
Khi lai hai cơ thể bố mẹ thuần chủng khác nhau về một cặp tính trạng tương phản:
- Đời con $F_1$ đồng tính biểu hiện tính trạng của một bên (tính trạng trội).
- Đời con $F_2$ phân li tính trạng theo tỉ lệ trung bình: **3 Trội : 1 Lặn** (Về kiểu gen: $1 AA : 2 Aa : 1 aa$).

$$\mathbf{P: \quad AA \text{ (hạt vàng)} \times aa \text{ (hạt xanh)} \implies F_1: 100\% Aa \text{ (hạt vàng)}}$$
$$\mathbf{F_1 \times F_1: \quad Aa \times Aa \implies F_2: 1 AA : 2 Aa : 1 aa \quad (3 \text{ vàng} : 1 \text{ xanh})}$$

### 3. Phép lai phân tích
- Là phép lai giữa cá thể mang tính trạng trội cần xác định kiểu gen với cá thể mang tính trạng lặn:
  - Nếu đời con **đồng tính** $\implies$ Cá thể mang tính trạng trội có kiểu gen **đồng hợp ($AA$)**.
  - Nếu đời con **phân tính theo tỉ lệ $1 : 1$** $\implies$ Cá thể mang tính trạng trội có kiểu gen **dị hợp ($Aa$)**.

---

## II. NHIỄM SẮC THỂ & CÁC CƠ CHẾ PHÂN BÀO

```mermaid
flowchart TD
    A["CƠ CHẾ DI TRUYỀN CẤP ĐỘ TẾ BÀO"] --> B["Nguyên Phân (Mitosis)<br/>- Diễn ra ở tế bào sinh dưỡng & sinh dục sơ khai<br/>- 1 tế bào mẹ (2n) -> 2 tế bào con (2n)<br/>- Giữ nguyên bộ NST"]
    A --> C["Giảm Phân (Meiosis)<br/>- Diễn ra ở tế bào sinh dục thời kỳ chín<br/>- 1 tế bào mẹ (2n) -> 4 giao tử (n)<br/>- Giảm một nửa bộ NST"]
    A --> D["Thụ Tinh (Fertilization)<br/>- Kết hợp giao tử đực (n) và giao tử cái (n)<br/>- Khôi phục bộ NST lưỡng bội (2n)"]
```

### So sánh bản chất giữa Nguyên phân và Giảm phân

| Tiêu chí | Nguyên phân | Giảm phân |
| :--- | :--- | :--- |
| **Loại tế bào diễn ra** | Tế bào sinh dưỡng và tế bào sinh dục sơ khai | Tế bào sinh dục chín (tạo tinh trùng, trứng) |
| **Số lần phân bào** | 1 lần phân bào duy nhất | 2 lần phân bào liên tiếp |
| **Kỳ đầu** | Không có sự tiếp hợp và trao đổi chéo giữa các NST | Có thể xảy ra tiếp hợp và trao đổi chéo ở kỳ đầu I |
| **Kết quả tạo thành** | **Từ 1 tế bào mẹ ($2n$) tạo ra 2 tế bào con có bộ NST giống hệt mẹ ($2n$)** | **Từ 1 tế bào mẹ ($2n$) tạo ra 4 tế bào con có bộ NST giảm đi một nửa ($n$)** |
| **Ý nghĩa sinh học** | Giúp cơ thể lớn lên, thay thế tế bào già; duy trì ổn định bộ NST qua các thế hệ tế bào. | Tạo ra các giao tử mang bộ NST đơn bội ($n$); kết hợp với thụ tinh tạo nhiều biến dị tổ hợp. |

---

## III. CƠ SỞ PHÂN TỬ CỦA DI TRUYỀN: ADN - ARN - PROTEIN

### 1. Cấu trúc và chức năng của ADN (Axit đêôxiribônuclêic)
- Cấu tạo theo **nguyên tắc đa phân**, đơn phân là 4 loại nuclêôtit: **A (Ađênin), T (Timin), G (Guanin), X (Xitôzin)**.
- Gồm hai chuỗi pôlinuclêôtit xoắn kép ngược chiều nhau liên kết theo **nguyên tắc bổ sung (NTBS)**:
  $$\mathbf{A \text{ liên kết với } T \text{ bằng 2 liên kết hiđrô} \quad (A = T)}$$
  $$\mathbf{G \text{ liên kết với } X \text{ bằng 3 liên kết hiđrô} \quad (G \equiv X)}$$

#### Các công thức tính toán toán học ADN:
- Tổng số nuclêôtit của ADN: $N = 2A + 2G = 2T + 2X$.
- Chiều dài phân tử ADN: $L = \dfrac{N}{2} \times 3.4 \text{ Å}$ *(với $1 \text{ nm} = 10 \text{ Å}$)*.
- Khối lượng phân tử ADN: $M = N \times 300 \text{ đvC}$.
- Tổng số liên kết hiđrô: $H = 2A + 3G$.

### 2. Mối quan hệ giữa Gen và Tính trạng
$$\mathbf{\text{Gen (ADN)} \xrightarrow{\text{Phiên mã}} \text{mARN} \xrightarrow{\text{Dịch mã}} \text{Prôtêin} \longrightarrow \text{Tính trạng}}$$

- **Phiên mã:** Tổng hợp mARN dựa trên một mạch khuôn của gen theo nguyên tắc bổ sung:
  $$A_{\text{khuôn}} - U, \quad T_{\text{khuôn}} - A, \quad G_{\text{khuôn}} - X, \quad X_{\text{khuôn}} - G$$
- **Dịch mã:** Các ribôxôm dịch chuyển trên mARN, mỗi bộ ba mã sao (codon) khớp với bộ ba đối mã (anticodon) trên tARN để sắp xếp các axit amin thành chuỗi pôlipeptit hoàn chỉnh.

---

## IV. BIẾN DỊ: ĐỘT BIẾN GEN VÀ ĐỘT BIẾN NHIỄM SẮC THỂ

| Loại đột biến | Các dạng thường gặp | Nguyên nhân & Hậu quả |
| :--- | :--- | :--- |
| **Đột biến gen** | - Mất một cặp nuclêôtit<br>- Thêm một cặp nuclêôtit<br>- Thay thế một cặp nuclêôtit | Do tác nhân vật lí, hóa học môi trường làm sai hỏng sao chép ADN; có thể gây hại, trung tính hoặc tạo nguồn nguyên liệu cho chọn giống. |
| **Đột biến cấu trúc NST**| - Mất đoạn<br>- Lặp đoạn<br>- Đảo đoạn<br>- Chuyển đoạn | Làm thay đổi trật tự hoặc số lượng gen trên NST; thường gây chết hoặc giảm sức sống của sinh vật (ví dụ: mất đoạn đầu NST 21 gây bệnh ung thư máu). |
| **Đột biến số lượng NST**| - Thể dị bội ($2n+1, 2n-1$)<br>- Thể đa bội ($3n, 4n$)| Rối loạn phân li NST trong phân bào.<br>*Ví dụ dị bội:* Thừa 1 NST số 21 ($2n+1=47$) gây **Hội chứng Đao (Down)**. |

---

## V. SINH THÁI HỌC & BẢO VỆ MÔI TRƯỜNG

### 1. Chuỗi thức ăn và Lưới thức ăn
- **Chuỗi thức ăn:** Là một dãy gồm nhiều loài sinh vật có quan hệ dinh dưỡng với nhau, mỗi loài là một mắt xích tiêu thụ mắt xích phía trước và bị mắt xích phía sau tiêu thụ.
  - *Ví dụ:* $\text{Cỏ} \longrightarrow \text{Châu chấu} \longrightarrow \text{Ếch} \longrightarrow \text{Rắn} \longrightarrow \text{Đại bàng}$.
- **Lưới thức ăn:** Tập hợp các chuỗi thức ăn có các mắt xích chung trong một hệ sinh thái.
- **Thành phần của một hệ sinh thái hoàn chỉnh:**
  1. Thành phần vô sinh (đất, nước, ánh sáng, nhiệt độ).
  2. Sinh vật sản xuất (thực vật quang hợp, tảo).
  3. Sinh vật tiêu thụ (động vật ăn thực vật, động vật ăn thịt).
  4. Sinh vật phân giải (vi khuẩn, nấm, giun đất).
"""

with open(os.path.join(SCIENCE_DIR, "03_sinh_hoc_9_di_truyen_va_sinh_thai.md"), "w", encoding="utf-8") as f:
    f.write(sinh_hoc_content)
print("Created science/03_sinh_hoc_9_di_truyen_va_sinh_thai.md")

