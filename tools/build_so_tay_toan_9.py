import os

file_path = r"f:\OnThiC3\EnglishDocs\docs\math\so_tay_cong_thuc_toan_9.md"

content = r"""---
title: "Sổ Tay Toàn Bộ Công Thức Toán 9 (Tập 1 & Tập 2 - Kết Nối Tri Thức)"
category: "Chuyên Đề Toán 9 Vào 10"
description: "Tổng hợp toàn bộ công thức Đại số, Căn thức, Hệ phương trình, Hàm số, Viète, Thống kê, Xác suất, Lượng giác, Đường tròn và Hình học không gian SGK Toán 9 Kết nối tri thức ôn thi vào lớp 10."
---

# 📐 Sổ Tay Toàn Bộ Công Thức Toán 9 (Tập 1 & 2 - Kết Nối Tri Thức)

::: info Hướng dẫn sử dụng sổ tay công thức
Tài liệu này hệ thống hóa **toàn bộ 100% công thức, định lý và điều kiện áp dụng** của chương trình Toán 9 mới (Bộ sách *Kết nối tri thức với cuộc sống*). Được thiết kế khoa học, súc tích, chuẩn ký hiệu toán học $KaTeX$, giúp học sinh tra cứu nhanh, ghi nhớ bản chất và không bị trừ điểm lỗi trình bày trong kỳ thi tuyển sinh vào lớp 10.
:::

---

## 📑 MỤC LỤC TRA CỨU NHANH THEO CỤM KIẾN THỨC

- [I. Căn Bậc Hai & Căn Bậc Ba](#i-can-bac-hai-can-bac-ba)
- [II. Phương Trình & Hệ Phương Trình Bậc Nhất Hai Ẩn](#ii-phuong-trinh-he-phuong-trinh-bac-nhat-hai-an)
- [III. Bất Đẳng Thức & Bất Phương Trình](#iii-bat-dang-thuc-bat-phuong-trinh)
- [IV. Hàm Số $y = ax^2$ & Phương Trình Bậc Hai - Định Lý Viète](#iv-ham-so-y-ax2-phuong-trinh-bac-hai-dinh-ly-viete)
- [V. Thống Kê & Xác Suất](#v-thong-ke-xac-suat)
- [VI. Hệ Thức Lượng & Tỉ Số Lượng Giác Trong Tam Giác Vuông](#vi-he-thuc-luong-ti-so-luong-giac-trong-tam-giac-vuong)
- [VII. Đường Tròn, Cung & Tứ Giác Nội Tiếp](#vii-duong-tron-cung-tu-giac-noi-tiep)
- [VIII. Hình Học Không Gian (Hình Trụ, Nón, Cầu)](#viii-hinh-hoc-khong-gian-hinh-tru-non-cau)

---

## I. CĂN BẬC HAI & CĂN BẬC BA

### 1. Điều kiện xác định & Hằng đẳng thức căn thức
- **Điều kiện xác định:** Căn thức bậc hai $\sqrt{A}$ có nghĩa $\Longleftrightarrow A \ge 0$.
- **Hằng đẳng thức cốt lõi:** 
  $$\sqrt{A^2} = |A| = \begin{cases} A & \text{khi } A \ge 0 \\ -A & \text{khi } A < 0 \end{cases}$$

### 2. Các phép biến đổi căn thức bậc hai

| Phép biến đổi | Công thức tổng quát | Điều kiện |
| :--- | :--- | :--- |
| **Khai phương một tích** | $\sqrt{A \cdot B} = \sqrt{A} \cdot \sqrt{B}$ | $A \ge 0, B \ge 0$ |
| **Khai phương một thương**| $\sqrt{\dfrac{A}{B}} = \dfrac{\sqrt{A}}{\sqrt{B}}$ | $A \ge 0, B > 0$ |
| **Đưa thừa số ra ngoài căn**| $\sqrt{A^2 B} = |A|\sqrt{B}$ | $B \ge 0$ |
| **Đưa thừa số vào trong căn**| $A\sqrt{B} = \sqrt{A^2 B}$ (với $A \ge 0$)<br>$A\sqrt{B} = -\sqrt{A^2 B}$ (với $A < 0$)| $B \ge 0$ |
| **Khử mẫu của biểu thức lấy căn**| $\sqrt{\dfrac{A}{B}} = \dfrac{\sqrt{A \cdot B}}{|B|}$ | $A \cdot B \ge 0, B \neq 0$ |
| **Trục căn thức ở mẫu (Dạng 1)**| $\dfrac{A}{\sqrt{B}} = \dfrac{A\sqrt{B}}{B}$ | $B > 0$ |
| **Trục căn thức ở mẫu (Nhân liên hợp)**| $\dfrac{C}{\sqrt{A} \pm \sqrt{B}} = \dfrac{C(\sqrt{A} \mp \sqrt{B})}{A - B}$ | $A \ge 0, B \ge 0, A \neq B$ |

### 3. Căn bậc ba
- Căn bậc ba của số thực $a$ là số $x$ sao cho $x^3 = a$, ký hiệu là $\sqrt[3]{a}$.
- Mọi số thực đều có duy nhất một căn bậc ba (không cần điều kiện $a \ge 0$).
- Tính chất: $\sqrt[3]{A^3} = A$; $\sqrt[3]{A \cdot B} = \sqrt[3]{A} \cdot \sqrt[3]{B}$; $\sqrt[3]{\dfrac{A}{B}} = \dfrac{\sqrt[3]{A}}{\sqrt[3]{B}}$ ($B \neq 0$).

---

## II. PHƯƠNG TRÌNH & HỆ PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN

### 1. Hệ hai phương trình bậc nhất hai ẩn
Dạng tổng quát:
$$\begin{cases} a_1 x + b_1 y = c_1 \quad (1) \\ a_2 x + b_2 y = c_2 \quad (2) \end{cases}$$

### 2. Hai phương pháp giải cơ bản
1. **Phương pháp thế:** Rút một ẩn từ một phương trình rồi thế vào phương trình còn lại để được phương trình bậc nhất một ẩn.
2. **Phương pháp cộng đại số:** Nhân hai vế của các phương trình với hệ số thích hợp để hệ số của một ẩn bằng nhau hoặc đối nhau, rồi cộng hoặc trừ từng vế.

### 3. Điều kiện số nghiệm của hệ phương trình (khi $a_2, b_2, c_2 \neq 0$)
- Hệ có **nghiệm duy nhất** $\Longleftrightarrow \dfrac{a_1}{a_2} \neq \dfrac{b_1}{b_2}$ (hai đường thẳng cắt nhau).
- Hệ **vô nghiệm** $\Longleftrightarrow \dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} \neq \dfrac{c_1}{c_2}$ (hai đường thẳng song song).
- Hệ có **vô số nghiệm** $\Longleftrightarrow \dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} = \dfrac{c_1}{c_2}$ (hai đường thẳng trùng nhau).

---

## III. BẤT ĐẲNG THỨC & BẤT PHƯƠNG TRÌNH

### 1. Tính chất cơ bản của bất đẳng thức
- Liên hệ giữa thứ tự và phép cộng: $a < b \Longleftrightarrow a + c < b + c$.
- Liên hệ giữa thứ tự và phép nhân:
  - Với $c > 0$: $a < b \Longleftrightarrow ac < bc$ (cùng chiều).
  - Với $c < 0$: $a < b \Longleftrightarrow ac > bc$ (**đổi chiều bất đẳng thức**).

### 2. Hai bất đẳng thức kinh điển thường dùng cho câu điểm 9, 10

#### a. Bất đẳng thức Cauchy (AM - GM) cho hai số không âm:
$$\dfrac{a + b}{2} \ge \sqrt{ab} \quad \text{hay} \quad a + b \ge 2\sqrt{ab} \quad (a \ge 0, b \ge 0)$$
- **Dấu "=" xảy ra** $\Longleftrightarrow a = b$.
- **Hệ quả thông dụng:**
  - $ab \le \left(\dfrac{a + b}{2}\right)^2 \le \dfrac{a^2 + b^2}{2}$
  - $\dfrac{1}{a} + \dfrac{1}{b} \ge \dfrac{4}{a + b}$ (với $a, b > 0$)

#### b. Bất đẳng thức Bunhiacopxki (Cauchy - Schwarz) cho 2 cặp số:
$$(a_1 b_1 + a_2 b_2)^2 \le (a_1^2 + a_2^2)(b_1^2 + b_2^2)$$
- **Dấu "=" xảy ra** $\Longleftrightarrow \dfrac{a_1}{b_1} = \dfrac{a_2}{b_2}$ (quy ước mẫu bằng 0 thì tử tương ứng bằng 0).

---

## IV. HÀM SỐ $y = ax^2$ & PHƯƠNG TRÌNH BẬC HAI - ĐỊNH LÝ VIÈTE

### 1. Tính chất hàm số $y = ax^2$ ($a \neq 0$)
- Đồ thị là một đường Parabol $(P)$ đi qua gốc tọa độ $O(0; 0)$, nhận trục $Oy$ làm trục đối xứng.
- Nếu $a > 0$: Đồ thị quay bề lõm lên trên, $O(0;0)$ là điểm thấp nhất; hàm số nghịch biến khi $x < 0$, đồng biến khi $x > 0$.
- Nếu $a < 0$: Đồ thị quay bề lõm xuống dưới, $O(0;0)$ là điểm cao nhất; hàm số đồng biến khi $x < 0$, nghịch biến khi $x > 0$.

### 2. Công thức nghiệm của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \neq 0$)

| Đại lượng | Công thức chuẩn $(\Delta)$ | Công thức nghiệm thu gọn $(\Delta')$ khi $b = 2b'$ |
| :--- | :--- | :--- |
| **Biệt thức** | $\Delta = b^2 - 4ac$ | $\Delta' = (b')^2 - ac$ |
| **Khi $\Delta > 0$** | PT có 2 nghiệm phân biệt:<br>$x_{1,2} = \dfrac{-b \pm \sqrt{\Delta}}{2a}$ | PT có 2 nghiệm phân biệt:<br>$x_{1,2} = \dfrac{-b' \pm \sqrt{\Delta'}}{a}$ |
| **Khi $\Delta = 0$** | PT có nghiệm kép: $x_1 = x_2 = -\dfrac{b}{2a}$ | PT có nghiệm kép: $x_1 = x_2 = -\dfrac{b'}{a}$ |
| **Khi $\Delta < 0$** | PT vô nghiệm trong tập số thực $\mathbb{R}$ | PT vô nghiệm |

> 💡 **Trường hợp nhẩm nghiệm nhanh:**
> - Nếu $a + b + c = 0 \implies x_1 = 1, \quad x_2 = \dfrac{c}{a}$.
> - Nếu $a - b + c = 0 \implies x_1 = -1, \quad x_2 = -\dfrac{c}{a}$.

### 3. Định lý Viète và các hệ thức thường gặp
Nếu phương trình $ax^2 + bx + c = 0$ ($a \neq 0$) có hai nghiệm $x_1, x_2$ ($\Delta \ge 0$), thì:
$$\begin{cases} S = x_1 + x_2 = -\dfrac{b}{a} \\ P = x_1 \cdot x_2 = \dfrac{c}{a} \end{cases}$$

#### Bảng hệ thức đối xứng biến đổi theo $S$ và $P$:
1. $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = \mathbf{S^2 - 2P}$
2. $x_1^3 + x_2^3 = (x_1 + x_2)^3 - 3x_1 x_2 (x_1 + x_2) = \mathbf{S^3 - 3SP} = \mathbf{S(S^2 - 3P)}$
3. $(x_1 - x_2)^2 = (x_1 + x_2)^2 - 4x_1 x_2 = \mathbf{S^2 - 4P} \implies |x_1 - x_2| = \sqrt{S^2 - 4P}$
4. $\dfrac{1}{x_1} + \dfrac{1}{x_2} = \dfrac{x_1 + x_2}{x_1 x_2} = \mathbf{\dfrac{S}{P}}$
5. $\dfrac{x_1}{x_2} + \dfrac{x_2}{x_1} = \dfrac{x_1^2 + x_2^2}{x_1 x_2} = \mathbf{\dfrac{S^2 - 2P}{P}}$

#### Điều kiện về dấu của hai nghiệm:
- Hai nghiệm trái dấu $\Longleftrightarrow ac < 0$ (hoặc $P < 0$).
- Hai nghiệm cùng dấu $\Longleftrightarrow \begin{cases} \Delta \ge 0 \\ P > 0 \end{cases}$
- Hai nghiệm cùng dương $\Longleftrightarrow \begin{cases} \Delta \ge 0 \\ S > 0 \\ P > 0 \end{cases}$
- Hai nghiệm cùng âm $\Longleftrightarrow \begin{cases} \Delta \ge 0 \\ S < 0 \\ P > 0 \end{cases}$

---

## V. THỐNG KÊ & XÁC SUẤT

### 1. Thống kê mô tả
- **Tần số ($m$):** Số lần xuất hiện của một giá trị trong mẫu dữ liệu.
- **Tần số tương đối ($f$):** Tỉ số giữa tần số $m$ của giá trị đó và kích thước mẫu $N$:
  $$f = \dfrac{m}{N} \cdot 100\%$$
- **Bảng tần số ghép nhóm:** Dùng khi số lượng giá trị phân tán lớn, nhóm các giá trị vào từng khoảng $[a; b)$. Giá trị đại diện của nhóm là $c = \dfrac{a + b}{2}$.

### 2. Xác suất cổ điển của biến cố
- **Không gian mẫu ($\Omega$):** Tập hợp tất cả các kết quả có thể xảy ra của một phép thử ngẫu nhiên.
- **Công thức xác suất của biến cố $E$:**
  $$P(E) = \dfrac{n(E)}{n(\Omega)} = \dfrac{\text{Số kết quả thuận lợi cho } E}{\text{Tổng số kết quả đồng khả năng trong } \Omega}$$
- Tính chất: $0 \le P(E) \le 1$. Nếu $E$ là biến cố chắc chắn thì $P(E) = 1$; nếu $E$ là biến cố không thể thì $P(E) = 0$.

---

## VI. HỆ THỨC LƯỢNG & TỈ SỐ LƯỢNG GIÁC TRONG TAM GIÁC VUÔNG

Cho $\triangle ABC$ vuông tại $A$, đường cao $AH$. Đặt $BC = a, AC = b, AB = c, AH = h, BH = c', CH = b'$.

```mermaid
flowchart TD
    A["Tam giác ABC vuông tại A, đường cao AH"] --> B["Hệ thức cạnh và đường cao"]
    A --> C["Tỉ số lượng giác góc nhọn"]
    
    B --> B1["b² = a · b',  c² = a · c'"]
    B --> B2["h² = b' · c'"]
    B --> B3["a · h = b · c"]
    B --> B4["1/h² = 1/b² + 1/c²"]
    
    C --> C1["sin = Đối / Huyền"]
    C --> C2["cos = Kề / Huyền"]
    C --> C3["tan = Đối / Kề"]
    C --> C4["cot = Kề / Đối"]
```

### 1. Hệ thức về cạnh và đường cao
1. $b^2 = a \cdot b' \quad \text{và} \quad c^2 = a \cdot c'$ (Bình phương cạnh góc vuông bằng tích cạnh huyền và hình chiếu)
2. $h^2 = b' \cdot c'$ (Bình phương đường cao bằng tích hai hình chiếu)
3. $a \cdot h = b \cdot c$ (Tích cạnh huyền và đường cao bằng tích hai cạnh góc vuông)
4. $\dfrac{1}{h^2} = \dfrac{1}{b^2} + \dfrac{1}{c^2}$ (Nghịch đảo bình phương đường cao)
5. $a^2 = b^2 + c^2$ (Định lý Pythagore)

### 2. Tỉ số lượng giác của góc nhọn $\alpha$
$$\sin \alpha = \dfrac{\text{Cạnh đối}}{\text{Cạnh huyền}}, \quad \cos \alpha = \dfrac{\text{Cạnh kề}}{\text{Cạnh huyền}}, \quad \tan \alpha = \dfrac{\text{Cạnh đối}}{\text{Cạnh kề}}, \quad \cot \alpha = \dfrac{\text{Cạnh kề}}{\text{Cạnh đối}}$$

- **Hệ thức lượng giác cơ bản:**
  - $\sin^2 \alpha + \cos^2 \alpha = 1$
  - $\tan \alpha = \dfrac{\sin \alpha}{\cos \alpha}, \quad \cot \alpha = \dfrac{\cos \alpha}{\sin \alpha}$
  - $\tan \alpha \cdot \cot \alpha = 1$
  - $1 + \tan^2 \alpha = \dfrac{1}{\cos^2 \alpha}, \quad 1 + \cot^2 \alpha = \dfrac{1}{\sin^2 \alpha}$
- **Hai góc phụ nhau ($\alpha + \beta = 90^\circ$):**
  - $\sin \alpha = \cos \beta$
  - $\cos \alpha = \sin \beta$
  - $\tan \alpha = \cot \beta$
  - $\cot \alpha = \tan \beta$

---

## VII. ĐƯỜNG TRÒN, CUNG & TỨ GIÁC NỘI TIẾP

### 1. Góc và cung trong đường tròn
- **Góc ở tâm:** Số đo góc ở tâm bằng số đo của cung bị chắn: $\widehat{AOB} = \text{sđ}\overparen{AB}$.
- **Góc nội tiếp:** Số đo góc nội tiếp bằng nửa số đo của cung bị chắn: $\widehat{ACB} = \dfrac{1}{2}\text{sđ}\overparen{AB}$.
  - Góc nội tiếp chắn nửa đường tròn là góc vuông ($90^\circ$).
  - Trong một đường tròn, các góc nội tiếp cùng chắn một cung hoặc chắn các cung bằng nhau thì bằng nhau.
- **Độ dài cung tròn & Diện tích hình quạt:**
  - Độ dài đường tròn: $C = 2\pi R = \pi d$.
  - Độ dài cung tròn $n^\circ$: $l = \dfrac{\pi R n}{180}$.
  - Diện tích hình tròn: $S = \pi R^2$.
  - Diện tích hình quạt tròn bán kính $R$, cung $n^\circ$: $S_q = \dfrac{\pi R^2 n}{360} = \dfrac{l \cdot R}{2}$.
  - Diện tích hình vành khuyên (giữa 2 đường tròn đồng tâm bán kính $R_2 > R_1$): $S_{vk} = \pi(R_2^2 - R_1^2)$.

### 2. Dấu hiệu nhận biết Tứ giác nội tiếp (Ăn trọn 1.0 - 1.5 điểm hình học)

Tứ giác $ABCD$ nội tiếp một đường tròn khi thỏa mãn **một trong 4 dấu hiệu** sau:
1. **Dấu hiệu 1 (Tổng 2 góc đối):** Tứ giác có tổng hai góc đối diện bằng $180^\circ$ ($\widehat{A} + \widehat{C} = 180^\circ$ hoặc $\widehat{B} + \widehat{D} = 180^\circ$).
2. **Dấu hiệu 2 (Góc ngoài tại một đỉnh):** Góc ngoài tại một đỉnh bằng góc trong của đỉnh đối diện.
3. **Dấu hiệu 3 (Cùng nhìn một cạnh):** Hai đỉnh kề nhau cùng nhìn cạnh chứa hai đỉnh còn lại dưới hai góc bằng nhau ($\widehat{DAC} = \widehat{DBC}$).
4. **Dấu hiệu 4 (Cách đều tâm):** Bốn đỉnh của tứ giác cùng cách đều một điểm $O$ cố định ($OA = OB = OC = OD = R$).

---

## VIII. HÌNH HỌC KHÔNG GIAN (HÌNH TRỤ, NÓN, CẦU)

| Hình học | Diện tích xung quanh $(S_{xq})$ | Diện tích toàn phần $(S_{tp})$ | Thể tích $(V)$ |
| :--- | :--- | :--- | :--- |
| **Hình trụ**<br>Bán kính đáy $R$, chiều cao $h$ | $S_{xq} = 2\pi R h$ | $S_{tp} = 2\pi R h + 2\pi R^2$ | $V = \pi R^2 h = S_{\text{đáy}} \cdot h$ |
| **Hình nón**<br>Bán kính đáy $R$, chiều cao $h$, đường sinh $l = \sqrt{h^2 + R^2}$ | $S_{xq} = \pi R l$ | $S_{tp} = \pi R l + \pi R^2$ | $V = \dfrac{1}{3}\pi R^2 h$ |
| **Hình cầu**<br>Bán kính $R$ | $S = 4\pi R^2 = \pi d^2$ | *(Mặt cầu)* | $V = \dfrac{4}{3}\pi R^3$ |

::: tip Mẹo đổi đơn vị đo lường trong bài toán thực tế:
- $1 \text{ m}^3 = 1000 \text{ dm}^3 = 1000 \text{ lít} = 1\,000\,000 \text{ cm}^3$
- $1 \text{ dm}^3 = 1 \text{ lít} = 1000 \text{ cm}^3 = 1000 \text{ ml}$
- Khi làm bài toán thực tế hình không gian, luôn quy đổi tất cả kích thước (bán kính, chiều cao, đường kính) về **cùng một đơn vị đo** trước khi thay vào công thức tính $S$ hoặc $V$.
:::
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Created so_tay_cong_thuc_toan_9.md")
