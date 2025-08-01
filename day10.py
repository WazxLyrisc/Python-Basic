# khai báo set

# fruit_basket = {"apple", "kiwi", "banana", "apple"}

# for fruit in fruit_basket:
#     print(fruit)

# # Thêm phần tử mới vào trong set
# fruit_basket.add("orange")
# fruit_basket.update({"cherry", "peach"})

# # Xóa phần tử ra khỏi set
# # fruit_basket.remove("apple")
# fruit_basket.discard("apple")
# for fruit in fruit_basket:
#     print(fruit)

# Phép hợp trong set
lunch = {"soup", "sandwich", "omelet"}
dinner = {"soup", "steak", "ice-cream"}
# O(m+n)
meals = lunch.union(dinner)
meals = lunch | dinner

# Phép giao trong set
laptop = {"Lenovo", "Apple", "Dell"}
tablet = {"Apple", "Lenovo", "Samsung"}
devices = laptop.intersection(tablet)
devices = laptop | tablet

# phép trừ trong set
car = {"mercedes", "vinfast", "bmw"}
motobike = {"honda", "yamaha", "vinfast"}
transportations = car.difference(motobike)
transportations = car - motobike

# ánh xạ
# gpa_10 = [5.0, 7.0, 10.0, 9.0]
# def convert_gpa(score):
#     return score/10 * 4

# gpa_4 = map(convert_gpa, gpa_10)
# print(list(gpa_4))

students = ["Hieu", "My Anh", "Tuan Anh"]
student_upper = map(str.upper, students)
print(list(student_upper))

# Dictionary key - value
person ={
    "name": "Kien",
    "gender": "Male",
    "age": 20,
    "job": "Engineer",
}
person["age"] = 50
person["hometown"] = "Hanoi"

# khởi tạo dictionary
phone_book = {}
phone_book = dict()

# Thêm/Cập nhật dictionary
phone_book['John'] = '0192848281'
phone_book['Alice'] = '0192949291'

# Truy xuất dictionary
print(phone_book.get("John"))

# Xóa value trong dictionary
del phone_book["Alice"]