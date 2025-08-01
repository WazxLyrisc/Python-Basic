'''class: Khuôn để tạo ra các objects'''

class Dog:
    # Phương thức __init__ để khởi tạo các thuộc tính cho class
    def __init__(self, name, age, color, gender, type):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender
        self.type = type

    # Phương thức để in ra thông tin các chú chó
    def display_information(self):
        print("Tên: " + self.name)
        print("Tuổi:", self.age)
        print("Màu lông: " + self.color)
        print("Giới tính: " + self.gender)
        print("Giống chó: " + self.type)

# Tạo ra các object từ class Dog bên trên
dog1 = Dog("Kiki", 3, "White", "Male", "Fur")
dog2 = Dog("Lulu", 2, "Black", "Male", "Tây Tạng")
dog3 = Dog("Haha", 1, "Brown", "Female", "Puddle")

# Truy cập vào các thuộc tính của object thông qua cú pháp: <tên_object>.<tên_thuộc_tính>
print(dog1.name)

dog1.display_information()
print("====================")
dog2.display_information()
print("====================")
dog3.display_information()

# Chữa bài tập thực hành
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def display_information(self):
        print(f"Một chiếc xe {self.color} chạy được {self.mileage}km")

car1 = Car("xanh", 20000)
car2 = Car("đỏ", 30000)

car1.display_information()
car2.display_information()

# Tính đóng gói trong OOP
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = "Gaugau"
    
    def speak(self):
        return self.sound
    
dog1 = Dog("Lulu", 2)
print(dog1.speak())

# Tính kế thừa trong OOP
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = "Gaugau"
    
    def speak(self):
        print(self.sound)
    
class MyDog(Dog):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.gender = gender

    def display_information(self):
        print(f"{self.name} - {self.age} - {self.gender}")

myDog1 = MyDog("Lulu", 3, "Male")
myDog1.display_information()
myDog1.speak()


class Dog:
    # Phương thức __init__ để khởi tạo các thuộc tính cho class
    def __init__(self, name, age, color, gender, type):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender
        self.type = type

    # Phương thức để in ra thông tin các chú chó
    def display_information(self):
        print("Tên: " + self.name)
        print("Tuổi:", self.age)
        print("Màu lông: " + self.color)
        print("Giới tính: " + self.gender)
        print("Giống chó: " + self.type)

    def update_information(self, new_name, new_age, new_color, new_gender, new_type):
        self.name = new_name
        self.age = new_age
        self.color = new_color
        self.gender = new_gender
        self.type = new_type

# Tạo ra các object từ class Dog bên trên
dog1 = Dog("Kiki", 3, "White", "Male", "Fur")
dog2 = Dog("Lulu", 2, "Black", "Male", "Tây Tạng")
dog3 = Dog("Haha", 1, "Brown", "Female", "Puddle")

# Đổi giá trị của thuộc tính
dog1.name = "Hihi"
dog2.update_information("Lala", 5, "Yellow", "Female", "Pitbull")
dog2.display_information()

class Item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

class Order:
    def __init__(self, item_list, customer_id):
        self.item_list = item_list
        self.customer_id = customer_id

    def total(self):
        sum = 0
        for i in range(1, len(self.item_list) + 1):
            sum += self.item_list[i]

class Promo:
    def __init__(self, price):
        self.price = price

    def discount(self):
        discount = self.price * 0.5
        print(discount)


# Chữa BTVN
class TaiKhoanChinh:
    def __init__(self, stk, ten, so_du):
        self.stk = stk
        self.ten = ten
        self.so_du = so_du

    def lay_so_du(self):
        print("Số dư của tài khoản:", self.so_du)

    def rut_tien(self, so_tien):
        if so_tien > self.so_du:
            print("Số dư trong tài khoản của bạn không đủ để thực hiện giao dịch")
        else:
            self.so_du = self.so_du - so_tien
            print("Số tiền rút:", so_tien)
            self.lay_so_du()

    def nap_tien(self, so_tien):
        self.so_du = self.so_du + so_tien
        print("Số tiền nạp:", so_tien)
        self.lay_so_du()

class TaiKhoanTietKiem(TaiKhoanChinh):
    def __init__(self, stk, ten, so_du, lai_suat):
        super().__init__(stk, ten, so_du)
        self.lai_suat = lai_suat

taikhoan1 = TaiKhoanChinh("0123456789", "Nguyễn Văn A", 10000000)
taikhoan1.lay_so_du()
taikhoan1.rut_tien(5000000)
taikhoan1.nap_tien(20000000)