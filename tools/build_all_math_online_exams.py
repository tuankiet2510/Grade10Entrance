# -*- coding: utf-8 -*-
import os

MATH_DIR = r"f:\OnThiC3\EnglishDocs\docs\math"
os.makedirs(MATH_DIR, exist_ok=True)

# 1. de_thi_hoc_ky_1_toan_9.md
de_thi_hoc_ky_1 = r"""---
title: "Đề Kiểm Tra Cuối Học Kỳ 1 Toán 9 (Năm học 2026 - 2027)"
category: "Đề Thi Toán 9"
description: "Đề kiểm tra cuối học kỳ 1 môn Toán 9 chuẩn cấu trúc ma trận GDPT 2018 (12 câu trắc nghiệm khách quan + 5 bài toán tự luận căn thức, hàm số bậc nhất, hệ phương trình, đường tròn và cực trị) có lời giải chi tiết từng bước."
---

# 📐 Đề Kiểm Tra Cuối Học Kỳ 1 Toán 9 (Năm học 2026 - 2027)

> **Môn thi:** Toán 9 • **Thời gian làm bài:** 90 phút (không kể thời gian phát đề)  
> **Phạm vi kiến thức trọng tâm:**  
> - Căn bậc hai, căn bậc ba và các phép biến đổi biểu thức chứa căn.  
> - Hàm số bậc nhất $y = ax + b$ ($a \ne 0$) và đồ thị đường thẳng.  
> - Hệ hai phương trình bậc nhất hai ẩn và ứng dụng thực tế.  
> - Hệ thức lượng trong tam giác vuông, tỉ số lượng giác góc nhọn.  
> - Đường tròn: Quan hệ đường kính - dây cung, tiếp tuyến của đường tròn.

---

## PHẦN I: TRẮC NGHIỆM KHÁCH QUAN (3.0 ĐIỂM - 12 CÂU)

::: info HƯỚNG DẪN LÀM BÀI
Mỗi câu hỏi có 4 phương án trả lời A, B, C, D. Chọn một phương án đúng duy nhất (mỗi câu đúng được 0.25 điểm).
:::

**Câu 1:** Điều kiện xác định của biểu thức $\sqrt{\dfrac{3}{x - 2}}$ là:  
A. $x \ge 2$  
B. $x > 2$  
C. $x < 2$  
D. $x \ne 2$  
*Đáp án đúng:* **B**  
*Lời giải:* Biểu thức có nghĩa khi $\dfrac{3}{x - 2} > 0$ (do tử số $3 > 0$ nên mẫu số phải dương và khác $0$) $\iff x - 2 > 0 \iff x > 2$.

---

**Câu 2:** Rút gọn biểu thức $A = \sqrt{12} - \sqrt{27} + \sqrt{48}$ ta được kết quả:  
A. $3\sqrt{3}$  
B. $2\sqrt{3}$  
C. $5\sqrt{3}$  
D. $\sqrt{3}$  
*Đáp án đúng:* **A**  
*Lời giải:* $A = \sqrt{4 \cdot 3} - \sqrt{9 \cdot 3} + \sqrt{16 \cdot 3} = 2\sqrt{3} - 3\sqrt{3} + 4\sqrt{3} = (2 - 3 + 4)\sqrt{3} = 3\sqrt{3}$.

---

**Câu 3:** Hàm số nào sau đây là hàm số bậc nhất đồng biến trên $\mathbb{R}$?  
A. $y = -2x + 5$  
B. $y = (1 - \sqrt{2})x - 3$  
C. $y = (\sqrt{3} - 1)x + 2$  
D. $y = 0x + 4$  
*Đáp án đúng:* **C**  
*Lời giải:* Hàm số bậc nhất $y = ax + b$ đồng biến trên $\mathbb{R}$ khi hệ số $a > 0$. Ta có $\sqrt{3} \approx 1{,}732 > 1 \implies a = \sqrt{3} - 1 > 0$.

---

**Câu 4:** Điểm nào sau đây thuộc đồ thị hàm số $y = 2x - 3$?  
A. $M(1; -1)$  
B. $N(2; 3)$  
C. $P(0; 3)$  
D. $Q(-1; 1)$  
*Đáp án đúng:* **A**  
*Lời giải:* Thay $x = 1$ vào hàm số: $y = 2(1) - 3 = 2 - 3 = -1$. Điểm $M(1; -1)$ thỏa mãn phương trình.

---

**Câu 5:** Góc tạo bởi đường thẳng $y = \sqrt{3}x + 1$ với trục hoành $Ox$ bằng:  
A. $30^\circ$  
B. $45^\circ$  
C. $60^\circ$  
D. $120^\circ$  
*Đáp án đúng:* **C**  
*Lời giải:* Gọi góc tạo bởi đường thẳng với chiều dương trục $Ox$ là $\alpha$. Ta có $\tan \alpha = a = \sqrt{3} \implies \alpha = 60^\circ$.

---

**Câu 6:** Hệ phương trình $\begin{cases} 2x - y = 3 \\ x + 2y = 4 \end{cases}$ có nghiệm duy nhất $(x; y)$ là:  
A. $(2; 1)$  
B. $(1; 2)$  
C. $(3; 3)$  
D. $(2; -1)$  
*Đáp án đúng:* **A**  
*Lời giải:* Từ PT (1) rút $y = 2x - 3$, thế vào PT (2): $x + 2(2x - 3) = 4 \iff 5x - 6 = 4 \iff 5x = 10 \iff x = 2$. Suy ra $y = 2(2) - 3 = 1$. Nghiệm là $(2; 1)$.

---

**Câu 7:** Cho tam giác $ABC$ vuông tại $A$, có $AB = 6\text{ cm}$, $AC = 8\text{ cm}$. Chiều cao $AH$ ứng với cạnh huyền $BC$ có độ dài bằng:  
A. $4{,}8\text{ cm}$  
B. $5\text{ cm}$  
C. $2{,}4\text{ cm}$  
D. $10\text{ cm}$  
*Đáp án đúng:* **A**  
*Lời giải:* Áp dụng định lý Pythagore: $BC = \sqrt{AB^2 + AC^2} = \sqrt{6^2 + 8^2} = 10\text{ cm}$.  
Hệ thức lượng: $AH \cdot BC = AB \cdot AC \implies AH = \dfrac{AB \cdot AC}{BC} = \dfrac{6 \cdot 8}{10} = 4{,}8\text{ cm}$.

---

**Câu 8:** Với mọi góc nhọn $\alpha$, khẳng định nào sau đây là **sai**?  
A. $\sin^2 \alpha + \cos^2 \alpha = 1$  
B. $\tan \alpha = \dfrac{\sin \alpha}{\cos \alpha}$  
C. $\tan \alpha \cdot \cot \alpha = 1$  
D. $\sin \alpha = \cos(180^\circ - \alpha)$  
*Đáp án đúng:* **D**  
*Lời giải:* Với hai góc phụ nhau $\alpha + \beta = 90^\circ$ thì $\sin \alpha = \cos(90^\circ - \alpha)$. Khẳng định D sai về công thức.

---

**Câu 9:** Cho đường tròn $(O; 5\text{ cm})$ và một dây cung $AB = 8\text{ cm}$. Khoảng cách từ tâm $O$ đến dây $AB$ bằng:  
A. $3\text{ cm}$  
B. $4\text{ cm}$  
C. $2\text{ cm}$  
D. $1\text{ cm}$  
*Đáp án đúng:* **A**  
*Lời giải:* Kẻ $OH \perp AB$ tại $H \implies H$ là trung điểm của $AB \implies AH = \dfrac{AB}{2} = 4\text{ cm}$.  
Tam giác $OAH$ vuông tại $H$: $OH = \sqrt{OA^2 - AH^2} = \sqrt{5^2 - 4^2} = \sqrt{9} = 3\text{ cm}$.

---

**Câu 10:** Cho điểm $A$ nằm ngoài đường tròn $(O; R)$. Kẻ hai tiếp tuyến $AB, AC$ với đường tròn ($B, C$ là các tiếp điểm). Khẳng định nào sau đây là **đúng**?  
A. $AB = AC$ và $AO$ là tia phân giác của góc $\widehat{BAC}$  
B. $AO \perp BC$ tại trung điểm của $BC$  
C. Bốn điểm $A, B, O, C$ cùng thuộc đường tròn đường kính $OA$  
D. Cả A, B, C đều đúng  
*Đáp án đúng:* **D**  
*Lời giải:* Theo tính chất của hai tiếp tuyến cắt nhau, cả 3 mệnh đề A, B, C đều là tính chất hình học chính xác.

---

**Câu 11:** Đường thẳng $d$ và đường tròn $(O; R)$ tiếp xúc nhau khi khoảng cách $d(O; d)$ thỏa mãn:  
A. $d > R$  
B. $d = R$  
C. $d < R$  
D. $d \le R$  
*Đáp án đúng:* **B**  
*Lời giải:* Đường thẳng tiếp xúc đường tròn khi và chỉ khi khoảng cách từ tâm đến đường thẳng bằng đúng bán kính ($d = R$).

---

**Câu 12:** Căn bậc ba của $-125$ là:  
A. $5$  
B. $-5$  
C. $\pm 5$  
D. Không tồn tại  
*Đáp án đúng:* **B**  
*Lời giải:* Vì $(-5)^3 = -125$ nên $\sqrt[3]{-125} = -5$. Căn bậc ba xác định với mọi số thực âm và dương.

---

## PHẦN II: TỰ LUẬN (7.0 ĐIỂM - 5 BÀI TOÁN)

### Bài 1 (1.5 điểm): Rút gọn biểu thức chứa căn
Cho hai biểu thức:  
$$A = \dfrac{\sqrt{x} + 2}{\sqrt{x} - 3} \quad \text{và} \quad B = \dfrac{\sqrt{x}}{\sqrt{x} + 3} + \dfrac{2\sqrt{x}}{\sqrt{x} - 3} - \dfrac{3x + 9}{x - 9} \quad (\text{với } x \ge 0, x \ne 9)$$

1. Tính giá trị của biểu thức $A$ khi $x = 16$.
2. Rút gọn biểu thức $B$.
3. Đặt $P = \dfrac{B}{A}$. Tìm các giá trị của $x$ để $P < \dfrac{1}{2}$.

#### Lời giải chi tiết:
**Ý 1 (0.5 điểm):**  
Thay $x = 16$ (thỏa mãn ĐKXĐ: $x \ge 0, x \ne 9$) vào biểu thức $A$:  
$$A = \dfrac{\sqrt{16} + 2}{\sqrt{16} - 3} = \dfrac{4 + 2}{4 - 3} = \dfrac{6}{1} = 6$$

**Ý 2 (0.5 điểm):**  
Ta có $x - 9 = (\sqrt{x} - 3)(\sqrt{x} + 3)$. Mẫu thức chung là $(\sqrt{x} - 3)(\sqrt{x} + 3)$:  
$$B = \dfrac{\sqrt{x}(\sqrt{x} - 3) + 2\sqrt{x}(\sqrt{x} + 3) - (3x + 9)}{(\sqrt{x} - 3)(\sqrt{x} + 3)}$$
$$= \dfrac{x - 3\sqrt{x} + 2x + 6\sqrt{x} - 3x - 9}{(\sqrt{x} - 3)(\sqrt{x} + 3)} = \dfrac{3\sqrt{x} - 9}{(\sqrt{x} - 3)(\sqrt{x} + 3)}$$
$$= \dfrac{3(\sqrt{x} - 3)}{(\sqrt{x} - 3)(\sqrt{x} + 3)} = \dfrac{3}{\sqrt{x} + 3}$$
Vậy $B = \dfrac{3}{\sqrt{x} + 3}$.

**Ý 3 (0.5 điểm):**  
Ta có:  
$$P = \dfrac{B}{A} = \dfrac{3}{\sqrt{x} + 3} : \dfrac{\sqrt{x} + 2}{\sqrt{x} - 3} = \dfrac{3(\sqrt{x} - 3)}{(\sqrt{x} + 3)(\sqrt{x} + 2)}$$
Để $P < \dfrac{1}{2}$:  
$$P - \dfrac{1}{2} < 0 \iff \dfrac{3\sqrt{x} - 9}{(\sqrt{x} + 3)(\sqrt{x} + 2)} - \dfrac{1}{2} < 0$$
$$\iff \dfrac{2(3\sqrt{x} - 9) - (x + 5\sqrt{x} + 6)}{2(\sqrt{x} + 2)(\sqrt{x} + 3)} < 0 \iff \dfrac{-x + \sqrt{x} - 24}{2(\sqrt{x} + 2)(\sqrt{x} + 3)} < 0$$
Vì $x \ge 0$ nên mẫu số $2(\sqrt{x} + 2)(\sqrt{x} + 3) > 0$.  
Xét tử số:  
$$-x + \sqrt{x} - 24 = -\left(x - \sqrt{x} + \dfrac{1}{4}\right) - \dfrac{95}{4} = -\left(\sqrt{x} - \dfrac{1}{2}\right)^2 - \dfrac{95}{4} < 0 \quad \forall x \ge 0$$
Do đó tử số luôn âm với mọi $x \ge 0$.  
Vậy bất phương trình nghiệm đúng với mọi $x \ge 0$ thỏa mãn ĐKXĐ ($x \ge 0, x \ne 9$).

---

### Bài 2 (1.5 điểm): Hàm số bậc nhất & Đồ thị
Cho hai đường thẳng $(d_1): y = 2x - 3$ và $(d_2): y = -x + 3$.
1. Xác định tọa độ giao điểm $A$ của $(d_1)$ và $(d_2)$ bằng phép toán.
2. Tìm giá trị của tham số $m$ để đường thẳng $(d_3): y = (m - 1)x + 2m$ đồng quy với $(d_1)$ và $(d_2)$.

#### Lời giải chi tiết:
**Ý 1 (0.75 điểm):**  
Phương trình hoành độ giao điểm của $(d_1)$ và $(d_2)$:  
$$2x - 3 = -x + 3 \iff 3x = 6 \iff x = 2$$
Thay $x = 2$ vào phương trình $(d_2)$: $y = -(2) + 3 = 1$.  
Vậy tọa độ giao điểm là $A(2; 1)$.

**Ý 2 (0.75 điểm):**  
Để ba đường thẳng $(d_1), (d_2), (d_3)$ đồng quy thì $(d_3)$ phải đi qua giao điểm $A(2; 1)$:  
Thay $x = 2, y = 1$ vào phương trình $(d_3)$:  
$$1 = (m - 1) \cdot 2 + 2m \iff 1 = 2m - 2 + 2m \iff 4m = 3 \iff m = \dfrac{3}{4}$$
Với $m = \dfrac{3}{4} \implies m - 1 = -\dfrac{1}{4} \ne 2$ và $\ne -1$ (ba đường thẳng phân biệt có hệ số góc khác nhau).  
Vậy $m = \dfrac{3}{4}$.

---

### Bài 3 (1.0 điểm): Bài toán thực tế
Một người đứng tại điểm $A$ trên bờ hồ nhìn lên đỉnh một tháp phát sóng truyền hình $B$ dưới góc nâng $32^\circ$. Người đó tiến lại gần chân tháp một đoạn $40\text{ m}$ đến vị trí $C$ thì nhìn thấy đỉnh tháp dưới góc nâng $48^\circ$. Giả sử mặt đất bằng phẳng và chiều cao mắt người quan sát cách mặt đất $1{,}6\text{ m}$. Tính chiều cao của tháp phát sóng (làm tròn kết quả đến mét).

#### Lời giải chi tiết:
Gọi $H$ là điểm trên tháp ngang tầm mắt người quan sát, $B$ là đỉnh tháp. Đoạn thẳng $BH$ vuông góc với đường nhìn nằm ngang $AC$.  
Đặt khoảng cách $CH = x$ ($x > 0$, đơn vị mét). Khi đó $AH = AC + CH = 40 + x$.  
Trong tam giác vuông $BCH$ vuông tại $H$:  
$$BH = CH \cdot \tan 48^\circ = x \cdot \tan 48^\circ$$
Trong tam giác vuông $BAH$ vuông tại $H$:  
$$BH = AH \cdot \tan 32^\circ = (40 + x) \cdot \tan 32^\circ$$
Do đó ta có phương trình:  
$$x \cdot \tan 48^\circ = (40 + x) \cdot \tan 32^\circ \iff x(\tan 48^\circ - \tan 32^\circ) = 40 \cdot \tan 32^\circ$$
$$\implies x = \dfrac{40 \cdot \tan 32^\circ}{\tan 48^\circ - \tan 32^\circ} \approx \dfrac{40 \cdot 0{,}6249}{1{,}1106 - 0{,}6249} \approx \dfrac{24{,}996}{0{,}4857} \approx 51{,}46\text{ m}$$
Từ đó tính được chiều cao phần tháp phía trên tầm mắt:  
$$BH = x \cdot \tan 48^\circ \approx 51{,}46 \cdot 1{,}1106 \approx 57{,}15\text{ m}$$
Chiều cao toàn phần của ngọn tháp là:  
$$h = BH + 1{,}6 \approx 57{,}15 + 1{,}6 = 58{,}75\text{ m} \approx 59\text{ m}$$
Vậy chiều cao của ngọn tháp phát sóng xấp xỉ $59\text{ m}$.

---

### Bài 4 (2.5 điểm): Hình học đường tròn
Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn sao cho $OA = 2R$. Qua $A$ kẻ hai tiếp tuyến $AB, AC$ với đường tròn $(O)$ ($B, C$ là các tiếp điểm). Đoạn thẳng $OA$ cắt dây cung $BC$ tại $H$.
1. Chứng minh bốn điểm $A, B, O, C$ cùng thuộc một đường tròn và $OA \perp BC$ tại $H$.
2. Tính độ dài các đoạn thẳng $AB, BC$ và số đo góc $\widehat{BAC}$ theo $R$.
3. Kẻ đường kính $CD$ của đường tròn $(O)$. Chứng minh $BD \parallel OA$.

#### Lời giải chi tiết:
**Ý 1 (1.0 điểm):**  
- Do $AB, AC$ là hai tiếp tuyến của $(O)$ nên $\widehat{ABO} = 90^\circ$ và $\widehat{ACO} = 90^\circ$.  
- Tam giác $ABO$ vuông tại $B \implies B$ thuộc đường tròn đường kính $OA$. Tam giác $ACO$ vuông tại $C \implies C$ thuộc đường tròn đường kính $OA$. Do đó bốn điểm $A, B, O, C$ cùng thuộc đường tròn đường kính $OA$.  
- Ta có $AB = AC$ (tính chất hai tiếp tuyến cắt nhau) và $OB = OC = R \implies OA$ là đường trung trực của đoạn thẳng $BC$, suy ra $OA \perp BC$ tại $H$.

**Ý 2 (1.0 điểm):**  
- Trong tam giác vuông $ABO$ vuông tại $B$, có $OA = 2R, OB = R$. Theo định lý Pythagore:  
  $$AB = \sqrt{OA^2 - OB^2} = \sqrt{(2R)^2 - R^2} = R\sqrt{3}$$
- Xét tam giác vuông $ABO$: $\sin \widehat{BAO} = \dfrac{OB}{OA} = \dfrac{R}{2R} = \dfrac{1}{2} \implies \widehat{BAO} = 30^\circ$.  
  Vì $OA$ là tia phân giác của $\widehat{BAC}$ nên $\widehat{BAC} = 2\widehat{BAO} = 2 \cdot 30^\circ = 60^\circ$.  
- Áp dụng hệ thức lượng cho tam giác vuông $ABO$ với đường cao $BH$:  
  $$BH \cdot OA = AB \cdot OB \implies BH = \dfrac{AB \cdot OB}{OA} = \dfrac{R\sqrt{3} \cdot R}{2R} = \dfrac{R\sqrt{3}}{2}$$
- Vì $H$ là trung điểm của $BC$ nên:  
  $$BC = 2BH = 2 \cdot \dfrac{R\sqrt{3}}{2} = R\sqrt{3}$$

**Ý 3 (0.5 điểm):**  
- Tam giác $BCD$ nội tiếp đường tròn $(O)$ có cạnh $CD$ là đường kính nên $\triangle BCD$ vuông tại $B \implies BD \perp BC$.  
- Mặt khác, theo kết quả câu 1 ta có $OA \perp BC$.  
- Suy ra $BD \parallel OA$ (do cùng vuông góc với đoạn $BC$).

---

### Bài 5 (0.5 điểm): Bất đẳng thức phân loại điểm 10
Cho hai số thực dương $a, b$ thỏa mãn điều kiện $a + b \le 2$. Tìm giá trị nhỏ nhất của biểu thức:
$$P = \dfrac{1}{a^2 + b^2} + \dfrac{1}{2ab} + 3ab$$

#### Lời giải chi tiết:
Áp dụng bất đẳng thức cộng mẫu số Schwarz: Với $x, y > 0$ ta có $\dfrac{1}{x} + \dfrac{1}{y} \ge \dfrac{4}{x + y}$.  
Chọn $x = a^2 + b^2$ và $y = 2ab$, ta có:  
$$\dfrac{1}{a^2 + b^2} + \dfrac{1}{2ab} \ge \dfrac{4}{a^2 + b^2 + 2ab} = \dfrac{4}{(a + b)^2} \ge \dfrac{4}{2^2} = 1$$

Khảo sát hàm theo $t = ab$: Vì $a^2 + b^2 \ge 2ab$, đẳng thức xảy ra khi $a = b$.  
Khi $a = b \in (0; 1]$, ta có $P \ge \dfrac{1}{ab} + 3ab$.  
Áp dụng bất đẳng thức Cauchy cho hai số dương $\dfrac{1}{ab}$ và $3ab$:  
$$P \ge \dfrac{1}{ab} + 3ab \ge 2\sqrt{\dfrac{1}{ab} \cdot 3ab} = 2\sqrt{3}$$
Dấu đẳng thức xảy ra khi và chỉ khi:  
$$\begin{cases} a = b \\ \dfrac{1}{ab} = 3ab \implies ab = \dfrac{1}{\sqrt{3}} \\ a + b \le 2 \end{cases} \iff a = b = \dfrac{1}{\sqrt[4]{3}}$$
Khi đó $a + b = 2 \cdot 3^{-1/4} \approx 1{,}52 \le 2$ (hoàn toàn thỏa mãn).  
Vậy giá trị nhỏ nhất của $P$ là $2\sqrt{3}$.
"""

