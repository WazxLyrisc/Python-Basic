'''1. Thuật toán tìm kiếm tuần tự (Linear search)'''
def linear_search(arr, num):
    for i in range (len(arr)):
        if arr[i] == num:
            return i
        
numbers = [10, 20, 5, -4, 100, 23, -6]
target = 23
result = linear_search(numbers, target)
print(result)

'''2. Thuật toán tìm kiếm nhị phân (Binary search)'''
def binary_search(arr, num):
    arr.sort()
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if num < arr[mid]:
            end = mid - 1
        elif num > arr[mid]:
            start = mid + 1
        else: # arr[mid] == num
            return mid
    return -1

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 16]
target = 10
result = binary_search(list, target)
print(result)