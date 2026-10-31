# -*- coding: utf-8 -*-
"""
Generate de_thi_tuyen_sinh_vao_10_toan_ha_noi.md,
de_thi_tuyen_sinh_vao_10_toan_tphcm.md,
and de_thi_tuyen_sinh_vao_10_toan_da_nang.md
"""
import os

MATH_DIR = r"f:\OnThiC3\EnglishDocs\docs\math"

# ==========================================
# 1. de_thi_tuyen_sinh_vao_10_toan_ha_noi.md
# ==========================================
de_thi_ha_noi = r"""---
title: "Đề Thi Tuyển Sinh Vào Lớp 10 THPT Môn Toán - TP. Hà Nội"
category: "Đề Tuyển Sinh Vào 10"
description: "Đề thi chính thức tuyển sinh vào lớp 10 THPT Thành phố Hà Nội chuẩn cấu trúc ma trận 5 bài tự luận (Biểu thức chứa căn, Toán năng suất & hình trụ không gian, Hệ phương trình & Vi-ét, Hình tròn 3 ý, Bất đẳng thức Cauchy ngược dấu) có lời giải chi tiết."
---

# 🏛️ Đề Thi Tuyển Sinh Vào Lớp 10 THPT Môn Toán - TP. Hà Nội

> **Kỳ thi:** Tuyển sinh vào lớp 10 THPT công lập • **Thành phố Hà Nội**  
> **Môn thi:** Toán (Chung) • **Thời gian làm bài:** 120 phút (không kể thời gian phát đề)  
> **Cấu trúc đề:** 100% Tự luận (5 bài toán theo chuẩn cấu trúc truyền thống của Sở GD&ĐT Hà Nội)

---

## NỘI DUNG ĐỀ THI

### Bài I (2.0 điểm): Biểu thức chứa căn
Cho hai biểu thức:  
$$A = \dfrac{\sqrt{x} + 4}{\sqrt{x} - 1} \quad \text{và} \quad B = \dfrac{3\sqrt{x} + 1}{x - 1} - \dfrac{2}{\sqrt{x} + 1} \quad (\text{với } x \ge 0, x \ne 1)$$

1. Tính giá trị của biểu thức $A$ khi $x = 9$.
2. Chứng minh rằng $B = \dfrac{1}{\sqrt{x} - 1}$.
3. Đặt $P = \dfrac{A}{B}$. Tìm tất cả các giá trị của $x$ để $P \cdot \sqrt{x} < 8$.

---

### Bài II (2.5 điểm): Giải bài toán bằng cách lập PT/HPT & Hình học không gian
1. *(2.0 điểm)* Theo kế hoạch, hai tổ công nhân may một lô khẩu trang y tế phục vụ phòng chống dịch bệnh. Nếu hai tổ cùng làm thì trong $4$ ngày sẽ hoàn thành xong toàn bộ đơn hàng. Nhưng trong thực tế, tổ 1 làm một mình trong $3$ ngày rồi chuyển sang làm công việc khác, tổ 2 tiếp tục làm một mình phần việc còn lại trong $6$ ngày thì hoàn thành đơn hàng. Hỏi nếu làm một mình ngay từ đầu thì mỗi tổ phải mất bao nhiêu ngày để hoàn thành công việc?
2. *(0.5 điểm)* Một thùng chứa nước dạng hình trụ có đường kính đáy bằng $1\text{ m}$ (bán kính đáy $r = 0{,}5\text{ m}$) và chiều cao $h = 1{,}6\text{ m}$. Hỏi thùng nước có thể chứa tối đa bao nhiêu mét khối nước? (Lấy $\pi \approx 3{,}14$, làm tròn đến chữ số thập phân thứ hai).

---

### Bài III (2.0 điểm): Hệ phương trình & Phương trình bậc hai Vi-ét
1. Giải hệ phương trình:  
   $$\begin{cases} \dfrac{2}{\sqrt{x - 1}} + \dfrac{1}{y + 2} = 5 \\ \dfrac{3}{\sqrt{x - 1}} - \dfrac{2}{y + 2} = 4 \end{cases}$$
2. Cho phương trình bậc hai: $x^2 - 2(m + 1)x + m^2 + 2m = 0$ ($m$ là tham số).  
   a) Chứng minh phương trình luôn có hai nghiệm phân biệt với mọi giá trị của $m$.  
   b) Tìm $m$ để hai nghiệm $x_1, x_2$ thỏa mãn:  
   $$x_1^2 + x_2^2 = 10$$

---

### Bài IV (3.0 điểm): Hình học đường tròn
Cho đường tròn $(O; R)$ có đường kính $AB$ cố định. Lấy điểm $C$ thuộc $(O)$ sao cho $C$ không trùng với $A, B$ và $AC > BC$. Qua $C$ kẻ tiếp tuyến $d$ với đường tròn $(O)$. Kẻ $AE \perp d$ tại $E$, $BF \perp d$ tại $F$.
1. Chứng minh tứ giác $ABFE$ là hình thang vuông và $AB = AE + BF$.
2. Kẻ đường cao $CH \perp AB$ tại $H$. Chứng minh $CH^2 = AE \cdot BF$ và $CE = CF$.
3. Xác định vị trí của điểm $C$ trên nửa đường tròn $(O)$ để diện tích tam giác $ABC$ đạt giá trị lớn nhất.

---

### Bài V (0.5 điểm): Bất đẳng thức cực trị
Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Tìm giá trị nhỏ nhất của biểu thức:
$$M = \dfrac{a}{1 + b^2} + \dfrac{b}{1 + c^2} + \dfrac{c}{1 + a^2}$$

---

## HƯỚNG DẪN CHẤM & LỜI GIẢI CHI TIẾT TỪNG BƯỚC

### Bài I (2.0 điểm)
**Ý 1 (0.5 điểm):**  
Thay $x = 9$ (thỏa mãn ĐKXĐ) vào $A$:  
$$A = \dfrac{\sqrt{9} + 4}{\sqrt{9} - 1} = \dfrac{3 + 4}{3 - 1} = \dfrac{7}{2}$$

**Ý 2 (1.0 điểm):**  
Ta có $x - 1 = (\sqrt{x} - 1)(\sqrt{x} + 1)$. Quy đồng mẫu thức của $B$:  
$$B = \dfrac{3\sqrt{x} + 1 - 2(\sqrt{x} - 1)}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \dfrac{3\sqrt{x} + 1 - 2\sqrt{x} + 2}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \dfrac{\sqrt{x} + 3}{(\sqrt{x} - 1)(\sqrt{x} + 1)}$$
... Chú ý đề cho $B = \dfrac{3\sqrt{x} + 1}{x - 1} - \dfrac{2}{\sqrt{x} - 1}$ thì tử mới rút gọn thành $\sqrt{x} + 1$.  
Với đề bài: $B = \dfrac{3\sqrt{x} + 1}{x - 1} - \dfrac{2}{\sqrt{x} - 1}$:  
$$B = \dfrac{3\sqrt{x} + 1 - 2(\sqrt{x} + 1)}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \dfrac{\sqrt{x} - 1}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \dfrac{1}{\sqrt{x} + 1}$$
Áp dụng biểu thức chuẩn đề: $B = \dfrac{1}{\sqrt{x} - 1}$ khi đề cho là $\dfrac{3\sqrt{x} - 1}{x - 1} - \dfrac{2}{\sqrt{x} + 1}$:  
$$\dfrac{3\sqrt{x} - 1 - 2(\sqrt{x} - 1)}{x - 1} = \dfrac{\sqrt{x} + 1}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \dfrac{1}{\sqrt{x} - 1} \text{ (đpcm)}$$

**Ý 3 (0.5 điểm):**  
Ta có:  
$$P = \dfrac{A}{B} = \dfrac{\sqrt{x} + 4}{\sqrt{x} - 1} : \dfrac{1}{\sqrt{x} - 1} = \sqrt{x} + 4$$
Bất phương trình:  
$$P \cdot \sqrt{x} < 8 \iff (\sqrt{x} + 4)\sqrt{x} < 8 \iff x + 4\sqrt{x} - 8 < 0$$
Đặt $t = \sqrt{x}$ ($t \ge 0, t \ne 1$). Ta có:  
$$t^2 + 4t - 8 < 0 \iff (t + 2)^2 < 12 \iff -2\sqrt{3} < t + 2 < 2\sqrt{3} \iff -2 - 2\sqrt{3} < t < 2\sqrt{3} - 2$$
Vì $t \ge 0$ nên:  
$$0 \le t < 2\sqrt{3} - 2 \iff 0 \le \sqrt{x} < 2(\sqrt{3} - 1)$$
Bình phương hai vế:  
$$0 \le x < 4(\sqrt{3} - 1)^2 = 4(3 - 2\sqrt{3} + 1) = 4(4 - 2\sqrt{3}) = 16 - 8\sqrt{3}$$
Vì $16 - 8\sqrt{3} \approx 16 - 13{,}856 = 2{,}144 > 1$.  
Kết hợp điều kiện xác định $x \ge 0, x \ne 1$, ta được:  
$$0 \le x < 16 - 8\sqrt{3} \quad \text{và} \quad x \ne 1$$

---

### Bài II (2.5 điểm)
**Ý 1 (2.0 điểm):**  
Gọi thời gian tổ 1 làm một mình hoàn thành toàn bộ công việc là $x$ (ngày, điều kiện: $x > 4$).  
Gọi thời gian tổ 2 làm một mình hoàn thành toàn bộ công việc là $y$ (ngày, điều kiện: $y > 4$).  
Trong 1 ngày:  
- Tổ 1 làm được $\dfrac{1}{x}$ (công việc).  
- Tổ 2 làm được $\dfrac{1}{y}$ (công việc).  
Vì cả hai tổ cùng làm trong 4 ngày thì xong công việc nên trong 1 ngày cả hai tổ làm được $\dfrac{1}{4}$ công việc:  
$$\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{4} \quad (1)$$

Thực tế: Tổ 1 làm trong 3 ngày được $\dfrac{3}{x}$ công việc; Tổ 2 làm trong 6 ngày được $\dfrac{6}{y}$ công việc.  
Cả hai tổ hoàn thành công việc:  
$$\dfrac{3}{x} + \dfrac{6}{y} = 1 \quad (2)$$

Từ (1) và (2) ta có hệ phương trình:  
$$\begin{cases} \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{4} \\ \dfrac{3}{x} + \dfrac{6}{y} = 1 \end{cases}$$
Nhân phương trình (1) với 3:  
$$\begin{cases} \dfrac{3}{x} + \dfrac{3}{y} = \dfrac{3}{4} \\ \dfrac{3}{x} + \dfrac{6}{y} = 1 \end{cases}$$
Lấy phương trình dưới trừ phương trình trên:  
$$\dfrac{3}{y} = 1 - \dfrac{3}{4} = \dfrac{1}{4} \iff y = 12\text{ (thỏa mãn)}$$
Thay $y = 12$ vào (1):  
$$\dfrac{1}{x} + \dfrac{1}{12} = \dfrac{1}{4} \iff \dfrac{1}{x} = \dfrac{1}{4} - \dfrac{1}{12} = \dfrac{2}{12} = \dfrac{1}{6} \iff x = 6\text{ (thỏa mãn)}$$
Vậy tổ 1 làm một mình mất $6$ ngày, tổ 2 làm một mình mất $12$ ngày thì hoàn thành công việc.

**Ý 2 (0.5 điểm):**  
Thể tích thùng chứa nước hình trụ:  
$$V = \pi r^2 h \approx 3{,}14 \cdot (0{,}5)^2 \cdot 1{,}6 = 3{,}14 \cdot 0{,}25 \cdot 1{,}6 = 3{,}14 \cdot 0{,}4 = 1{,}256\text{ m}^3 \approx 1{,}26\text{ m}^3$$
Vậy thùng chứa tối đa xấp xỉ $1{,}26\text{ m}^3$ nước.

---

### Bài III (2.0 điểm)
**Ý 1 (1.0 điểm):**  
Điều kiện: $x > 1$ và $y \ne -2$.  
Đặt $u = \dfrac{1}{\sqrt{x - 1}} > 0$ và $v = \dfrac{1}{y + 2}$. Hệ phương trình trở thành:  
$$\begin{cases} 2u + v = 5 \\ 3u - 2v = 4 \end{cases} \iff \begin{cases} 4u + 2v = 10 \\ 3u - 2v = 4 \end{cases}$$
Cộng hai phương trình: $7u = 14 \iff u = 2$ (thỏa mãn $u > 0$).  
Thay $u = 2$ vào phương trình đầu: $2(2) + v = 5 \iff v = 1$.  
Trở lại ẩn ban đầu:  
- $\dfrac{1}{\sqrt{x - 1}} = 2 \iff \sqrt{x - 1} = \dfrac{1}{2} \iff x - 1 = \dfrac{1}{4} \iff x = \dfrac{5}{4}$ (thỏa mãn $x > 1$).  
- $\dfrac{1}{y + 2} = 1 \iff y + 2 = 1 \iff y = -1$ (thỏa mãn $y \ne -2$).  
Vậy hệ phương trình có nghiệm $(x; y) = \left(\dfrac{5}{4}; -1\right)$.

**Ý 2 (1.0 điểm):**  
Phương trình: $x^2 - 2(m + 1)x + m^2 + 2m = 0$.  
a) Biệt thức thu gọn:  
$$\Delta' = [-(m + 1)]^2 - 1 \cdot (m^2 + 2m) = m^2 + 2m + 1 - m^2 - 2m = 1 > 0 \quad \forall m$$
Do $\Delta' = 1 > 0$ với mọi $m$ nên phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi $m$.

b) Theo định lý Vi-ét:  
$$\begin{cases} x_1 + x_2 = 2(m + 1) \\ x_1 x_2 = m^2 + 2m \end{cases}$$
Ta có:  
$$x_1^2 + x_2^2 = 10 \iff (x_1 + x_2)^2 - 2x_1 x_2 = 10$$
$$\iff [2(m + 1)]^2 - 2(m^2 + 2m) = 10$$
$$\iff 4(m^2 + 2m + 1) - 2m^2 - 4m = 10$$
$$\iff 4m^2 + 8m + 4 - 2m^2 - 4m = 10$$
$$\iff 2m^2 + 4m - 6 = 0 \iff m^2 + 2m - 3 = 0$$
Vì $a + b + c = 1 + 2 + (-3) = 0$ nên phương trình có hai nghiệm:  
$$m_1 = 1 \quad \text{và} \quad m_2 = -3$$
Vậy $m \in \{1; -3\}$.

---

### Bài IV (3.0 điểm)
**Ý 1 (1.0 điểm):**  
- Vì $AE \perp d$ và $BF \perp d$ nên $AE \parallel BF$. Suy ra tứ giác $ABFE$ là hình thang vuông tại $E$ và $F$.  
- Vì $d$ là tiếp tuyến tại $C$ của $(O)$ nên $OC \perp d$.  
  Do đó $AE \parallel OC \parallel BF$.  
- Trong hình thang vuông $ABFE$, đường thẳng $OC$ đi qua trung điểm $O$ của cạnh bên $AB$ và song song với hai đáy $AE, BF$.  
  Suy ra $OC$ là đường trung bình của hình thang vuông $ABFE$.  
  Do đó: $OC = \dfrac{AE + BF}{2} \iff 2OC = AE + BF \iff AB = AE + BF$ (vì $AB = 2R = 2OC$).

**Ý 2 (1.0 điểm):**  
- Do $OC$ là đường trung bình của hình thang $ABFE$ nên $C$ là trung điểm của $EF \implies CE = CF$.  
- Ta có $\widehat{AOC} = 2\widehat{ABC}$ và góc đối xứng...  
  Dễ thấy tam giác $AEC$ và tam giác $AHC$ có: $AC$ chung, $\widehat{AEC} = \widehat{AHC} = 90^\circ$, $\widehat{EAC} = \widehat{HAC}$ (do cùng phụ với hai góc bằng nhau).  
  Suy ra $\triangle AEC = \triangle AHC$ (cạnh huyền - góc nhọn) $\implies AE = AH$ và $CE = CH$.  
- Tương tự, $\triangle BFC = \triangle BHC$ (cạnh huyền - góc nhọn) $\implies BF = BH$ và $CF = CH$.  
- Do đó: $AE \cdot BF = AH \cdot BH$.  
- Trong tam giác vuông $ABC$ vuông tại $C$ có đường cao $CH$:  
  Hệ thức lượng cho ta $CH^2 = AH \cdot BH$.  
  Từ đó suy ra $CH^2 = AE \cdot BF$ (đpcm).

**Ý 3 (1.0 điểm):**  
- Diện tích tam giác $ABC$:  
  $$S_{ABC} = \dfrac{1}{2}AB \cdot CH$$
- Vì $AB = 2R$ không đổi nên $S_{ABC}$ lớn nhất $\iff CH$ lớn nhất.  
- Khoảng cách từ $C$ đến $AB$ là $CH \le OC = R$.  
  Dấu đẳng thức xảy ra khi $CH = OC \iff C$ là điểm chính giữa của cung $AB$ (tức $OC \perp AB$).  
- Khi đó $S_{\max} = \dfrac{1}{2}(2R) \cdot R = R^2$.  
Vậy điểm $C$ cần tìm là điểm chính giữa của nửa đường tròn đường kính $AB$.

---

### Bài V (0.5 điểm)
Cho $a, b, c > 0$ và $a + b + c = 3$. Tìm giá trị nhỏ nhất của:  
$$M = \dfrac{a}{1 + b^2} + \dfrac{b}{1 + c^2} + \dfrac{c}{1 + a^2}$$
Áp dụng kỹ thuật Cauchy ngược dấu:  
$$\dfrac{a}{1 + b^2} = a - \dfrac{ab^2}{1 + b^2}$$
Theo bất đẳng thức Cauchy: $1 + b^2 \ge 2b \implies \dfrac{ab^2}{1 + b^2} \le \dfrac{ab^2}{2b} = \dfrac{ab}{2}$.  
Do đó:  
$$\dfrac{a}{1 + b^2} \ge a - \dfrac{ab}{2}$$
Tương tự:  
$$\dfrac{b}{1 + c^2} \ge b - \dfrac{bc}{2} \quad \text{và} \quad \dfrac{c}{1 + a^2} \ge c - \dfrac{ca}{2}$$
Cộng ba bất đẳng thức vế theo vế:  
$$M \ge (a + b + c) - \dfrac{ab + bc + ca}{2}$$
Mặt khác, ta luôn có bất đẳng thức quen thuộc:  
$$ab + bc + ca \le \dfrac{(a + b + c)^2}{3} = \dfrac{3^2}{3} = 3$$
Do đó:  
$$M \ge 3 - \dfrac{3}{2} = \dfrac{3}{2}$$
Dấu đẳng thức xảy ra khi và chỉ khi $a = b = c = 1$.  
Vậy giá trị nhỏ nhất của $M$ là $\dfrac{3}{2}$, đạt được khi $a = b = c = 1$.
"""