with open(os.path.join(MATH_DIR, "de_thi_hoc_ky_1_toan_9.md"), "w", encoding="utf-8") as f:
    f.write(de_thi_hoc_ky_1)
print("Created de_thi_hoc_ky_1_toan_9.md")

# 2. de_thi_giua_hoc_ky_2_toan_9.md
de_thi_giua_hk2 = r"""---
title: "Đề Kiểm Tra Giữa Học Kỳ 2 Toán 9 (Năm học 2026 - 2027)"
category: "Đề Thi Toán 9"
description: "Đề kiểm tra giữa kỳ 2 môn Toán 9 chuẩn cấu trúc ma trận GDPT 2018 (Hệ phương trình bậc nhất hai ẩn, Hàm số y = ax^2, Phương trình bậc hai một ẩn, Hệ thức Viète, Góc với đường tròn và Tứ giác nội tiếp) có lời giải chi tiết từng bước."
---

# 📐 Đề Kiểm Tra Giữa Học Kỳ 2 Toán 9 (Năm học 2026 - 2027)

> **Môn thi:** Toán 9 • **Thời gian làm bài:** 90 phút (không kể thời gian phát đề)  
> **Phạm vi kiến thức trọng tâm:**  
> - Hệ hai phương trình bậc nhất hai ẩn (phương pháp thế, cộng đại số và giải bài toán bằng cách lập hệ phương trình).  
> - Hàm số $y = ax^2$ ($a \ne 0$) và đồ thị Parabol.  
> - Phương trình bậc hai một ẩn $ax^2 + bx + c = 0$ và Hệ thức Vi-ét cùng các ứng dụng.  
> - Hình học: Góc ở tâm, số đo cung, góc nội tiếp, góc tạo bởi tia tiếp tuyến và dây cung, tứ giác nội tiếp.

---

## PHẦN I: TRẮC NGHIỆM KHÁCH QUAN (3.0 ĐIỂM - 12 CÂU)

::: info HƯỚNG DẪN LÀM BÀI
Mỗi câu hỏi có 4 phương án trả lời A, B, C, D. Chọn một phương án đúng duy nhất (mỗi câu đúng được 0.25 điểm).
:::

**Câu 1:** Cặp số nào sau đây là nghiệm của phương trình $3x - 2y = 5$?  
A. $(1; -1)$  
B. $(2; 1)$  
C. $(3; 2)$  
D. $(-1; 4)$  
*Đáp án đúng:* **A**  
*Lời giải:* Thay $x = 1, y = -1$ vào vế trái: $3(1) - 2(-1) = 3 + 2 = 5$ (thỏa mãn).

---

**Câu 2:** Hàm số $y = -2x^2$ đồng biến trên khoảng nào sau đây?  
A. $(0; +\infty)$  
B. $(-\infty; 0)$  
C. $\mathbb{R}$  
D. $(-\infty; +\infty)$  
*Đáp án đúng:* **B**  
*Lời giải:* Với hàm số $y = ax^2$ có hệ số $a = -2 < 0$, hàm số đồng biến khi $x < 0$ (khoảng $(-\infty; 0)$) và nghịch biến khi $x > 0$.

---

**Câu 3:** Điểm nào sau đây thuộc đồ thị hàm số $y = \dfrac{1}{2}x^2$?  
A. $M(-2; 2)$  
B. $N(2; 4)$  
C. $P(-1; 1)$  
D. $Q(4; 4)$  
*Đáp án đúng:* **A**  
*Lời giải:* Thay $x = -2$: $y = \dfrac{1}{2}(-2)^2 = \dfrac{1}{2} \cdot 4 = 2$. Do đó điểm $M(-2; 2)$ thuộc đồ thị.

---

**Câu 4:** Biệt thức $\Delta'$ của phương trình bậc hai $x^2 - 4x + 3 = 0$ bằng:  
A. $1$  
B. $4$  
C. $-1$  
D. $16$  
*Đáp án đúng:* **A**  
*Lời giải:* Ta có $a = 1, b' = -2, c = 3$. Biệt thức thu gọn: $\Delta' = (b')^2 - ac = (-2)^2 - 1 \cdot 3 = 4 - 3 = 1$.

---

**Câu 5:** Phương trình bậc hai $2x^2 - 7x + 3 = 0$ có hai nghiệm là:  
A. $x_1 = 3;\ x_2 = \dfrac{1}{2}$  
B. $x_1 = -3;\ x_2 = -\dfrac{1}{2}$  
C. $x_1 = 1;\ x_2 = \dfrac{3}{2}$  
D. $x_1 = 2;\ x_2 = 3$  
*Đáp án đúng:* **A**  
*Lời giải:* $\Delta = (-7)^2 - 4(2)(3) = 49 - 24 = 25 > 0 \implies \sqrt{\Delta} = 5$. Nghiệm $x_1 = \dfrac{7 + 5}{4} = 3;\ x_2 = \dfrac{7 - 5}{4} = \dfrac{1}{2}$.

---

**Câu 6:** Gọi $x_1, x_2$ là hai nghiệm của phương trình $x^2 - 5x - 6 = 0$. Giá trị của biểu thức $S = x_1 + x_2$ và $P = x_1 x_2$ lần lượt là:  
A. $S = 5;\ P = -6$  
B. $S = -5;\ P = 6$  
C. $S = 5;\ P = 6$  
D. $S = -5;\ P = -6$  
*Đáp án đúng:* **A**  
*Lời giải:* Theo định lý Vi-ét: $S = x_1 + x_2 = -\dfrac{b}{a} = 5$ và $P = x_1 x_2 = \dfrac{c}{a} = -6$.

---

**Câu 7:** Hai số $u$ và $v$ có tổng $u + v = 7$ và tích $uv = 12$ là hai nghiệm của phương trình:  
A. $x^2 - 7x + 12 = 0$  
B. $x^2 + 7x + 12 = 0$  
C. $x^2 - 12x + 7 = 0$  
D. $x^2 + 12x - 7 = 0$  
*Đáp án đúng:* **A**  
*Lời giải:* Hai số có tổng là $S$ và tích là $P$ là nghiệm của phương trình $x^2 - Sx + P = 0 \iff x^2 - 7x + 12 = 0$.

---

**Câu 8:** Trong một đường tròn, góc nội tiếp chắn nửa đường tròn có số đo bằng:  
A. $60^\circ$  
B. $90^\circ$  
C. $180^\circ$  
D. $45^\circ$  
*Đáp án đúng:* **B**  
*Lời giải:* Góc nội tiếp chắn nửa đường tròn có số đo bằng một nửa số đo cung bị chắn ($180^\circ / 2 = 90^\circ$).

---

**Câu 9:** Cho đường tròn $(O)$, góc ở tâm $\widehat{AOB} = 80^\circ$. Số đo của cung nhỏ $\overparen{AB}$ bằng:  
A. $40^\circ$  
B. $80^\circ$  
C. $160^\circ$  
D. $100^\circ$  
*Đáp án đúng:* **B**  
*Lời giải:* Số đo của cung nhỏ bằng chính số đo của góc ở tâm chắn cung đó: sđ $\overparen{AB} = \widehat{AOB} = 80^\circ$.

---

**Câu 10:** Tứ giác $ABCD$ nội tiếp đường tròn có $\widehat{A} = 75^\circ$. Số đo của góc $\widehat{C}$ đối diện bằng:  
A. $105^\circ$  
B. $15^\circ$  
C. $75^\circ$  
D. $115^\circ$  
*Đáp án đúng:* **A**  
*Lời giải:* Trong tứ giác nội tiếp, tổng hai góc đối nhau bằng $180^\circ$. Do đó $\widehat{C} = 180^\circ - \widehat{A} = 180^\circ - 75^\circ = 105^\circ$.

---

**Câu 11:** Cho đường tròn $(O; R)$ và dây cung $BC = R\sqrt{3}$. Góc ở tâm $\widehat{BOC}$ chắn dây $BC$ có số đo bằng:  
A. $60^\circ$  
B. $90^\circ$  
C. $120^\circ$  
D. $150^\circ$  
*Đáp án đúng:* **C**  
*Lời giải:* Kẻ $OH \perp BC \implies BH = \dfrac{BC}{2} = \dfrac{R\sqrt{3}}{2}$. Trong tam giác vuông $OBH$: $\sin \widehat{BOH} = \dfrac{BH}{OB} = \dfrac{R\sqrt{3}/2}{R} = \dfrac{\sqrt{3}}{2} \implies \widehat{BOH} = 60^\circ \implies \widehat{BOC} = 2 \cdot 60^\circ = 120^\circ$.

---

**Câu 12:** Điều kiện của tham số $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt là:  
A. $m < 1$  
B. $m \le 1$  
C. $m > 1$  
D. $m = 1$  
*Đáp án đúng:* **A**  
*Lời giải:* Phương trình có hai nghiệm phân biệt $\iff \Delta' > 0 \iff (-1)^2 - 1 \cdot m > 0 \iff 1 - m > 0 \iff m < 1$.

---

## PHẦN II: TỰ LUẬN (7.0 ĐIỂM - 5 BÀI TOÁN)

### Bài 1 (1.5 điểm): Giải phương trình và hệ phương trình
1. Giải hệ phương trình:  
   $$\begin{cases} 3x + 2y = 8 \\ 2x - y = 3 \end{cases}$$
2. Giải phương trình bậc hai:  
   $$2x^2 - 5x + 2 = 0$$

#### Lời giải chi tiết:
**Ý 1 (0.75 điểm):**  
Từ phương trình thứ hai rút ra: $y = 2x - 3$.  
Thế vào phương trình thứ nhất:  
$$3x + 2(2x - 3) = 8 \iff 3x + 4x - 6 = 8 \iff 7x = 14 \iff x = 2$$
Thay $x = 2$ vào $y = 2x - 3 \implies y = 2(2) - 3 = 1$.  
Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (2; 1)$.

**Ý 2 (0.75 điểm):**  
Phương trình: $2x^2 - 5x + 2 = 0$.  
Hệ số: $a = 2, b = -5, c = 2$.  
Biệt thức: $\Delta = b^2 - 4ac = (-5)^2 - 4 \cdot 2 \cdot 2 = 25 - 16 = 9 > 0$.  
Căn bậc hai của $\Delta$: $\sqrt{\Delta} = \sqrt{9} = 3$.  
Phương trình có hai nghiệm phân biệt:  
$$x_1 = \dfrac{-b + \sqrt{\Delta}}{2a} = \dfrac{5 + 3}{4} = 2$$
$$x_2 = \dfrac{-b - \sqrt{\Delta}}{2a} = \dfrac{5 - 3}{4} = \dfrac{2}{4} = \dfrac{1}{2}$$
Vậy tập nghiệm của phương trình là $S = \left\{2; \dfrac{1}{2}\right\}$.

---

### Bài 2 (1.5 điểm): Tương giao Parabol và Định lý Vi-ét
Cho Parabol $(P): y = x^2$ và đường thẳng $(d): y = 2x + m - 1$ ($m$ là tham số).
1. Với $m = 4$, tìm tọa độ các giao điểm của $(d)$ và $(P)$.
2. Tìm tất cả các giá trị của $m$ để $(d)$ cắt $(P)$ tại hai điểm phân biệt có hoành độ $x_1, x_2$ thỏa mãn hệ thức:  
   $$x_1^2 + x_2^2 - x_1 x_2 = 7$$

#### Lời giải chi tiết:
Phương trình hoành độ giao điểm của $(P)$ và $(d)$ là:  
$$x^2 = 2x + m - 1 \iff x^2 - 2x - (m - 1) = 0 \quad (*)$$

**Ý 1 (0.75 điểm):**  
Khi $m = 4$, phương trình $(*)$ trở thành:  
$$x^2 - 2x - 3 = 0$$
Vì $a - b + c = 1 - (-2) + (-3) = 0$ nên phương trình có hai nghiệm:  
$$x_1 = -1 \implies y_1 = (-1)^2 = 1$$
$$x_2 = -\dfrac{c}{a} = 3 \implies y_2 = 3^2 = 9$$
Vậy với $m = 4$, tọa độ hai giao điểm là $A(-1; 1)$ và $B(3; 9)$.

**Ý 2 (0.75 điểm):**  
Để $(d)$ cắt $(P)$ tại hai điểm phân biệt $\iff$ phương trình $(*)$ có hai nghiệm phân biệt:  
$$\Delta' = (-1)^2 - 1 \cdot [-(m - 1)] = 1 + m - 1 = m > 0$$
Theo định lý Vi-ét, ta có:  
$$\begin{cases} x_1 + x_2 = 2 \\ x_1 x_2 = -(m - 1) = 1 - m \end{cases}$$
Biến đổi hệ thức bài ra:  
$$x_1^2 + x_2^2 - x_1 x_2 = 7 \iff (x_1 + x_2)^2 - 3x_1 x_2 = 7$$
Thay các giá trị theo $m$ vào:  
$$2^2 - 3(1 - m) = 7 \iff 4 - 3 + 3m = 7 \iff 1 + 3m = 7 \iff 3m = 6 \iff m = 2$$
Đối chiếu điều kiện $m > 0$, giá trị $m = 2$ thỏa mãn.  
Vậy $m = 2$ là giá trị cần tìm.

---

### Bài 3 (1.5 điểm): Giải bài toán bằng cách lập hệ phương trình
Hai xưởng sản xuất may theo kế hoạch phải may tổng cộng $3000$ chiếc áo ấm cho học sinh vùng cao. Nhờ cải tiến kỹ thuật, trong thực tế xưởng I đã may vượt mức $10\%$, xưởng II may vượt mức $15\%$ so với kế hoạch, do đó cả hai xưởng đã may được tất cả $3380$ chiếc áo. Hỏi theo kế hoạch ban đầu, mỗi xưởng phải may bao nhiêu chiếc áo?

#### Lời giải chi tiết:
Gọi số áo ấm xưởng I phải may theo kế hoạch là $x$ (chiếc áo, $x \in \mathbb{N}^*, x < 3000$).  
Gọi số áo ấm xưởng II phải may theo kế hoạch là $y$ (chiếc áo, $y \in \mathbb{N}^*, y < 3000$).  
Theo kế hoạch ban đầu cả hai xưởng phải may 3000 chiếc áo, ta có phương trình:  
$$x + y = 3000 \quad (1)$$

Trong thực tế:  
- Xưởng I vượt mức $10\%$, số áo vượt là: $10\% \cdot x = 0{,}1x$ chiếc.  
- Xưởng II vượt mức $15\%$, số áo vượt là: $15\% \cdot y = 0{,}15y$ chiếc.  
Tổng số áo may được là 3380 chiếc, tức số áo vượt mức là:  
$$3380 - 3000 = 380\text{ chiếc}$$
Ta có phương trình:  
$$0{,}1x + 0{,}15y = 380 \iff 10x + 15y = 38000 \iff 2x + 3y = 7600 \quad (2)$$

Từ (1) và (2) ta có hệ phương trình:  
$$\begin{cases} x + y = 3000 \\ 2x + 3y = 7600 \end{cases}$$
Nhân phương trình (1) với 2:  
$$\begin{cases} 2x + 2y = 6000 \\ 2x + 3y = 7600 \end{cases}$$
Lấy phương trình dưới trừ phương trình trên:  
$$y = 7600 - 6000 = 1600\text{ (thỏa mãn)}$$
Thay $y = 1600$ vào (1):  
$$x = 3000 - 1600 = 1400\text{ (thỏa mãn)}$$
Vậy theo kế hoạch, xưởng I phải may $1400$ chiếc áo và xưởng II phải may $1600$ chiếc áo.

---

### Bài 4 (2.0 điểm): Hình học đường tròn & Tứ giác nội tiếp
Cho đường tròn $(O; R)$, từ điểm $M$ nằm ngoài đường tròn kẻ hai tiếp tuyến $MA, MB$ với đường tròn ($A, B$ là hai tiếp điểm). Kẻ cát tuyến $MCD$ không đi qua tâm $O$ ($C$ nằm giữa $M$ và $D$). Gọi $H$ là giao điểm của $OM$ và $AB$.
1. Chứng minh bốn điểm $M, A, O, B$ cùng thuộc một đường tròn và $OM \perp AB$ tại $H$.
2. Chứng minh $MA^2 = MC \cdot MD$ và $MC \cdot MD = MH \cdot MO$.

#### Lời giải chi tiết:
**Ý 1 (1.0 điểm):**  
- Vì $MA, MB$ là hai tiếp tuyến của $(O)$ nên $\widehat{MAO} = 90^\circ$ và $\widehat{MBO} = 90^\circ$.  
- Tứ giác $MAOB$ có $\widehat{MAO} + \widehat{MBO} = 90^\circ + 90^\circ = 180^\circ$, do đó tứ giác $MAOB$ nội tiếp đường tròn đường kính $OM$.  
- Ta có $MA = MB$ (tính chất hai tiếp tuyến cắt nhau) và $OA = OB = R$.  
  Suy ra $OM$ là đường trung trực của đoạn thẳng $AB \implies OM \perp AB$ tại $H$.

**Ý 2 (1.0 điểm):**  
- Xét hai tam giác $\triangle MAC$ và $\triangle MDA$:  
  - Có góc $\widehat{AMD}$ chung.  
  - $\widehat{MAC} = \widehat{MDA}$ (góc tạo bởi tia tiếp tuyến và dây cung bằng góc nội tiếp cùng chắn cung $\overparen{AC}$).  
  Do đó $\triangle MAC \backsim \triangle MDA$ (g-g).  
  Suy ra tỉ số đồng dạng: $\dfrac{MA}{MD} = \dfrac{MC}{MA} \implies MA^2 = MC \cdot MD \quad (1)$.  
- Mặt khác, trong tam giác vuông $OAM$ vuông tại $A$ có đường cao $AH$:  
  Theo hệ thức lượng trong tam giác vuông: $MA^2 = MH \cdot MO \quad (2)$.  
- Từ (1) và (2) suy ra: $MC \cdot MD = MH \cdot MO$ (đpcm).

---

### Bài 5 (0.5 điểm): Cực trị đại số
Cho các số thực không âm $x, y$ thỏa mãn $x^2 + y^2 = 4$. Tìm giá trị lớn nhất và giá trị nhỏ nhất của biểu thức:
$$M = x + y$$

#### Lời giải chi tiết:
- **Tìm giá trị lớn nhất (GTLN):**  
  Áp dụng bất đẳng thức Bunhiacopxki (Cauchy-Schwarz) cho hai bộ số $(1; 1)$ và $(x; y)$:  
  $$(1 \cdot x + 1 \cdot y)^2 \le (1^2 + 1^2)(x^2 + y^2) = 2 \cdot 4 = 8$$
  $$\implies (x + y)^2 \le 8 \implies x + y \le 2\sqrt{2} \quad (\text{do } x, y \ge 0)$$
  Dấu đẳng thức xảy ra khi:  
  $$\begin{cases} \dfrac{x}{1} = \dfrac{y}{1} \implies x = y \\ x^2 + y^2 = 4 \end{cases} \iff 2x^2 = 4 \iff x = y = \sqrt{2}$$
  Vậy $\max M = 2\sqrt{2}$.

- **Tìm giá trị nhỏ nhất (GTNN):**  
  Vì $x \ge 0, y \ge 0$ nên $2xy \ge 0$. Ta có:  
  $$M^2 = (x + y)^2 = x^2 + y^2 + 2xy = 4 + 2xy \ge 4$$
  $$\implies M \ge 2$$
  Dấu đẳng thức xảy ra khi:  
  $$2xy = 0 \iff x = 0 \text{ hoặc } y = 0$$
  Kết hợp $x^2 + y^2 = 4$, ta được $(x; y) = (0; 2)$ hoặc $(x; y) = (2; 0)$.  
  Vậy $\min M = 2$.
"""

with open(os.path.join(MATH_DIR, "de_thi_giua_hoc_ky_2_toan_9.md"), "w", encoding="utf-8") as f:
    f.write(de_thi_giua_hk2)
print("Created de_thi_giua_hoc_ky_2_toan_9.md")
