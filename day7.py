'''1. Thuật toán sắp xếp lựa chọn (Selection sort)'''
def selection_sort(arr: list):
    arr_sorted = [] # O(1)
    while arr:
        minimum = min(arr) # O(n^2) Khai báo biến minimum để lưu giá trị bé nhất trong arr
        arr_sorted.append(minimum) # 0(n^2) Thêm giá trị đó vào danh sách mới
        arr.remove(minimum) # O(n) Xoá giá trị đó khỏi danh sách cũ
    return arr_sorted

# arr = [9, 10, 11, 1, -6, -100]
# result = selection_sort(arr)
# print(result)

'''2. Thuật toán nổi bọt (Bubbles sort)'''
def bubbles_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# arr = [9, 10, 11, 1, -6, -100]
# result = bubbles_sort(arr)
# print(result)