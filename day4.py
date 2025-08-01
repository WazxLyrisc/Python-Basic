'''
Tạo các class gồm các thuộc tính và phương thức sau đây:
    1. Class HinhChuNhat:
        - 2 thuộc tính: Chiều dài, Chiều rộng
        - Phương thức get_P() để tính chu vi HinhChuNhat
        - Phương thức get_S() để tính diện tích HinhChuNhat
        
    2. Class TamGiacVuong kế thừa từ class HinhChuNhat:
        - 2 thuộc tính: 2 cạnh góc vuông là Chiều dài và Chiều rộng của HinhChuNhat
        - Phương thức get_S() để tính diện tích TamGiac
        - Phương thức get_hypotenuse() để tính độ dài cạnh huyền tam giác
'''
import math
class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def get_P(self):
        return (self.chieu_dai + self.chieu_rong) * 2
    
    def get_S(self):
        return (self.chieu_dai * self.chieu_rong)
    
class TamGiacVuong(HinhChuNhat):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong)

    def get_S(self):
        return (self.chieu_dai * self.chieu_rong * 0.5)
    
    def get_hypotenuse(self):
        return math.sqrt(self.chieu_dai ** 2 + self.chieu_rong ** 2)

tamgiac1 = TamGiacVuong(10, 5)
print(tamgiac1.get_S())
print(tamgiac1.get_hypotenuse())

'''Sử dụng lớp trừu tượng (abstract class) đã có sẵn trong Python'''

from abc import ABC, abstractmethod
class MonAn(ABC):
    @abstractmethod
    def chuan_bi(self):
        pass

class MonChinh(MonAn):
    def chuan_bi(self):
        print("Chuẩn bị món chính")

class MonTrangMieng(MonAn):
    def chuan_bi(self):
        print("Chuẩn bị món tráng miệng")
'''
Hãy xây dựng một hệ thống trừu tượng PaymentMethod mô phỏng các hình thức thanh toán khác nhau:
1. Thanh toán bằng tiền mặt
2. Thanh toán chuyển khoản
3. Thanh toán quẹt thẻ
'''
from abc import ABC, abstractmethod

# Bước 1: Tạo lớp trừu tượng PaymentMethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class CashPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Thanh toán {amount} bằng tiền mặt")

class BankingPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Thanh toán {amount} bằng chuyển khoản")

class CardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Thanh toán {amount} bằng thẻ tín dụng")

payment1 = CashPayment()
payment1.pay(100000)