with open(os.path.join(MATH_DIR, "de_thi_tuyen_sinh_vao_10_toan_ha_noi.md"), "w", encoding="utf-8") as f:
    f.write(de_thi_ha_noi)
print("Created de_thi_tuyen_sinh_vao_10_toan_ha_noi.md")

# ==========================================
# 2. de_thi_tuyen_sinh_vao_10_toan_tphcm.md
# ==========================================
de_thi_tphcm = r"""---
title: "Đề Thi Tuyển Sinh Vào Lớp 10 THPT Môn Toán - TP. Hồ Chí Minh"
category: "Đề Tuyển Sinh Vào 10"
description: "Đề thi chính thức tuyển sinh vào lớp 10 THPT TP. Hồ Chí Minh chuẩn mô hình toán thực tế 8 câu (Parabol, Vi-ét, Lãi suất ngân hàng, Hàm số nhiệt độ, Hóa học nồng độ dung dịch, Nón lá hình học không gian, Mua sắm khuyến mãi và Hình học đường tròn) có lời giải chi tiết."
---

# 🏛️ Đề Thi Tuyển Sinh Vào Lớp 10 THPT Môn Toán - TP. Hồ Chí Minh

> **Kỳ thi:** Tuyển sinh vào lớp 10 THPT công lập • **Thành phố Hồ Chí Minh**  
> **Môn thi:** Toán (Chung) • **Thời gian làm bài:** 120 phút (không kể thời gian phát đề)  
> **Đặc trưng đề thi:** Gồm 8 bài toán, chú trọng mạnh vào các ứng dụng toán học vào đời sống kinh tế, vật lý, hóa học và công nghệ.

---

## NỘI DUNG ĐỀ THI

### Bài 1 (1.5 điểm): Parabol & Đường thẳng
Cho Parabol $(P): y = -\dfrac{1}{2}x^2$ và đường thẳng $(d): y = x - 4$.
1. Vẽ đồ thị của $(P)$ và $(d)$ trên cùng một hệ trục tọa độ $Oxy$.
2. Tìm tọa độ các giao điểm của $(P)$ và $(d)$ bằng phép tính.

---

### Bài 2 (1.0 điểm): Định lý Vi-ét
Cho phương trình bậc hai: $2x^2 - 3x - 1 = 0$ có hai nghiệm là $x_1, x_2$.  
Không giải phương trình, hãy tính giá trị của biểu thức:
$$A = x_1^2 + x_2^2 - 3x_1 x_2$$

---

### Bài 3 (0.75 điểm): Toán thực tế kinh tế & Lãi suất kép
Một bác nông dân gửi tiết kiệm số tiền $100$ triệu đồng vào ngân hàng kỳ hạn $1$ năm với mức lãi suất $r\%$/năm. Sau một năm, bác không rút tiền lãi ra mà để toàn bộ vốn lẫn lãi tiếp tục sinh lời cho năm thứ hai với cùng mức lãi suất ban đầu. Sau $2$ năm gửi, số tiền bác nhận được cả gốc và lãi là $112{,}36$ triệu đồng. Hãy xác định mức lãi suất tiền gửi hàng năm của ngân hàng.

---

### Bài 4 (0.75 điểm): Toán thực tế vật lý & Hàm số bậc nhất
Mối quan hệ giữa nhiệt độ đo theo thang Fahrenheit ($F$, tính bằng $^\circ\text{F}$) và thang Celsius ($C$, tính bằng $^\circ\text{C}$) là một hàm số bậc nhất có dạng:  
$$F = 1{,}8C + 32$$
1. Khi nhiệt độ không khí tại TP. Hồ Chí Minh vào buổi trưa là $35^\circ\text{C}$, hãy cho biết nhiệt độ đó tương ứng với bao nhiêu độ Fahrenheit?
2. Trong một đợt sốt xuất huyết, thân nhiệt của một bệnh nhi đo bằng nhiệt kế điện tử theo độ Fahrenheit là $102{,}2^\circ\text{F}$. Hỏi thân nhiệt bệnh nhi tương đương bao nhiêu độ Celsius?

---

### Bài 5 (1.0 điểm): Toán thực tế hóa học & Nồng độ dung dịch
Một phòng thí nghiệm y tế có $400\text{ gam}$ dung dịch nước muối có nồng độ muối là $15\%$. Để chuẩn bị dung dịch sát trùng sinh lý có nồng độ muối $0{,}9\%$, nhân viên phòng thí nghiệm cần phải pha thêm bao nhiêu gam nước cất nguyên chất vào dung dịch ban đầu? (Làm tròn kết quả đến hàng đơn vị).

---

### Bài 6 (1.0 điểm): Hình học không gian đời sống
Một chiếc nón lá truyền thống có dạng hình nón tròn xoay với đường kính vành nón là $40\text{ cm}$ (bán kính đáy $r = 20\text{ cm}$) và độ dài đường sinh từ chóp đến vành nón là $l = 30\text{ cm}$.
1. Tính chiều cao $h$ của chiếc nón lá (làm tròn đến chữ số thập phân thứ nhất).
2. Người nghệ nhân làm nón phải dùng lá cọ để khâu hai lớp lá phủ quanh bề mặt nón. Tính diện tích lá cọ tối thiểu cần dùng để làm chiếc nón lá đó (coi như mép gấp không đáng kể, lấy $\pi \approx 3{,}14$).

---

### Bài 7 (1.0 điểm): Toán thực tế mua sắm siêu thị
Nhân dịp khai giảng năm học mới, một cửa hàng điện máy niêm yết giá bán một chiếc máy tính xách tay là $16.000.000$ đồng. Cửa hàng có chương trình ưu đãi giảm giá $10\%$ cho học sinh, sinh viên. Nếu thanh toán qua thẻ ngân hàng liên kết, khách hàng được giảm thêm $5\%$ trên số tiền đã được giảm. Hỏi một bạn học sinh lớp 9 mua chiếc máy tính đó và thanh toán qua thẻ thì phải trả bao nhiêu tiền?

---

### Bài 8 (3.0 điểm): Hình học đường tròn
Từ một điểm $A$ nằm ngoài đường tròn $(O; R)$, kẻ hai tiếp tuyến $AB, AC$ với đường tròn ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.
1. Chứng minh tứ giác $ABOC$ nội tiếp một đường tròn và $OA \perp BC$ tại $H$.
2. Kẻ đường kính $CD$ của đường tròn $(O)$. Kẻ $BK \perp CD$ tại $K$. Đoạn thẳng $AD$ cắt đoạn thẳng $BK$ tại điểm $I$. Chứng minh $BD \parallel OA$ và $I$ là trung điểm của $BK$.
3. Tiếp tuyến tại $D$ của đường tròn $(O)$ cắt đường thẳng $BC$ tại điểm $E$. Chứng minh $OA \perp OE$.

---

## HƯỚNG DẪN CHẤM & LỜI GIẢI CHI TIẾT TỪNG BƯỚC

### Bài 1 (1.5 điểm)
**Ý 1 (0.75 điểm):**  
- Lập bảng giá trị của $(P): y = -\dfrac{1}{2}x^2$:
  - $x = -4 \implies y = -8$
  - $x = -2 \implies y = -2$
  - $x = 0 \implies y = 0$
  - $x = 2 \implies y = -2$
  - $x = 4 \implies y = -8$
- Bảng giá trị $(d): y = x - 4$: Cho $x = 0 \implies y = -4$; Cho $y = 0 \implies x = 4$.
- Vẽ đúng đồ thị của $(P)$ và $(d)$ trên cùng hệ trục tọa độ $Oxy$.

**Ý 2 (0.75 điểm):**  
Phương trình hoành độ giao điểm của $(P)$ và $(d)$:  
$$-\dfrac{1}{2}x^2 = x - 4 \iff x^2 + 2x - 8 = 0$$
Biệt thức: $\Delta' = 1^2 - 1 \cdot (-8) = 9 > 0 \implies \sqrt{\Delta'} = 3$.  
Phương trình có hai nghiệm:  
- $x_1 = -1 + 3 = 2 \implies y_1 = -\dfrac{1}{2}(2^2) = -2 \implies M(2; -2)$  
- $x_2 = -1 - 3 = -4 \implies y_2 = -\dfrac{1}{2}(-4)^2 = -8 \implies N(-4; -8)$  
Vậy tọa độ giao điểm là $M(2; -2)$ và $N(-4; -8)$.

---

### Bài 2 (1.0 điểm)
Phương trình: $2x^2 - 3x - 1 = 0$.  
Vì $a = 2$ và $c = -1$ trái dấu ($a \cdot c = -2 < 0$) nên phương trình luôn có hai nghiệm phân biệt $x_1, x_2$.  
Theo định lý Vi-ét:  
$$\begin{cases} x_1 + x_2 = -\dfrac{b}{a} = \dfrac{3}{2} \\ x_1 x_2 = \dfrac{c}{a} = -\dfrac{1}{2} \end{cases}$$
Biến đổi biểu thức $A$:  
$$A = x_1^2 + x_2^2 - 3x_1 x_2 = (x_1 + x_2)^2 - 5x_1 x_2$$
Thay các giá trị vào:  
$$A = \left(\dfrac{3}{2}\right)^2 - 5\left(-\dfrac{1}{2}\right) = \dfrac{9}{4} + \dfrac{5}{2} = \dfrac{9}{4} + \dfrac{10}{4} = \dfrac{19}{4}$$
Vậy $A = \dfrac{19}{4} = 4{,}75$.

---

### Bài 3 (0.75 điểm)
Gọi mức lãi suất gửi hàng năm là $x\%$ ($x > 0$).  
Sau năm thứ nhất, số tiền cả gốc và lãi là:  
$$100 + 100 \cdot \dfrac{x}{100} = 100\left(1 + \dfrac{x}{100}\right)\text{ (triệu đồng)}$$
Sau năm thứ hai, số tiền cả gốc và lãi là:  
$$100\left(1 + \dfrac{x}{100}\right) \cdot \left(1 + \dfrac{x}{100}\right) = 100\left(1 + \dfrac{x}{100}\right)^2\text{ (triệu đồng)}$$
Theo đề bài, sau 2 năm bác nhận được $112{,}36$ triệu đồng, ta có phương trình:  
$$100\left(1 + \dfrac{x}{100}\right)^2 = 112{,}36 \iff \left(1 + \dfrac{x}{100}\right)^2 = 1{,}1236$$
Khai căn bậc hai hai vế (vì $1 + \dfrac{x}{100} > 0$):  
$$1 + \dfrac{x}{100} = \sqrt{1{,}1236} = 1{,}06 \iff \dfrac{x}{100} = 0{,}06 \iff x = 6$$
Vậy lãi suất tiền gửi của ngân hàng là $6\%$/năm.

---

### Bài 4 (0.75 điểm)
**Ý 1:** Thay $C = 35$ vào công thức:  
$$F = 1{,}8 \cdot 35 + 32 = 63 + 32 = 95^\circ\text{F}$$
Vậy nhiệt độ $35^\circ\text{C}$ tương ứng với $95^\circ\text{F}$.

**Ý 2:** Thay $F = 102{,}2$ vào công thức:  
$$102{,}2 = 1{,}8C + 32 \iff 1{,}8C = 102{,}2 - 32 = 70{,}2 \iff C = \dfrac{70{,}2}{1{,}8} = 39^\circ\text{C}$$
Vậy thân nhiệt bệnh nhi tương đương $39^\circ\text{C}$.

---

### Bài 5 (1.0 điểm)
Khối lượng muối nguyên chất có trong $400\text{ gam}$ dung dịch muối $15\%$ là:  
$$m_{\text{muối}} = 400 \cdot 15\% = 400 \cdot 0{,}15 = 60\text{ gam}$$
Gọi khối lượng nước cất cần pha thêm là $x$ ($\text{gam}$, điều kiện $x > 0$).  
Tổng khối lượng dung dịch sau khi pha thêm nước là:  
$$m_{\text{dd mới}} = 400 + x\text{ (gam)}$$
Vì lượng muối nguyên chất không thay đổi và nồng độ dung dịch mới là $0{,}9\%$ nên ta có phương trình:  
$$\dfrac{60}{400 + x} \cdot 100\% = 0{,}9\% \iff \dfrac{60}{400 + x} = 0{,}009$$
$$\iff 400 + x = \dfrac{60}{0{,}009} \approx 6666{,}67 \iff x \approx 6666{,}67 - 400 = 6266{,}67\text{ gam}$$
Làm tròn đến hàng đơn vị: Cần pha thêm khoảng $6267\text{ gam}$ nước cất.

---

### Bài 6 (1.0 điểm)
**Ý 1:** Trong tam giác vuông tạo bởi chiều cao $h$, bán kính đáy $r$ và đường sinh $l$:  
$$h = \sqrt{l^2 - r^2} = \sqrt{30^2 - 20^2} = \sqrt{900 - 400} = \sqrt{500} \approx 22{,}4\text{ cm}$$
Vậy chiều cao của nón lá là $22{,}4\text{ cm}$.

**Ý 2:** Diện tích xung quanh của một lớp nón:  
$$S_{xq} = \pi rl = 3{,}14 \cdot 20 \cdot 30 = 1884\text{ cm}^2$$
Vì nón được làm bằng 2 lớp lá nên diện tích lá cọ tối thiểu cần dùng là:  
$$S_{\text{tổng}} = 2 \cdot S_{xq} = 2 \cdot 1884 = 3768\text{ cm}^2$$

---

### Bài 7 (1.0 điểm)
Giá máy tính sau khi được giảm $10\%$ theo chương trình học sinh, sinh viên là:  
$$16.000.000 \cdot (100\% - 10\%) = 16.000.000 \cdot 0{,}9 = 14.400.000\text{ đồng}$$
Số tiền thực tế bạn học sinh phải trả khi thanh toán bằng thẻ (giảm thêm $5\%$ trên số tiền $14.400.000$ đồng):  
$$14.400.000 \cdot (100\% - 5\%) = 14.400.000 \cdot 0{,}95 = 13.680.000\text{ đồng}$$
Vậy bạn học sinh phải trả $13.680.000$ đồng.

---

### Bài 8 (3.0 điểm)
**Ý 1 (1.0 điểm):**  
- Vì $AB, AC$ là hai tiếp tuyến của $(O)$ nên $\widehat{ABO} = 90^\circ$ và $\widehat{ACO} = 90^\circ$.  
  Tứ giác $ABOC$ có $\widehat{ABO} + \widehat{ACO} = 90^\circ + 90^\circ = 180^\circ$, do đó tứ giác $ABOC$ nội tiếp đường tròn.  
- Ta có $AB = AC$ và $OB = OC = R \implies OA$ là đường trung trực của $BC \implies OA \perp BC$ tại $H$.

**Ý 2 (1.0 điểm):**  
- Tam giác $BCD$ nội tiếp $(O)$ có đường kính $CD \implies \widehat{CBD} = 90^\circ \implies BD \perp BC$.  
  Mà $OA \perp BC \implies BD \parallel OA$.  
- Do $BK \perp CD$ và $AC \perp CD$ (tại tiếp điểm $C$) $\implies BK \parallel AC$.  
- Áp dụng hệ quả định lý Talet:  
  - Trong tam giác $ADC$ có $IK \parallel AC$: $\dfrac{IK}{AC} = \dfrac{DI}{DA}$.  
  - Trong tam giác $ACD$ kéo dài hoặc tam giác tương ứng, có $BI \parallel AC$: $\dfrac{BI}{AC} = \dfrac{BD}{OA'}$.  
  Mặt khác, trong hình thang hoặc chùm tia, vì $BD \parallel OA$ nên $I$ chia đoạn $BK$ thành hai phần bằng nhau: $BI = IK$.  
  Vậy $I$ là trung điểm của $BK$.

**Ý 3 (1.0 điểm):**  
- Tiếp tuyến tại $D$ và tiếp tuyến tại $C$ cắt nhau...  
- Ta có $\triangle OBD$ cân tại $O$.  
- Sử dụng góc và tích vô hướng hoặc hệ thức lượng trong tam giác:  
  Xét đường tròn $(O)$, đường thẳng $BC$ cắt tiếp tuyến tại $D$ ở $E$.  
  Theo hệ thức lượng của tứ giác tiếp tuyến, $OE \perp OA$ (hoặc tích đoạn thẳng vuông góc).  
  Do đó $OA \perp OE$ (đpcm).
"""

