# # stack last in - first out

# # Xem phần tử cuối cùng của stack
# stack = [1, 2, 3, 4]
# print(stack[-1])

# # Đưa phần tử vào cuối stack
# stack.append(5)
# print(stack)

# # Xóa phần tử cuối khỏi stack
# stack.pop()
# print(stack)

# stack_length = len(stack)

# def is_empty(stack):
#     if len(stack) == 0:
#         return True
#     else:
#         return False
    

# Thực hành
"""Đề bài: Chuyển đổi số thập phân sang nhị phân
Viết một hàm sử dụng stack để chuyển một số nguyên không âm từ hệ thập phân (base 10) sang hệ nhị phân (base 2)."""

# number = int(input("Nhập số hệ thập phân: "))

# def decimal_to_binary(number):
#     if number <= 0:
#         return "0"
#     else:
#         stack = []
#         while number > 0:
#             remainer = number % 2
#             stack.append(remainer)
#             number = number // 2

#         result = ""
#         while len(stack) > 0:
#             remainer = stack.pop()
#             result += str(remainer)
#         return result
    
# print(decimal_to_binary(number))

# Thực hành 2
class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []

    def visit_page(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()
        print(f"URL: {url}")

    def back(self):
        if self.back_stack:
            current_page = self.back_stack.pop()
            self.forward_stack.append(current_page)
            previous_page = self.back_stack[-1]
            print(f"Previous page: {previous_page}")
        else:
            print("Nothing to back")

    def forward(self):
        if self.forward_stack:
            forward_page = self.forward_stack.pop()
            self.back_stack.append(forward_page)
            print(f"Forward page: {forward_page}")
        else:
            print("Nothing to Forward")

browser = Browser()
browser.visit_page("www.facebook.com")
browser.visit_page("www.youtube.com")
browser.visit_page("www.wikipedia.org")

browser.back()
browser.back()
browser.forward()
browser.forward()