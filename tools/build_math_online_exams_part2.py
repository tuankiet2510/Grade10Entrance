# -*- coding: utf-8 -*-
"""
Generate de_thi_hoc_ky_2_toan_9.md and de_thi_tuyen_sinh_vao_10_toan_quang_ngai.md
"""
import os

MATH_DIR = r"f:\OnThiC3\EnglishDocs\docs\math"

# ==========================================
# 1. de_thi_hoc_ky_2_toan_9.md
# ==========================================
de_thi_hk2 = r"""---
title: "Đề Kiểm Tra Cuối Học Kỳ 2 Toán 9 (Năm học 2026 - 2027)"
category: "Đề Thi Toán 9"
description: "Đề kiểm tra cuối học kỳ 2 môn Toán 9 bao quát toàn bộ chương trình GDPT 2018 (12 câu trắc nghiệm khách quan + 5 bài toán tự luận Phương trình bậc hai, Vi-ét, Thống kê, Xác suất, Tứ giác nội tiếp, Hình trụ nón cầu và BĐT) có lời giải chi tiết."
---

# 📐 Đề Kiểm Tra Cuối Học Kỳ 2 Toán 9 (Năm học 2026 - 2027)

> **Môn thi:** Toán 9 • **Thời gian làm bài:** 90 phút (không kể thời gian phát đề)  
> **Phạm vi kiến thức trọng tâm:**  
> - Đại số & Phương trình: Phương trình bậc hai một ẩn, định lý Vi-ét và các dạng toán thực tế.  
> - Thống kê & Xác suất: Bảng tần số, tần số tương đối, không gian mẫu và xác suất của biến cố.  
> - Hình học phẳng & Hình học không gian: Góc với đường tròn, tứ giác nội tiếp, diện tích & thể tích các hình khối (hình trụ, hình nón, hình cầu).

---

## PHẦN I: TRẮC NGHIỆM KHÁCH QUAN (3.0 ĐIỂM - 12 CÂU)

::: info HƯỚNG DẪN LÀM BÀI
Mỗi câu hỏi có 4 phương án trả lời A, B, C, D. Chọn một phương án đúng duy nhất (mỗi câu đúng được 0.25 điểm).
:::

**Câu 1:** Phương trình bậc hai $x^2 - 6x + 9 = 0$ có:  
A. Hai nghiệm phân biệt  
B. Vô nghiệm  
C. Nghiệm kép $x_1 = x_2 = 3$  
D. Nghiệm kép $x_1 = x_2 = -3$  
*Đáp án đúng:* **C**  
*Lời giải:* Ta có $\Delta' = (-3)^2 - 1 \cdot 9 = 9 - 9 = 0$. Phương trình có nghiệm kép $x_1 = x_2 = -\dfrac{b'}{a} = 3$.

---

**Câu 2:** Cho phương trình $2x^2 + 5x - 7 = 0$. Tổng và tích hai nghiệm $x_1, x_2$ của phương trình là:  
A. $x_1 + x_2 = -\dfrac{5}{2};\ x_1 x_2 = -\dfrac{7}{2}$  
B. $x_1 + x_2 = \dfrac{5}{2};\ x_1 x_2 = -\dfrac{7}{2}$  
C. $x_1 + x_2 = -\dfrac{5}{2};\ x_1 x_2 = \dfrac{7}{2}$  
D. $x_1 + x_2 = 5;\ x_1 x_2 = -7$  
*Đáp án đúng:* **A**  
*Lời giải:* Theo định lý Vi-ét: $x_1 + x_2 = -\dfrac{b}{a} = -\dfrac{5}{2}$ và $x_1 x_2 = \dfrac{c}{a} = -\dfrac{7}{2}$.

---

**Câu 3:** Gieo một con xúc xắc cân đối và đồng chất một lần. Xác suất để xuất hiện mặt có số chấm là số nguyên tố bằng:  
A. $\dfrac{1}{2}$  
B. $\dfrac{1}{3}$  
C. $\dfrac{2}{3}$  
D. $\dfrac{1}{6}$  
*Đáp án đúng:* **A**  
*Lời giải:* Không gian mẫu $\Omega = \{1; 2; 3; 4; 5; 6\} \implies n(\Omega) = 6$. Các mặt có số chấm là số nguyên tố: $A = \{2; 3; 5\} \implies n(A) = 3$. Xác suất $P(A) = \dfrac{3}{6} = \dfrac{1}{2}$.

---

**Câu 4:** Một hộp đựng 5 quả bóng xanh và 3 quả bóng đỏ có kích thước như nhau. Lấy ngẫu nhiên 1 quả bóng. Xác suất lấy được bóng màu đỏ là:  
A. $\dfrac{3}{8}$  
B. $\dfrac{5}{8}$  
C. $\dfrac{3}{5}$  
D. $\dfrac{1}{8}$  
*Đáp án đúng:* **A**  
*Lời giải:* Tổng số quả bóng là $5 + 3 = 8$. Số quả bóng đỏ là $3$. Xác suất là $\dfrac{3}{8}$.

---

**Câu 5:** Góc nội tiếp chắn nửa đường tròn luôn có số đo là:  
A. $45^\circ$  
B. $60^\circ$  
C. $90^\circ$  
D. $180^\circ$  
*Đáp án đúng:* **C**  
*Lời giải:* Theo tính chất góc nội tiếp: Góc nội tiếp chắn nửa đường tròn là góc vuông ($90^\circ$).

---

**Câu 6:** Cho tứ giác $ABCD$ nội tiếp đường tròn $(O)$ có $\widehat{B} = 110^\circ$. Số đo của góc $\widehat{D}$ là:  
A. $70^\circ$  
B. $80^\circ$  
C. $110^\circ$  
D. $90^\circ$  
*Đáp án đúng:* **A**  
*Lời giải:* Trong tứ giác nội tiếp, hai góc đối có tổng bằng $180^\circ$. Suy ra $\widehat{D} = 180^\circ - \widehat{B} = 180^\circ - 110^\circ = 70^\circ$.

---

**Câu 7:** Một hình trụ có bán kính đáy $r = 4\text{ cm}$ và chiều cao $h = 5\text{ cm}$. Diện tích xung quanh của hình trụ là:  
A. $40\pi\text{ cm}^2$  
B. $20\pi\text{ cm}^2$  
C. $80\pi\text{ cm}^2$  
D. $16\pi\text{ cm}^2$  
*Đáp án đúng:* **A**  
*Lời giải:* Diện tích xung quanh hình trụ: $S_{xq} = 2\pi rh = 2\pi \cdot 4 \cdot 5 = 40\pi\text{ cm}^2$.

---

**Câu 8:** Thể tích của một hình nón có bán kính đáy $r = 3\text{ cm}$ và chiều cao $h = 4\text{ cm}$ là:  
A. $12\pi\text{ cm}^3$  
B. $36\pi\text{ cm}^3$  
C. $16\pi\text{ cm}^3$  
D. $4\pi\text{ cm}^3$  
*Đáp án đúng:* **A**  
*Lời giải:* Thể tích hình nón: $V = \dfrac{1}{3}\pi r^2 h = \dfrac{1}{3}\pi \cdot 3^2 \cdot 4 = 12\pi\text{ cm}^3$.

---

**Câu 9:** Diện tích mặt cầu bán kính $R = 3\text{ cm}$ bằng:  
A. $36\pi\text{ cm}^2$  
B. $12\pi\text{ cm}^2$  
C. $9\pi\text{ cm}^2$  
D. $27\pi\text{ cm}^2$  
*Đáp án đúng:* **A**  
*Lời giải:* Diện tích mặt cầu: $S = 4\pi R^2 = 4\pi \cdot 3^2 = 36\pi\text{ cm}^2$.

---

**Câu 10:** Cho phương trình $x^2 - (m + 1)x + m = 0$. Phương trình luôn có hai nghiệm là:  
A. $x_1 = 1;\ x_2 = m$  
B. $x_1 = -1;\ x_2 = -m$  
C. $x_1 = 1;\ x_2 = -m$  
D. $x_1 = -1;\ x_2 = m$  
*Đáp án đúng:* **A**  
*Lời giải:* Vì $a + b + c = 1 - (m + 1) + m = 1 - m - 1 + m = 0$ nên phương trình có hai nghiệm $x_1 = 1$ và $x_2 = \dfrac{c}{a} = m$.

---

**Câu 11:** Trong một cuộc khảo sát thời gian tự học (giờ/ngày) của học sinh, giá trị có tần số lớn nhất được gọi là:  
A. Mốt của mẫu số liệu  
B. Số trung bình  
C. Trung vị  
D. Tần số tương đối  
*Đáp án đúng:* **A**  
*Lời giải:* Theo định nghĩa thống kê lớp 9, giá trị có tần số xuất hiện lớn nhất trong mẫu số liệu được gọi là Mốt (kí hiệu là $M_o$).

---

**Câu 12:** Độ dài cung tròn $60^\circ$ của đường tròn bán kính $R = 6\text{ cm}$ bằng:  
A. $2\pi\text{ cm}$  
B. $\pi\text{ cm}$  
C. $3\pi\text{ cm}$  
D. $6\pi\text{ cm}$  
*Đáp án đúng:* **A**  
*Lời giải:* Công thức độ dài cung tròn: $l = \dfrac{\pi R n}{180} = \dfrac{\pi \cdot 6 \cdot 60}{180} = 2\pi\text{ cm}$.

---

## PHẦN II: TỰ LUẬN (7.0 ĐIỂM - 5 BÀI TOÁN)

### Bài 1 (1.5 điểm): Rút gọn biểu thức
Cho hai biểu thức:  
$$A = \dfrac{\sqrt{x} + 1}{\sqrt{x} - 2} \quad \text{và} \quad B = \dfrac{\sqrt{x}}{\sqrt{x} + 2} + \dfrac{4\sqrt{x}}{x - 4} \quad (\text{với } x \ge 0, x \ne 4)$$

1. Tính giá trị của biểu thức $A$ khi $x = 9$.
2. Rút gọn biểu thức $B$.
3. Đặt $M = \dfrac{B}{A}$. Tìm giá trị nguyên của $x$ để $M \ge \dfrac{1}{2}$.

#### Lời giải chi tiết:
**Ý 1 (0.5 điểm):**  
Thay $x = 9$ (thỏa mãn ĐKXĐ) vào biểu thức $A$:  
$$A = \dfrac{\sqrt{9} + 1}{\sqrt{9} - 2} = \dfrac{3 + 1}{3 - 2} = 4$$

**Ý 2 (0.5 điểm):**  
Ta có $x - 4 = (\sqrt{x} - 2)(\sqrt{x} + 2)$. Mẫu thức chung là $(\sqrt{x} - 2)(\sqrt{x} + 2)$:  
$$B = \dfrac{\sqrt{x}(\sqrt{x} - 2) + 4\sqrt{x}}{(\sqrt{x} - 2)(\sqrt{x} + 2)} = \dfrac{x - 2\sqrt{x} + 4\sqrt{x}}{(\sqrt{x} - 2)(\sqrt{x} + 2)}$$
$$= \dfrac{x + 2\sqrt{x}}{(\sqrt{x} - 2)(\sqrt{x} + 2)} = \dfrac{\sqrt{x}(\sqrt{x} + 2)}{(\sqrt{x} - 2)(\sqrt{x} + 2)} = \dfrac{\sqrt{x}}{\sqrt{x} - 2}$$
Vậy $B = \dfrac{\sqrt{x}}{\sqrt{x} - 2}$.

**Ý 3 (0.5 điểm):**  
Ta có:  
$$M = \dfrac{B}{A} = \dfrac{\sqrt{x}}{\sqrt{x} - 2} : \dfrac{\sqrt{x} + 1}{\sqrt{x} - 2} = \dfrac{\sqrt{x}}{\sqrt{x} + 1}$$
Để $M \ge \dfrac{1}{2}$:  
$$\dfrac{\sqrt{x}}{\sqrt{x} + 1} \ge \dfrac{1}{2} \iff \dfrac{2\sqrt{x} - (\sqrt{x} + 1)}{2(\sqrt{x} + 1)} \ge 0 \iff \dfrac{\sqrt{x} - 1}{2(\sqrt{x} + 1)} \ge 0$$
Vì $x \ge 0 \implies 2(\sqrt{x} + 1) > 0$. Do đó bất phương trình tương đương:  
$$\sqrt{x} - 1 \ge 0 \iff \sqrt{x} \ge 1 \iff x \ge 1$$
Kết hợp điều kiện xác định $x \ge 0, x \ne 4$, ta được $x \ge 1$ và $x \ne 4$.  
Các số nguyên $x$ thỏa mãn là $x \in \{1; 2; 3; 5; 6; 7; \dots\}$.

---

### Bài 2 (1.5 điểm): Phương trình bậc hai & Định lý Vi-ét
Cho phương trình bậc hai: $x^2 - 2(m - 1)x + m^2 - 4 = 0$ ($m$ là tham số).
1. Tìm $m$ để phương trình có hai nghiệm phân biệt $x_1, x_2$.
2. Tìm $m$ để hai nghiệm thỏa mãn hệ thức:  
   $$x_1^2 + x_2^2 - 3x_1 x_2 = 11$$

#### Lời giải chi tiết:
**Ý 1 (0.75 điểm):**  
Ta có: $a = 1, b' = -(m - 1), c = m^2 - 4$.  
$$\Delta' = [-(m - 1)]^2 - 1 \cdot (m^2 - 4) = m^2 - 2m + 1 - m^2 + 4 = 5 - 2m$$
Để phương trình có hai nghiệm phân biệt $\iff \Delta' > 0 \iff 5 - 2m > 0 \iff m < \dfrac{5}{2}$.

**Ý 2 (0.75 điểm):**  
Với $m < \dfrac{5}{2}$, theo định lý Vi-ét ta có:  
$$\begin{cases} x_1 + x_2 = 2(m - 1) \\ x_1 x_2 = m^2 - 4 \end{cases}$$
Biến đổi hệ thức bài ra:  
$$x_1^2 + x_2^2 - 3x_1 x_2 = 11 \iff (x_1 + x_2)^2 - 5x_1 x_2 = 11$$
Thay $x_1 + x_2$ và $x_1 x_2$ vào:  
$$[2(m - 1)]^2 - 5(m^2 - 4) = 11$$
$$\iff 4(m^2 - 2m + 1) - 5m^2 + 20 = 11$$
$$\iff 4m^2 - 8m + 4 - 5m^2 + 20 = 11$$
$$\iff -m^2 - 8m + 24 = 11 \iff -m^2 - 8m + 13 = 0 \iff m^2 + 8m - 13 = 0$$
Giải phương trình theo $m$:  
$$\Delta'_m = 4^2 - 1 \cdot (-13) = 16 + 13 = 29 > 0$$
$$\implies m = -4 + \sqrt{29} \quad \text{hoặc} \quad m = -4 - \sqrt{29}$$
So sánh với điều kiện $m < \dfrac{5}{2} = 2{,}5$:  
- Với $m_1 = -4 + \sqrt{29} \approx -4 + 5{,}385 = 1{,}385 < 2{,}5$ (thỏa mãn).  
- Với $m_2 = -4 - \sqrt{29} \approx -9{,}385 < 2{,}5$ (thỏa mãn).  
Vậy $m = -4 \pm \sqrt{29}$ là các giá trị cần tìm.

---

### Bài 3 (1.5 điểm): Thống kê - Xác suất & Toán thực tế
1. Một hộp chứa 20 tấm thẻ được đánh số thứ tự từ 1 đến 20. Rút ngẫu nhiên một tấm thẻ trong hộp. Tính xác suất của biến cố:  
   a) "Tấm thẻ rút ra ghi số chia hết cho 5".  
   b) "Tấm thẻ rút ra ghi số là số chính phương".
2. Một lon nước ngọt dạng hình trụ có bán kính đáy $r = 3\text{ cm}$ và chiều cao $h = 12\text{ cm}$.  
   a) Tính diện tích toàn phần của lon nước ngọt (lấy $\pi \approx 3{,}14$, làm tròn đến chữ số thập phân thứ nhất).  
   b) Lon nước ngọt đó có thể chứa tối đa bao nhiêu mililít ($1\text{ ml} = 1\text{ cm}^3$)?

#### Lời giải chi tiết:
**Ý 1 (0.75 điểm):**  
Không gian mẫu có $n(\Omega) = 20$ kết quả đồng khả năng.  
a) Tập hợp các số chia hết cho 5 từ 1 đến 20: $A = \{5; 10; 15; 20\} \implies n(A) = 4$.  
Xác suất: $P(A) = \dfrac{4}{20} = \dfrac{1}{5} = 0{,}2$.  
b) Tập hợp các số chính phương từ 1 đến 20: $B = \{1; 4; 9; 16\} \implies n(B) = 4$.  
Xác suất: $P(B) = \dfrac{4}{20} = \dfrac{1}{5} = 0{,}2$.

**Ý 2 (0.75 điểm):**  
a) Diện tích toàn phần của lon nước ngọt:  
$$S_{tp} = S_{xq} + 2S_{\text{đáy}} = 2\pi rh + 2\pi r^2 = 2\pi r(h + r)$$
$$S_{tp} = 2 \cdot 3{,}14 \cdot 3 \cdot (12 + 3) = 18{,}84 \cdot 15 = 282{,}6\text{ cm}^2$$
b) Thể tích lon nước ngọt:  
$$V = \pi r^2 h = 3{,}14 \cdot 3^2 \cdot 12 = 3{,}14 \cdot 9 \cdot 12 = 339{,}12\text{ cm}^3$$
Vì $1\text{ cm}^3 = 1\text{ ml}$ nên thể tích lon có thể chứa tối đa xấp xỉ $339{,}1\text{ ml}$.

---

### Bài 4 (2.0 điểm): Hình học tổng hợp
Cho tam giác nhọn $ABC$ ($AB < AC$) nội tiếp đường tròn $(O; R)$. Ba đường cao $AD, BE, CF$ cắt nhau tại trực tâm $H$.
1. Chứng minh các tứ giác $BCEF$ và $AEHF$ là các tứ giác nội tiếp.
2. Vẽ đường kính $AK$ của đường tròn $(O)$. Chứng minh $AB \cdot AC = AD \cdot AK = 2R \cdot AD$.
3. Chứng minh $OA \perp EF$.

#### Lời giải chi tiết:
**Ý 1 (1.0 điểm):**  
- Xét tứ giác $BCEF$:  
  Có $\widehat{BEC} = 90^\circ$ (do $BE \perp AC$) và $\widehat{BFC} = 90^\circ$ (do $CF \perp AB$).  
  Hai đỉnh $E, F$ kề nhau cùng nhìn cạnh $BC$ dưới góc vuông $90^\circ$.  
  Do đó tứ giác $BCEF$ nội tiếp đường tròn đường kính $BC$.  
- Xét tứ giác $AEHF$:  
  Có $\widehat{AEH} = 90^\circ$ và $\widehat{AFH} = 90^\circ$.  
  Tổng hai góc đối diện: $\widehat{AEH} + \widehat{AFH} = 90^\circ + 90^\circ = 180^\circ$.  
  Do đó tứ giác $AEHF$ nội tiếp đường tròn đường kính $AH$.

**Ý 2 (0.5 điểm):**  
- Vì $AK$ là đường kính của $(O)$ nên góc nội tiếp $\widehat{ACK} = 90^\circ$.  
- Xét $\triangle ABD$ và $\triangle AKC$:  
  - Có $\widehat{ADB} = \widehat{ACK} = 90^\circ$.  
  - Có $\widehat{ABD} = \widehat{AKC}$ (hai góc nội tiếp cùng chắn cung nhỏ $\overparen{AC}$ của $(O)$).  
  Suy ra $\triangle ABD \backsim \triangle AKC$ (g-g).  
- Từ đó ta có tỉ số đồng dạng:  
  $$\dfrac{AB}{AK} = \dfrac{AD}{AC} \implies AB \cdot AC = AD \cdot AK$$
  Vì $AK = 2R$ nên $AB \cdot AC = 2R \cdot AD$ (đpcm).

**Ý 3 (0.5 điểm):**  
- Kẻ tiếp tuyến $Ax$ với đường tròn $(O)$ tại $A$ ($Ax$ nằm trên nửa mặt phẳng bờ $AB$ chứa $C$).  
- Ta có $\widehat{xAB} = \widehat{ACB}$ (góc tạo bởi tiếp tuyến và dây cung bằng góc nội tiếp cùng chắn cung $\overparen{AB}$).  
- Mặt khác, do tứ giác $BCEF$ nội tiếp nên góc ngoài tại đỉnh $E$ bằng góc trong tại đỉnh đối diện: $\widehat{AFE} = \widehat{ACB}$.  
- Suy ra $\widehat{xAB} = \widehat{AFE}$. Mà hai góc này ở vị trí so le trong nên $Ax \parallel EF$.  
- Vì $Ax$ là tiếp tuyến của $(O)$ tại $A$ nên $OA \perp Ax$. Kết hợp $Ax \parallel EF \implies OA \perp EF$ (đpcm).

---

### Bài 5 (0.5 điểm): Bất đẳng thức phân loại học sinh giỏi
Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Tìm giá trị nhỏ nhất của biểu thức:
$$P = \dfrac{a^2}{b + 1} + \dfrac{b^2}{c + 1} + \dfrac{c^2}{a + 1}$$

#### Lời giải chi tiết:
Áp dụng bất đẳng thức Cauchy dạng Engel (Cauchy-Schwarz dạng phân thức):  
$$P = \dfrac{a^2}{b + 1} + \dfrac{b^2}{c + 1} + \dfrac{c^2}{a + 1} \ge \dfrac{(a + b + c)^2}{(b + 1) + (c + 1) + (a + 1)}$$
Ta có:  
$$(a + b + c)^2 = 3^2 = 9$$
Mẫu số:  
$$(b + 1) + (c + 1) + (a + 1) = a + b + c + 3 = 3 + 3 = 6$$
Do đó:  
$$P \ge \dfrac{9}{6} = \dfrac{3}{2}$$
Dấu đẳng thức xảy ra khi và chỉ khi:  
$$\dfrac{a}{b + 1} = \dfrac{b}{c + 1} = \dfrac{c}{a + 1} \quad \text{và} \quad a + b + c = 3 \iff a = b = c = 1$$
Vậy giá trị nhỏ nhất của biểu thức $P$ là $\dfrac{3}{2}$, đạt được khi $a = b = c = 1$.
"""