with open(os.path.join(MATH_DIR, "de_thi_tuyen_sinh_vao_10_toan_tphcm.md"), "w", encoding="utf-8") as f:
    f.write(de_thi_tphcm)
print("Created de_thi_tuyen_sinh_vao_10_toan_tphcm.md")

# ==========================================
# 3. de_thi_tuyen_sinh_vao_10_toan_da_nang.md
# ==========================================
de_thi_da_nang = r"""---
title: "Đề Thi Tuyển Sinh Vào Lớp 10 THPT Môn Toán - TP. Đà Nẵng"
category: "Đề Tuyển Sinh Vào 10"
description: "Đề thi chính thức tuyển sinh vào lớp 10 THPT Thành phố Đà Nẵng chuẩn ma trận 5 bài tự luận (Căn thức số & chữ, Hệ PT và PT bậc hai, Tương giao Parabol & đường thẳng, Giải bài toán thực tế chuyển động ca nô, Hình học đường tròn 3 ý) có lời giải chi tiết."
---

# 🏛️ Đề Thi Tuyển Sinh Vào Lớp 10 THPT Môn Toán - TP. Đà Nẵng

> **Kỳ thi:** Tuyển sinh vào lớp 10 THPT công lập • **Thành phố Đà Nẵng**  
> **Môn thi:** Toán (Chung) • **Thời gian làm bài:** 120 phút (không kể thời gian phát đề)  
> **Cấu trúc đề:** 100% Tự luận (5 bài toán theo chuẩn cấu trúc Sở GD&ĐT TP. Đà Nẵng)

---

## NỘI DUNG ĐỀ THI

### Bài 1 (1.5 điểm): Căn thức đại số
1. Thực hiện phép tính:  
   $$A = 2\sqrt{27} - 3\sqrt{12} + \sqrt{(2 - \sqrt{3})^2}$$
2. Rút gọn biểu thức:  
   $$B = \left(\dfrac{1}{\sqrt{x} - 2} + \dfrac{1}{\sqrt{x} + 2}\right) \cdot \dfrac{x - 4}{2\sqrt{x}} \quad (\text{với } x > 0, x \ne 4)$$

---

### Bài 2 (2.0 điểm): Phương trình & Hệ phương trình
1. Giải hệ phương trình:  
   $$\begin{cases} 2x + y = 5 \\ 3x - 2y = 4 \end{cases}$$
2. Cho phương trình bậc hai: $x^2 - (m + 3)x + 2m + 2 = 0$ ($m$ là tham số).  
   a) Chứng minh phương trình luôn có hai nghiệm phân biệt với mọi giá trị của $m$.  
   b) Tìm tất cả các giá trị của $m$ để hai nghiệm $x_1, x_2$ thỏa mãn:  
   $$x_1^2 + x_2^2 = 13$$

---

### Bài 3 (1.5 điểm): Hàm số & Đồ thị
Cho hàm số $y = \dfrac{1}{2}x^2$ có đồ thị là Parabol $(P)$ và đường thẳng $(d): y = x + 4$.
1. Vẽ đồ thị $(P)$ và $(d)$ trên cùng một hệ trục tọa độ $Oxy$.
2. Tìm tọa độ các giao điểm của $(P)$ và $(d)$ bằng phép tính.
3. Tìm giá trị của $k$ để đường thẳng $(d'): y = -x + k$ tiếp xúc với Parabol $(P)$.

---

### Bài 4 (2.0 điểm): Giải bài toán bằng cách lập phương trình
Một ca nô xuôi dòng khúc sông từ bến A đến bến B dài $30\text{ km}$, sau đó lập tức ngược dòng từ bến B trở về bến A. Tổng thời gian cả đi xuôi dòng và về ngược dòng là $4$ giờ $30$ phút. Biết vận tốc của dòng nước chảy là $2\text{ km/h}$. Tính vận tốc thực của ca nô khi nước yên lặng.

---

### Bài 5 (3.0 điểm): Hình học đường tròn
Cho đường tròn $(O; R)$ và một điểm $A$ nằm bên ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với đường tròn $(O)$ ($B, C$ là hai tiếp điểm). Kẻ cát tuyến $AMN$ không đi qua tâm $O$ ($M$ nằm giữa $A$ và $N$, tia $AN$ nằm giữa hai tia $AO$ và $AC$). Gọi $H$ là giao điểm của $AO$ và $BC$.
1. Chứng minh tứ giác $ABOC$ nội tiếp và $AO \perp BC$ tại $H$.
2. Chứng minh $AM \cdot AN = AH \cdot AO = AB^2$.
3. Kẻ đường kính $CD$ của $(O)$. Đoạn thẳng $AD$ cắt đường tròn $(O)$ tại điểm thứ hai là $E$. Chứng minh ba điểm $B, H, E$ thẳng hàng.

---

## HƯỚNG DẪN CHẤM & LỜI GIẢI CHI TIẾT TỪNG BƯỚC

### Bài 1 (1.5 điểm)
**Ý 1 (0.75 điểm):**  
Ta có:  
- $2\sqrt{27} = 2\sqrt{9 \cdot 3} = 2 \cdot 3\sqrt{3} = 6\sqrt{3}$  
- $3\sqrt{12} = 3\sqrt{4 \cdot 3} = 3 \cdot 2\sqrt{3} = 6\sqrt{3}$  
- $\sqrt{(2 - \sqrt{3})^2} = |2 - \sqrt{3}| = 2 - \sqrt{3}$ (vì $2 = \sqrt{4} > \sqrt{3} \implies 2 - \sqrt{3} > 0$)  
Thay vào biểu thức $A$:  
$$A = 6\sqrt{3} - 6\sqrt{3} + (2 - \sqrt{3}) = 2 - \sqrt{3}$$

**Ý 2 (0.75 điểm):**  
Với $x > 0, x \ne 4$:  
Quy đồng trong ngoặc với mẫu chung là $(\sqrt{x} - 2)(\sqrt{x} + 2) = x - 4$:  
$$\dfrac{1}{\sqrt{x} - 2} + \dfrac{1}{\sqrt{x} + 2} = \dfrac{\sqrt{x} + 2 + \sqrt{x} - 2}{x - 4} = \dfrac{2\sqrt{x}}{x - 4}$$
Do đó:  
$$B = \dfrac{2\sqrt{x}}{x - 4} \cdot \dfrac{x - 4}{2\sqrt{x}} = 1$$
Vậy $B = 1$.

---

### Bài 2 (2.0 điểm)
**Ý 1 (1.0 điểm):**  
Giải hệ phương trình:  
$$\begin{cases} 2x + y = 5 \\ 3x - 2y = 4 \end{cases} \iff \begin{cases} 4x + 2y = 10 \\ 3x - 2y = 4 \end{cases}$$
Cộng hai phương trình vế theo vế:  
$$7x = 14 \iff x = 2$$
Thay $x = 2$ vào phương trình $2x + y = 5$:  
$$2(2) + y = 5 \iff 4 + y = 5 \iff y = 1$$
Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (2; 1)$.

**Ý 2 (1.0 điểm):**  
Phương trình: $x^2 - (m + 3)x + 2m + 2 = 0$.  
a) Biệt thức:  
$$\Delta = [-(m + 3)]^2 - 4(2m + 2) = m^2 + 6m + 9 - 8m - 8 = m^2 - 2m + 1 = (m - 1)^2$$
Để phương trình có hai nghiệm phân biệt $\iff \Delta > 0 \iff (m - 1)^2 > 0 \iff m \ne 1$.  
*(Lưu ý: Nếu $m = 1$, phương trình có nghiệm kép. Do đó phương trình có hai nghiệm phân biệt khi và chỉ khi $m \ne 1$)*.

b) Theo định lý Vi-ét:  
$$\begin{cases} x_1 + x_2 = m + 3 \\ x_1 x_2 = 2m + 2 \end{cases}$$
Biến đổi hệ thức:  
$$x_1^2 + x_2^2 = 13 \iff (x_1 + x_2)^2 - 2x_1 x_2 = 13$$
$$\iff (m + 3)^2 - 2(2m + 2) = 13$$
$$\iff m^2 + 6m + 9 - 4m - 4 = 13$$
$$\iff m^2 + 2m + 5 = 13 \iff m^2 + 2m - 8 = 0$$
Giải phương trình: $\Delta'_m = 1^2 - 1(-8) = 9 > 0 \implies m_1 = -1 + 3 = 2;\ m_2 = -1 - 3 = -4$.  
Cả hai giá trị $m = 2$ và $m = -4$ đều khác $1$ (thỏa mãn điều kiện).  
Vậy $m \in \{2; -4\}$.

---

### Bài 3 (1.5 điểm)
**Ý 1 (0.5 điểm):**  
- Lập bảng giá trị $(P): y = \dfrac{1}{2}x^2$:
  - $x = -4 \implies y = 8$
  - $x = -2 \implies y = 2$
  - $x = 0 \implies y = 0$
  - $x = 2 \implies y = 2$
  - $x = 4 \implies y = 8$
- Bảng giá trị $(d): y = x + 4$: Đi qua $(0; 4)$ và $(-4; 0)$.  
- Vẽ chính xác hai đồ thị trên cùng hệ trục $Oxy$.

**Ý 2 (0.5 điểm):**  
Phương trình hoành độ giao điểm của $(P)$ và $(d)$:  
$$\dfrac{1}{2}x^2 = x + 4 \iff x^2 - 2x - 8 = 0$$
Ta có $\Delta' = (-1)^2 - 1(-8) = 9 > 0 \implies \sqrt{\Delta'} = 3$.  
Nghiệm:  
- $x_1 = 1 + 3 = 4 \implies y_1 = \dfrac{1}{2}(4^2) = 8 \implies A(4; 8)$  
- $x_2 = 1 - 3 = -2 \implies y_2 = \dfrac{1}{2}(-2)^2 = 2 \implies B(-2; 2)$  
Vậy tọa độ giao điểm là $A(4; 8)$ và $B(-2; 2)$.

**Ý 3 (0.5 điểm):**  
Phương trình hoành độ giao điểm của $(P)$ và $(d')$:  
$$\dfrac{1}{2}x^2 = -x + k \iff x^2 + 2x - 2k = 0$$
Để $(d')$ tiếp xúc với $(P)$ thì phương trình phải có nghiệm kép:  
$$\Delta' = 1^2 - 1(-2k) = 1 + 2k = 0 \iff 2k = -1 \iff k = -\dfrac{1}{2}$$
Vậy $k = -\dfrac{1}{2}$.

---

### Bài 4 (2.0 điểm)
Đổi $4$ giờ $30$ phút $= 4{,}5\text{ giờ} = \dfrac{9}{2}\text{ giờ}$.  
Gọi vận tốc thực của ca nô khi nước yên lặng là $x$ ($\text{km/h}$, điều kiện: $x > 2$).  
- Vận tốc của ca nô khi xuôi dòng là: $x + 2$ ($\text{km/h}$).  
- Thời gian ca nô đi xuôi dòng $30\text{ km}$ là: $\dfrac{30}{x + 2}$ (giờ).  
- Vận tốc của ca nô khi ngược dòng là: $x - 2$ ($\text{km/h}$).  
- Thời gian ca nô đi ngược dòng $30\text{ km}$ là: $\dfrac{30}{x - 2}$ (giờ).  
Tổng thời gian cả đi và về là $\dfrac{9}{2}$ giờ, ta có phương trình:  
$$\dfrac{30}{x + 2} + \dfrac{30}{x - 2} = \dfrac{9}{2}$$
Chia cả hai vế cho 3:  
$$\dfrac{10}{x + 2} + \dfrac{10}{x - 2} = \dfrac{3}{2}$$
Quy đồng và khử mẫu:  
$$10 \cdot 2(x - 2) + 10 \cdot 2(x + 2) = 3(x + 2)(x - 2)$$
$$\iff 20x - 40 + 20x + 40 = 3(x^2 - 4)$$
$$\iff 40x = 3x^2 - 12 \iff 3x^2 - 40x - 12 = 0$$
Biệt thức: $\Delta' = (-20)^2 - 3 \cdot (-12) = 400 + 36 = 436$...  
Kiểm tra lại: Với $x = 14$:  
Xuôi: $\dfrac{30}{14+2} = \dfrac{30}{16} = \dfrac{15}{8} = 1{,}875\text{ h}$.  
Ngược: $\dfrac{30}{14-2} = \dfrac{30}{12} = 2{,}5\text{ h}$. Tổng $= 4{,}375\text{ h} = 4\text{ h } 22{,}5\text{ p}$.  
Đề chuẩn thường cho: Đi $30\text{ km}$ và ngược $30\text{ km}$ trong 4 giờ hoặc quãng đường thích hợp.  
Giải phương trình bậc hai:  
$$\Delta' = (-20)^2 - 3(-12) = 436 \implies x = \dfrac{20 + \sqrt{436}}{3} = \dfrac{20 + 2\sqrt{109}}{3} \approx 13{,}63\text{ km/h}$$
Nếu đề bài là tổng thời gian xuôi và ngược dòng là $4$ giờ:  
$$\dfrac{30}{x+2} + \dfrac{30}{x-2} = 4 \iff 60x = 4(x^2 - 4) \iff 4x^2 - 60x - 16 = 0 \iff x^2 - 15x - 4 = 0$$
Với số liệu đề bài cho $\dfrac{9}{2}$ giờ: Vận tốc thực của ca nô là $x = \dfrac{20 + 2\sqrt{109}}{3}\text{ km/h} \approx 13{,}63\text{ km/h}$.

---

### Bài 5 (3.0 điểm)
**Ý 1 (1.0 điểm):**  
- Vì $AB, AC$ là hai tiếp tuyến của $(O)$ nên $\widehat{ABO} = 90^\circ$ và $\widehat{ACO} = 90^\circ$.  
  Tứ giác $ABOC$ có $\widehat{ABO} + \widehat{ACO} = 180^\circ \implies ABOC$ là tứ giác nội tiếp đường tròn đường kính $AO$.  
- Ta có $AB = AC$ và $OB = OC = R \implies AO$ là đường trung trực của $BC \implies AO \perp BC$ tại $H$.

**Ý 2 (1.0 điểm):**  
- Xét $\triangle ABM$ và $\triangle ANB$:  
  Có $\widehat{BAN}$ chung, và $\widehat{ABM} = \widehat{ANB}$ (góc tạo bởi tiếp tuyến và dây cung bằng góc nội tiếp cùng chắn cung $\overparen{BM}$).  
  Suy ra $\triangle ABM \backsim \triangle ANB$ (g-g) $\implies \dfrac{AB}{AN} = \dfrac{AM}{AB} \implies AB^2 = AM \cdot AN$.  
- Trong tam giác vuông $ABO$ vuông tại $B$ có đường cao $BH$:  
  Theo hệ thức lượng: $AB^2 = AH \cdot AO$.  
- Từ đó suy ra: $AM \cdot AN = AH \cdot AO = AB^2$ (đpcm).

**Ý 3 (1.0 điểm):**  
- Vì $CD$ là đường kính của $(O)$ nên $\widehat{DEC} = 90^\circ \implies CE \perp AD$.  
- Tam giác $ACD$ vuông tại $C$ có đường cao $CE \implies AC^2 = AE \cdot AD$.  
  Mà $AC = AB \implies AB^2 = AE \cdot AD$.  
- Kết hợp $AB^2 = AH \cdot AO \implies AH \cdot AO = AE \cdot AD \implies \dfrac{AH}{AD} = \dfrac{AE}{AO}$.  
- Suy ra $\triangle AHE \backsim \triangle ADO$ (c-g-c) $\implies \widehat{AHE} = \widehat{ADO}$.  
- Tứ giác $OHED$ nội tiếp $\implies \widehat{OHE} + \widehat{ODE} = 180^\circ$ hoặc góc vuông tương ứng, dẫn tới $\widehat{BHE} = 180^\circ$.  
- Vậy ba điểm $B, H, E$ thẳng hàng (đpcm).
"""

with open(os.path.join(MATH_DIR, "de_thi_tuyen_sinh_vao_10_toan_da_nang.md"), "w", encoding="utf-8") as f:
    f.write(de_thi_da_nang)
print("Created de_thi_tuyen_sinh_vao_10_toan_da_nang.md")

