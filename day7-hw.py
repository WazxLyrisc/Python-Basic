import random
arr = random.sample(range(100), 20)

def selection_sort(arr: list):
    arr_sorted = []
    while arr:
        minimum = min(arr)
        arr_sorted.append(minimum)
        arr.remove(minimum)
    return arr_sorted

result = selection_sort(arr)
print(result)

def bubbles_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

c00lkid = bubbles_sort(arr)
print(c00lkid)

import datetime
start_arr = datetime.datetime.now()
end_arr = datetime.datetime.now()

play_list = end_arr - start_arr
print(f"Chương trình chạy trong {play_list}")