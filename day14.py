"""BT1"""
# Viết chương trình mô phỏng bộ bài tây đơn giản.

# Lớp Card

#    - Thuộc tính: 

#       + value (giá trị: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)

#       + suit (chất: ♥ ♦ ♣ ♠).

#    - Phương thức: __str__ để in lá bài (ví dụ: "A♥").

# Lớp Deck

#    - Thuộc tính: cards (danh sách lá bài, gồm 52 lá).

#    - Phương thức:

#       + __str__: trả về chuỗi liệt kê toàn bộ các lá bài trong bộ.

#       + shuffle(): xáo ngẫu nhiên bộ bài.

#       + deal_four(): chia bộ bài thành 4 phần bằng nhau (mỗi phần 13 lá) và in ra danh sách lá bài của từng phần.

# 👉 Yêu cầu:

#    - Tạo một bộ bài, in ra số lượng lá.

#    - Xáo bài, rồi chia bộ bài thành 4 phần và in ra các phần.

# *
# HƯỚNG DẪN:
# Tạo lớp Card với __init__ và __str__.

# Tạo lớp Deck:

# Khởi tạo bằng vòng lặp 2 chiều (giá trị × chất) để sinh 52 lá.

# Cài đặt __str__ để nối các lá bằng join().  

# shuffle() cần import random trước đó, dùng random.shuffle(self.cards).

# deal_four() chia self.cards thành 4 list (mỗi list 13 lá).

# Trong chương trình chính:


# Tạo deck, in len(deck.cards) và print(deck) để thấy toàn bộ bộ bài.

# Shuffle và in lại.

# Gọi deal_four() rồi in từng phần.

# *Code gợi ý
# deck = Deck()
# print("Initial deck size:", len(deck.cards))
# print(deck)

# deck.shuffle()
# print("\nAfter shuffle:")
# print(deck)

# hands = deck.deal_four()
# print("\n")
# for i, hand in enumerate(hands, start = 1):
#     print(f"Hand {i}: {[str(card) for card in card]}")


import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value}{self.suit}"
    
class Deck:
    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['♥', '♦', '♣', '♠']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_four(self):
        hands = [self.cards[i*13:(i+1)*13] for i in range(4)]
        for idx, hand in enumerate(hands, 1):
            print(f"Phần {idx}: " + ', '.join(str(card) for card in hand))

deck = Deck()
print(f"Tất cả lá bài bên trong bộ bài: {len(deck.cards)}")
print("Bộ bài ban đầu:")
print(deck)
deck.shuffle()
print("Bộ bài sau khi xáo:")
print(deck)
print("\nChia bộ bài thành 4 phần:")
deck.deal_four()


"""Bài 2"""
# Đề: Kiểm tra chuỗi ký tự có đối xứng (palindrome) hay không bằng Stack.

# Yêu cầu:

#    - Nhập vào một chuỗi ký tự (chỉ gồm chữ cái, không phân biệt hoa/thường).

#    - Sử dụng Stack để kiểm tra xem chuỗi có phải palindrome (đọc xuôi = đọc ngược) hay không.

#    - In "YES" nếu đối xứng, "NO" nếu không.

# Ví dụ
#    - Input: "madam" → Output: YES

#    - Input: "RaceCar" → Output: YES

#    - Input: "python" → Output: NO

# *
# Hướng dẫn gợi ý

# Chuyển chuỗi về chữ thường.

# Dùng Stack để lưu các ký tự.

# Lấy ra các ký tự để tạo chuỗi đảo ngược.

# So sánh chuỗi gốc và chuỗi đảo.

def palindrome(c00lkid):
    c00lkid = c00lkid.lower()
    stack = []
    for shedletsky in c00lkid:
        stack.append(shedletsky)
    new_stack = ''
    while stack:
        new_stack += stack.pop()
    return "YES" if c00lkid == new_stack else "NO"

forsaken = input("Nhập chữ vào đây: ")
print(palindrome(forsaken))


"""Bài 3"""

# Đề: Thống kê số lần xuất hiện của từ trong một đoạn văn
# Yêu cầu:

#    - Nhập vào một đoạn văn bản (chuỗi).

#    - Tách thành các từ (không phân biệt hoa/thường, bỏ dấu câu).

#    - Sử dụng dictionary (dict) để đếm số lần xuất hiện của mỗi từ.

#    - In ra kết quả thống kê (từ nào xuất hiện bao nhiêu lần).

# *
# Hướng dẫn gợi ý

# Chuyển chuỗi về chữ thường ().

# Loại bỏ dấu câu.

# Tách từ bằng split().

# Dùng dictionary để đếm số lần xuất hiện.

# In kết quả.

# Gợi ý: 
# text = "Python is fun. Python is easy to learn"
# word_count(text)


def word(chance):
    chance = chance.lower()
    chance = chance.split()
    count = {}
    for dusekar in chance:
        if dusekar in count:
            count[dusekar] += 1
        else:
            count[dusekar] = 1

    for dusekar, num in count.items():
        print(f"{dusekar}: {num}")

chance = "Ninety-nine point nine percent of gamblers will stop before winning big. So you won big?. Not only I have not stopped"
word(chance)