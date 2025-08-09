'''Hàng đợi'''
# # First in - first out : là cấu trúc dữ liệu
# queue = [1,2,3]

# # Xem phần tử đầu tiên của queue
# print(queue[0])

# # thêm phần tử vào queue
# queue.append(4)
# print(queue)

# # Xóa phần tử khỏi queue (Phần tử đầu tiên)
# front = queue.pop(0)
# print(front)
# print(queue)

# # kiểm tra queue rỗng
# def is_empty(queue):
#     if len(queue) == 0:
#         return True
#     else:
#         return False
    

"""Bài Thực hành 1"""
# Bài 1: Cài đặt Queue cơ bản bằng danh sách (list)
# Yêu cầu:
#   - Tạo lớp Queue với các phương thức:
#       + enqueue(item) — thêm phần tử vào cuối hàng đợi.
#       + dequeue() — lấy và xóa phần tử ở đầu hàng đợi.
#       + is_empty() — kiểm tra hàng đợi có rỗng không.
#       + size() — trả về số lượng phần tử trong hàng đợi.
# Thử sử dụng hàng đợi để lưu và lấy các số nguyên từ 1 đến 5.

"""class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty() == False:
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)

q = Queue()

for i in range(1, 6):
    q.enqueue(i)

while not q.is_empty():
    print(q.enqueue())

# while not q.is_empty: # Nếu như nó không rỗng
#     q.dequeue()
#     print(q.size())
# Thêm 1 -> 5
# Lấy ra từng phần tử và in"""


"""Bài thực hành 2"""
# # Bài 2: Mô phỏng hệ thống xếp hàng
# # Yêu cầu:
# #   - Người dùng đến quầy giao dịch và lấy số thứ tự từ 1 đến 5.
# #   - Mỗi lượt xử lý, quầy giao dịch lấy số tiếp theo trong hàng đợi và thông báo "Đang phục vụ khách hàng số X".
# #   - In ra danh sách còn lại trong hàng đợi sau mỗi lượt.
# #   - Gợi ý: Có thể dùng collections.deque để tối ưu:

# from collections import deque

# queue = deque()
# # enqueue các số từ 1 đến 5
# # xử lý đến khi hàng đợi rỗng

# Cách 1
"""queue1 = []
for i in range(1, 6):
    queue1.append(i)

def is_empty(queue1):
    if len(queue1) == 0:
        return True
    else:
        return False
    
while not is_empty(queue1):
    current = queue1.pop(0)
    print(f"Đang phục vụ khác hàng thứ {current}")
    print(f"Hàng chờ còn {len(queue1)} khách hàng")"""

# Cách 2

"""from collections import deque

queue1 = deque()
for i in range(1, 6):
    queue1.append(i)

def is_empty(queue1):
    if len(queue1) == 0:
        return True
    else:
        return False
    
while not is_empty(queue1):
    current = queue1.popleft()
    print(f"Đang phục vụ khác hàng thứ {current}")
    print(f"Hàng chờ còn {len(queue1)} khách hàng")"""

"""Bài thực hành 3"""

# Lập trình ứng dụng MP3 Player

import queue
class MP3Player:
    def __init__(self):
        self.music_queue = queue.Queue()
        self.current_song = None

    def add_song(self, song):
        self.music_queue.put(song)

    def play_next_song(self):
        if self.music_queue.empty():
            print("Hàng đợi không có bài hát nào đang chờ! ")
        else:
            self.current_song = self.music_queue.get()
            print(f"Chơi bài hát {self.music_queue.get()}")

    def skip_song(self):
        if self.current_song is None:
            print("Không có bài hát nào đang chạy nên không thể skip qua")
        else:
            self.current_song = None
            self.play_next_song()

song = MP3Player()
song.add_song("Rap God")
song.add_song("Godzilla")
song.add_song("Limbo")


song.skip_song()