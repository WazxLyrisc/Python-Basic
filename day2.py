my_string = "phuong123123"
chieu_dai_chuoi = len(my_string)
print(chieu_dai_chuoi)

'''
1. Chiều dài của chuỗi: len(ten_chuỗi) => tổng số lương ký tự trong 1 chuỗi

- Truy cập vào các phần tử nằm trong 1 chuỗi:
    tên_chuỗi[index]
    0 <= index < len(my_string)
!!! Lưu ý: các giá trị nằm trong 1 chuỗi bắt đầu từ số 0

- Cách để lấy ra ký tự nằm cuối 1 chuỗi: tên_chuỗi[]

    Giá trị cuối = 5
    chiều dài thực tế là 6 => hàm len chiều dài chuỗi là 1 giá trị luôn trả đúng về số lượng của 1 chuỗi
    vị trí cuối = len(chuoi) - 1 
    print(my_string[len(my_string) - 1])
'''
my_text_number = "125602"
# print(my_text_number[0])
# print(my_text_number[1])
# print(my_text_number[2])
# print(my_text_number[3])
# print(my_text_number[4])
# print(my_text_number[5])

total = int(my_text_number[0]) + int(my_text_number[1]) + int(my_text_number[2]) + int(my_text_number[3]) + int(my_text_number[4]) + int(my_text_number[5])
# total =   "1"           +         "2"       +        "5"        +        "6"        +       "0"          +        "2"       
print(total)

a = "10"
a = int(a)
b = "20"
b = int(b)
# Chuỗi + chuỗi => ra 1 chuỗi khác gồm các chuỗi nhỏ nối lại với nhau
print(a + b)

'''
2. Các phép so sánh trong python:
    >, >=, <, <=, ==, !=

    - Các kiểu câu so sánh: 
        + So sánh và: and
        + So sánh hoặc: or
'''
value1 = 20
value2 = 10

a = 8
b = "8"

result = value1 != value2 and a == b
print(result)

'''
3. IF/ELSE ở trong python
    if điều_kiện:
        Đoạn này sẽ được thực thi nếu câu điều kiện đúng
    else:
        Đoạn này được thực thi nếu các câu điều kiện bên trên sai
'''
# print Thiếu nhi : 1 -> 12
# print Thiếu niên: 12 -> 18
# print Trưởng thành: age lớn hơn hoặc bằng 18
# print sai khoảng tuổi: age nhỏ hơn 1

age = -1
if age >= 1 and age < 12:
    print('Tôi đang ở độ tuổi thiếu nhi')
elif age >= 12 and age < 18:
    print('Tôi đang ở độ tuổi thiếu niên')
elif age >= 18:
    print("Truong thanh")
else:
    print("Sai khoang tuoi")


# Điểm phải là giá trị nhập từ input
# Nếu điểm < 5 => Điểm E
# điểm >= 5 và điểm nhỏ hơn 6 => Điểm D
# điểm >= 6 và điểm nhỏ hơn 7 => Điểm C
# điểm >= 7 và điểm nhỏ hơn 8 => Điểm B
# điểm >= 8 và điểm nhỏ hơn 9 => Điểm A
# điểm >= 9 => Điểm A+

# Tạo chức năng check đăng nhập
# khai báo 2 giá trị bầu là username, passowrd
# set username và password mặc đình là gì đó
# khai báo thêm 2 biến nữa là username_input và password_input
# Thục hiện viết if else để check đăng nhập khi và chỉ khi ussname = username_input và password = passwor_input

# for i in range(start, end, bước_nhảy)
# điều kiện để vòng chạy là: start <= i < end
# for i in range(0, 10, 5):
#     print(i)

# for i in range(0, 10, 1):
#     print(i)

for i in range(10, 0, -1):
    print(i)

# Yêu cầu ngừoi dung nhập 1 chuỗi và in ra các chữ cái nằm trong chuỗi