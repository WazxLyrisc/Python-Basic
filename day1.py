'''1. Cách in giá trị ra màn hình'''
print("Hello world")
print(1 + 1)
x = "MindX"
print(x)
print("MindX", "School")


'''2. Cách khai báo biến trong python: <tên biến> = <giá trị>'''
name = "Đào Trung Kiên"
age = 50
job = "Developer"
hometown = "Hanoi"

'''
3. Các kiểu dữ liệu trong python
- Số nguyên: 
    Ký hiệu: int(integer)
    VD: 3, 4, 10, -100, -2000
- Số thực: 
    Ký hiệu: float
    VD: 3,9; 10,2; 3,14; -1,5
- Chuỗi:
    Ký hiệu: str(string)
    VD: "MindX", 'School', 'Hanoi', "Việt Nam"
- Boolean:
    Ký hiệu: bool
    VD: True, False
!!! Lệnh type() để kiểm tra kiểu dữ liệu của biến
'''
a = 10
b = 3.14
c = "Hà Nội"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

''' 4. Cho phép người dùng nhập từ bàn phím vào chương trình '''
chieu_dai = int(input("Nhập chiều dài: "))
chieu_rong = int(input("Nhập chiều rộng: "))

print(type(chieu_dai))
print(type(chieu_rong))

# Phương pháp ép kiểu dữ liệu
a = 10 # int
b = "10" # str
x = float(a)
y = int(b)

print(type(a))
print(type(b))
print(type(x))
print(type(y))

'''
5. Các toán tử cơ bản trong python
- Cộng: Dùng để tính tổng
    Ký hiệu: +
- Trừ: Dùng để tính hiệu
    Ký hiệu: -
- Nhân: Dùng để tính tích
    Ký hiệu: *
- Chia: Dùng để tính thương
    Ký hiệu: /
- Lấy phần dư: Dùng để tính phần dư của phép chia
    Ký hiệu: %
    VD: 7 % 2 = 1, 100 % 30 = 10
- Lấy phần nguyên: Dùng để tính phần nguyên của phép chia
    Ký hiệu: //
    VD: 7 // 2 = 3, 100 // 30 = 3, 10 // 5 = 2
- Luỹ thừa: Dùng để tính luỹ thừa
    Ký hiệu: **
    VD: 2 ** 3 = 8, 10 ** 2 = 100, 5 ** 4 = 625
'''

# Bài tập:
# 1. Viết chương trình để nhập 2 giá trị là HỌ và TÊN. 
#     Sau đó in 2 giá trị ra màn hình cùng 1 dòng.

ho = input("Họ: ")
ten = input("Tên: ")
print(ho, ten)

# 2. Viết chương trình để nhập vào 2 giá trị là a và b.
#     Sau đó sử dụng 7 toán tử bên trên để tính các giá trị của chúng.

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a %", "b =", a % b)
print("a // b =", a // b)
print("a^b =", a ** b)


# Chữa BTVN
n = int(input("Nhập số n: "))
sum = 0

# for (start, stop, step)
# Lặp dãy số từ 1 -> n
for i in range(1, n + 1, 2):
    sum += i
print("Tổng các số lẻ từ 1 đến n là", sum)

# Kiểm tra n có phải số nguyên tố hay không
check = 0
for i in range(2, n):
    if (n % i == 0):
        check = 1
    break
if (check == 0):
    print("n là số nguyên tố")
else:
    print("n không là số nguyên tố")

# In ra các ước số của n
for i in range(1, n + 1):
    if (n % i == 0):
        print(i, "là ước của n")