with open(os.path.join(MATH_DIR, "de_thi_hoc_ky_2_toan_9.md"), "w", encoding="utf-8") as f:
    f.write(de_thi_hk2)
print("Created de_thi_hoc_ky_2_toan_9.md")

# ==========================================
# 2. de_thi_tuyen_sinh_vao_10_toan_quang_ngai.md
# ==========================================
de_thi_quang_ngai = r"""---
title: "Đề Thi Tuyển Sinh Vào Lớp 10 THPT Môn Toán - Tỉnh Quảng Ngãi"
category: "Đề Tuyển Sinh Vào 10"
description: "Đề thi chính thức tuyển sinh vào lớp 10 THPT tỉnh Quảng Ngãi theo đúng cấu trúc chuẩn ma trận đề thi 5 câu tự luận (Rút gọn căn thức, Parabol và Viète, Lập phương trình toán thực tế chuyển động, Hình học đường tròn 3 ý và Bất đẳng thức cực trị phân loại 10 điểm) có lời giải chi tiết."
---

# 🏛️ Đề Thi Tuyển Sinh Vào Lớp 10 THPT Môn Toán - Tỉnh Quảng Ngãi

> **Kỳ thi:** Tuyển sinh vào lớp 10 THPT công lập • **Tỉnh Quảng Ngãi**  
> **Môn thi:** Toán (Chung) • **Thời gian làm bài:** 120 phút (không kể thời gian phát đề)  
> **Cấu trúc đề:** 100% Tự luận (5 bài toán theo chuẩn ma trận đề thi chính thức của Sở GD&ĐT Quảng Ngãi)

---

## NỘI DUNG ĐỀ THI

### Bài 1 (2.0 điểm): Căn thức bậc hai & Rút gọn biểu thức
1. Thực hiện phép tính:  
   $$A = \sqrt{48} - 2\sqrt{75} + \sqrt{108} - \sqrt{(\sqrt{3} - 2)^2}$$
2. Cho biểu thức:  
   $$P = \left(\dfrac{\sqrt{x}}{\sqrt{x} - 1} - \dfrac{1}{x - \sqrt{x}}\right) : \dfrac{\sqrt{x} + 1}{x - 1} \quad (\text{với } x > 0, x \ne 1)$$  
   a) Rút gọn biểu thức $P$.  
   b) Tìm các giá trị của $x$ để $P < 2$.

---

### Bài 2 (2.0 điểm): Parabol & Hệ thức Vi-ét
1. Trong mặt phẳng tọa độ $Oxy$, cho Parabol $(P): y = x^2$ và đường thẳng $(d): y = 2x + 3$.  
   a) Vẽ đồ thị Parabol $(P)$ và đường thẳng $(d)$ trên cùng một hệ trục tọa độ.  
   b) Tìm tọa độ các giao điểm của $(P)$ và $(d)$ bằng phép tính.
2. Cho phương trình bậc hai: $x^2 - 2(m - 1)x + 2m - 5 = 0$ ($m$ là tham số).  
   Tìm tất cả các giá trị của $m$ để phương trình có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn:  
   $$(x_1 - x_2)^2 = 8$$

---

### Bài 3 (2.0 điểm): Hệ phương trình & Giải toán bằng cách lập phương trình
1. Giải hệ phương trình:  
   $$\begin{cases} 3x - 2y = 7 \\ 2x + 3y = 9 \end{cases}$$
2. Một ô tô tải và một ô tô du lịch cùng khởi hành từ thành phố Quảng Ngãi đi thành phố Đà Nẵng với quãng đường dài $120\text{ km}$. Vận tốc của xe du lịch lớn hơn vận tốc của xe tải là $20\text{ km/h}$, do đó xe du lịch đến Đà Nẵng sớm hơn xe tải $30$ phút. Tính vận tốc của mỗi xe.

---

### Bài 4 (3.0 điểm): Hình học đường tròn
Cho tam giác nhọn $ABC$ ($AB < AC$) nội tiếp đường tròn $(O; R)$. Các đường cao $AD, BE, CF$ cắt nhau tại trực tâm $H$.
1. Chứng minh tứ giác $BCEF$ là tứ giác nội tiếp một đường tròn.
2. Kẻ đường kính $AK$ của đường tròn $(O)$. Chứng minh tam giác $ABD$ đồng dạng với tam giác $AKC$ và suy ra $AB \cdot AC = AD \cdot AK = 2R \cdot AD$.
3. Gọi $M$ là trung điểm của đoạn thẳng $BC$. Chứng minh ba điểm $H, M, K$ thẳng hàng và $AH = 2OM$.

---

### Bài 5 (1.0 điểm): Bất đẳng thức phân loại điểm 10
Cho hai số thực dương $x, y$ thỏa mãn điều kiện $x + y = 2$. Tìm giá trị nhỏ nhất của biểu thức:
$$Q = \dfrac{1}{x^2 + y^2} + \dfrac{1}{xy}$$

---

## HƯỚNG DẪN CHẤM & LỜI GIẢI CHI TIẾT TỪNG BƯỚC

### Bài 1 (2.0 điểm)
**Ý 1 (1.0 điểm):**  
Ta có:  
- $\sqrt{48} = \sqrt{16 \cdot 3} = 4\sqrt{3}$  
- $2\sqrt{75} = 2\sqrt{25 \cdot 3} = 2 \cdot 5\sqrt{3} = 10\sqrt{3}$  
- $\sqrt{108} = \sqrt{36 \cdot 3} = 6\sqrt{3}$  
- $\sqrt{(\sqrt{3} - 2)^2} = |\sqrt{3} - 2| = 2 - \sqrt{3}$ (do $\sqrt{3} \approx 1{,}732 < 2 \implies \sqrt{3} - 2 < 0$)  

Thay vào biểu thức $A$:  
$$A = 4\sqrt{3} - 10\sqrt{3} + 6\sqrt{3} - (2 - \sqrt{3}) = (4 - 10 + 6)\sqrt{3} - 2 + \sqrt{3} = 0 - 2 + \sqrt{3} = \sqrt{3} - 2$$
Vậy $A = \sqrt{3} - 2$.

**Ý 2 (1.0 điểm):**  
a) Với $x > 0, x \ne 1$, ta có $x - \sqrt{x} = \sqrt{x}(\sqrt{x} - 1)$ và $x - 1 = (\sqrt{x} - 1)(\sqrt{x} + 1)$:  
$$P = \left(\dfrac{\sqrt{x} \cdot \sqrt{x} - 1}{\sqrt{x}(\sqrt{x} - 1)}\right) : \dfrac{\sqrt{x} + 1}{(\sqrt{x} - 1)(\sqrt{x} + 1)}$$
$$P = \dfrac{x - 1}{\sqrt{x}(\sqrt{x} - 1)} \cdot \dfrac{\sqrt{x} - 1}{1} = \dfrac{(\sqrt{x} - 1)(\sqrt{x} + 1)}{\sqrt{x}(\sqrt{x} - 1)} \cdot (\sqrt{x} - 1)$$
$$P = \dfrac{(\sqrt{x} + 1)(\sqrt{x} - 1)}{\sqrt{x}} = \dfrac{x - 1}{\sqrt{x}}$$
b) Để $P < 2$:  
$$\dfrac{x - 1}{\sqrt{x}} < 2 \iff x - 1 < 2\sqrt{x} \quad (\text{vì } \sqrt{x} > 0)$$
$$\iff x - 2\sqrt{x} - 1 < 0 \iff (\sqrt{x} - 1)^2 - 2 < 0 \iff (\sqrt{x} - 1)^2 < 2$$
$$\iff -\sqrt{2} < \sqrt{x} - 1 < \sqrt{2} \iff 1 - \sqrt{2} < \sqrt{x} < 1 + \sqrt{2}$$
Vì $\sqrt{x} > 0$ nên: $0 < \sqrt{x} < 1 + \sqrt{2}$.  
Bình phương hai vế:  
$$0 < x < (1 + \sqrt{2})^2 = 3 + 2\sqrt{2}$$
Kết hợp điều kiện $x > 0, x \ne 1$, ta được tập giá trị cần tìm:  
$$0 < x < 3 + 2\sqrt{2} \quad \text{và} \quad x \ne 1$$

---

### Bài 2 (2.0 điểm)
**Ý 1 (1.0 điểm):**  
a) Bảng giá trị cho Parabol $(P): y = x^2$:
- Khi $x = -2 \implies y = 4$
- Khi $x = -1 \implies y = 1$
- Khi $x = 0 \implies y = 0$
- Khi $x = 1 \implies y = 1$
- Khi $x = 2 \implies y = 4$
Đường thẳng $(d): y = 2x + 3$ đi qua hai điểm $(0; 3)$ và $\left(-\dfrac{3}{2}; 0\right)$.  
Vẽ đúng hai đồ thị trên cùng hệ trục tọa độ $Oxy$.

b) Phương trình hoành độ giao điểm của $(P)$ và $(d)$:  
$$x^2 = 2x + 3 \iff x^2 - 2x - 3 = 0$$
Vì $a - b + c = 1 - (-2) + (-3) = 0$ nên phương trình có hai nghiệm:  
- $x_1 = -1 \implies y_1 = (-1)^2 = 1 \implies A(-1; 1)$  
- $x_2 = 3 \implies y_2 = 3^2 = 9 \implies B(3; 9)$  
Vậy tọa độ các giao điểm là $A(-1; 1)$ và $B(3; 9)$.

**Ý 2 (1.0 điểm):**  
Phương trình: $x^2 - 2(m - 1)x + 2m - 5 = 0$.  
Biệt thức:  
$$\Delta' = [-(m - 1)]^2 - 1 \cdot (2m - 5) = m^2 - 2m + 1 - 2m + 5 = m^2 - 4m + 6 = (m - 2)^2 + 2$$
Vì $(m - 2)^2 \ge 0$ nên $\Delta' \ge 2 > 0$ với mọi $m \in \mathbb{R}$.  
Do đó phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi $m$.  
Theo định lý Vi-ét:  
$$\begin{cases} x_1 + x_2 = 2(m - 1) \\ x_1 x_2 = 2m - 5 \end{cases}$$
Biến đổi hệ thức bài ra:  
$$(x_1 - x_2)^2 = 8 \iff (x_1 + x_2)^2 - 4x_1 x_2 = 8$$
Thay $x_1 + x_2$ và $x_1 x_2$ vào:  
$$[2(m - 1)]^2 - 4(2m - 5) = 8$$
$$\iff 4(m^2 - 2m + 1) - 8m + 20 = 8$$
$$\iff 4m^2 - 8m + 4 - 8m + 20 = 8$$
$$\iff 4m^2 - 16m + 16 = 0 \iff 4(m - 2)^2 = 0 \iff m = 2$$
Vậy $m = 2$ là giá trị duy nhất cần tìm.

---

### Bài 3 (2.0 điểm)
**Ý 1 (1.0 điểm):**  
Giải hệ phương trình:  
$$\begin{cases} 3x - 2y = 7 \\ 2x + 3y = 9 \end{cases} \iff \begin{cases} 9x - 6y = 21 \\ 4x + 6y = 18 \end{cases}$$
Cộng hai phương trình vế theo vế:  
$$13x = 39 \iff x = 3$$
Thay $x = 3$ vào phương trình $2x + 3y = 9$:  
$$2(3) + 3y = 9 \iff 6 + 3y = 9 \iff 3y = 3 \iff y = 1$$
Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (3; 1)$.

**Ý 2 (1.0 điểm):**  
Đổi $30\text{ phút} = \dfrac{1}{2}\text{ giờ}$.  
Gọi vận tốc của ô tô tải là $x$ ($\text{km/h}$, điều kiện: $x > 0$).  
Vận tốc của ô tô du lịch là $x + 20$ ($\text{km/h}$).  
Thời gian ô tô tải đi hết quãng đường $120\text{ km}$ là: $\dfrac{120}{x}$ (giờ).  
Thời gian ô tô du lịch đi hết quãng đường $120\text{ km}$ là: $\dfrac{120}{x + 20}$ (giờ).  
Vì ô tô du lịch đến sớm hơn ô tô tải $30$ phút nên ta có phương trình:  
$$\dfrac{120}{x} - \dfrac{120}{x + 20} = \dfrac{1}{2}$$
Quy đồng và khử mẫu:  
$$120 \cdot 2(x + 20) - 120 \cdot 2x = x(x + 20)$$
$$\iff 240x + 4800 - 240x = x^2 + 20x$$
$$\iff x^2 + 20x - 4800 = 0$$
Biệt thức: $\Delta' = 10^2 - 1 \cdot (-4800) = 100 + 4800 = 4900 > 0 \implies \sqrt{\Delta'} = 70$.  
Phương trình có hai nghiệm:  
$$x_1 = -10 + 70 = 60\text{ (thỏa mãn } x > 0)$$
$$x_2 = -10 - 70 = -80\text{ (loại)}$$
Vậy:  
- Vận tốc của xe tải là $60\text{ km/h}$.  
- Vận tốc của xe du lịch là $60 + 20 = 80\text{ km/h}$.

---

### Bài 4 (3.0 điểm)
**Ý 1 (1.0 điểm):**  
- Vì $BE \perp AC \implies \widehat{BEC} = 90^\circ$.  
- Vì $CF \perp AB \implies \widehat{BFC} = 90^\circ$.  
- Xét tứ giác $BCEF$, hai đỉnh $E$ và $F$ kề nhau cùng nhìn đoạn thẳng $BC$ dưới một góc vuông $90^\circ$.  
Do đó tứ giác $BCEF$ nội tiếp đường tròn đường kính $BC$.

**Ý 2 (1.0 điểm):**  
- Do $AK$ là đường kính của $(O)$ nên góc nội tiếp chắn nửa đường tròn $\widehat{ACK} = 90^\circ$.  
- Xét tam giác vuông $ABD$ (vuông tại $D$) và tam giác vuông $AKC$ (vuông tại $C$):  
  - $\widehat{ADB} = \widehat{ACK} = 90^\circ$  
  - $\widehat{ABD} = \widehat{AKC}$ (hai góc nội tiếp cùng chắn cung $\overparen{AC}$)  
  Suy ra $\triangle ABD \backsim \triangle AKC$ (g-g).  
- Suy ra tỉ số đồng dạng:  
  $$\dfrac{AB}{AK} = \dfrac{AD}{AC} \implies AB \cdot AC = AD \cdot AK$$
  Vì $AK = 2R$ nên $AB \cdot AC = 2R \cdot AD$ (đpcm).

**Ý 3 (1.0 điểm):**  
- Tứ giác $BHCK$ có:  
  - $BK \perp AB$ (góc nội tiếp chắn nửa đường tròn $\widehat{ABK} = 90^\circ$), mà $CH \perp AB$ (đường cao $CF$) $\implies BK \parallel CH$.  
  - $CK \perp AC$ (góc nội tiếp chắn nửa đường tròn $\widehat{ACK} = 90^\circ$), mà $BH \perp AC$ (đường cao $BE$) $\implies CK \parallel BH$.  
  Suy ra tứ giác $BHCK$ là hình bình hành.  
- Vì $BHCK$ là hình bình hành nên hai đường chéo cắt nhau tại trung điểm của mỗi đường. Mà $M$ là trung điểm của $BC \implies M$ cũng là trung điểm của $HK$.  
  Do đó ba điểm $H, M, K$ thẳng hàng.  
- Xét tam giác $AHK$:  
  - $O$ là trung điểm đường kính $AK$.  
  - $M$ là trung điểm đoạn thẳng $HK$.  
  Suy ra $OM$ là đường trung bình của tam giác $AHK \implies OM = \dfrac{1}{2}AH \implies AH = 2OM$ (đpcm).

---

### Bài 5 (1.0 điểm)
Cho $x, y > 0$ và $x + y = 2$. Tìm giá trị nhỏ nhất của $Q = \dfrac{1}{x^2 + y^2} + \dfrac{1}{xy}$.  
Ta có:  
$$Q = \dfrac{1}{x^2 + y^2} + \dfrac{1}{2xy} + \dfrac{1}{2xy}$$
Áp dụng bất đẳng thức cộng mẫu số $\dfrac{1}{a} + \dfrac{1}{b} \ge \dfrac{4}{a + b}$ với $a = x^2 + y^2 > 0$ và $b = 2xy > 0$:  
$$\dfrac{1}{x^2 + y^2} + \dfrac{1}{2xy} \ge \dfrac{4}{x^2 + y^2 + 2xy} = \dfrac{4}{(x + y)^2} = \dfrac{4}{2^2} = 1$$
Mặt khác, theo bất đẳng thức Cauchy:  
$$xy \le \left(\dfrac{x + y}{2}\right)^2 = \left(\dfrac{2}{2}\right)^2 = 1 \implies \dfrac{1}{2xy} \ge \dfrac{1}{2 \cdot 1} = \dfrac{1}{2}$$
Cộng hai bất đẳng thức cùng chiều:  
$$Q \ge 1 + \dfrac{1}{2} = \dfrac{3}{2}$$
Dấu đẳng thức xảy ra khi và chỉ khi:  
$$\begin{cases} x^2 + y^2 = 2xy \iff x = y \\ x + y = 2 \end{cases} \iff x = y = 1$$
Vậy giá trị nhỏ nhất của biểu thức $Q$ là $\dfrac{3}{2}$, đạt được khi $x = y = 1$.
"""

with open(os.path.join(MATH_DIR, "de_thi_tuyen_sinh_vao_10_toan_quang_ngai.md"), "w", encoding="utf-8") as f:
    f.write(de_thi_quang_ngai)
print("Created de_thi_tuyen_sinh_vao_10_toan_quang_ngai.md")

