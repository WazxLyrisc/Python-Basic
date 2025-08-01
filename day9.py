# Chữa bài kiểm tra
'''BT1'''
# n = int(input("Nhập độ dài của mảng: "))
# arr = []
# for i in range(n):
#     i = int(input("Nhập các phần tử của mảng: "))
#     arr.append(i)

# found_number = False
# for i in range(n):
#     for j in range(i + 1, n): #Còn lại của mảng
#         if arr[i] == arr[j]:
#             print("Số đầu tiên xuất hiện lặp lại: ", arr[i])
#             found_number = True
#             break

# if found_number == False:
#     print("Không có số nào lặp lại.")

'''BT2'''
n = int(input("Nhập độ dài của mảng: "))
arr = []
for i in range(n):
    i = int(input("Nhập các phần tử của mảng: "))
    arr.append(i)

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Điểm cao nhất là: ", arr[0])

if n < 2:
    print("Không có")
elif n >= 2:
    for i in range(n):
        if arr[i] != arr[0]:
            print("Điểm cao thứ hai là: ", arr[i])
            break