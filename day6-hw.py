import random
arr = random.sample(range(100), 20)

target = 19

def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i

result = linear_search(arr, target)
print(result)

def binary_search(arr, num):
    arr.sort()
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if num < arr[mid]:
            start = arr[mid] - 1
        elif num > arr[mid]:
            end = arr[mid] + 1
        else:
            return mid
    return -1

shedletsky = binary_search(arr, target)
print(shedletsky)

import datetime
start_time = datetime.datetime.now()
end_time = datetime.datetime.now()

elasped_time = end_time - start_time
print(f"Thời gian chạy là {elasped_time}")