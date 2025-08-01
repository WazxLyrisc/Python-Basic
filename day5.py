'''1. Đánh giá thuật toán và thời gian của thuật toán'''
import time

def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = 999999937 # Số nguyên tố lớn nhất có 9 chữ số

begin = time.time()
result = is_prime(number)
end = time.time()

print(number, "is prime" if result else "is not prime")
print("Algorithm took", end - begin, "seconds")


import time

def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 999999937

begin = time.time()
result = is_prime(number)
end = time.time()

print(number, "is prime" if result else "is not prime")
print("Algorithm took", end - begin, "seconds")

'''2. Ví dụ 1: Đánh giá độ phức tạp của thuật toán sau:'''
n = int(input()) # O(1)
s1 = 0 # O(1)

for i in range(1, n + 1): # O(n)
    s1 += i # O(1 * n) = O(n)

s2 = 0 # O(1)
for i in range(1, n + 1): # O(n)
    s2 += i * i # O(1 * n) = O(n)

print(s1) # O(1)
print(s2) # O(1)

# => Độ phức tạp của thuật toán: O(n)

'''3. Ví dụ 2: Đánh giá độ phức tạp của thuật toán sau:'''
sum = 0 # O(1)
for i in range(1, n + 1): # O(n^2)
    for j in range(1, i + 1):
        sum += 1

print(sum) # O(1)

# => Độ phức tạp: O(n^2)

'''4. Ví dụ 3: Đánh giá độ phức tạp của thuật toán sau'''

n = int(input("Nhập n: ")) # O(1)
arr = [] # O(1)
for i in range(1, n + 1): #O(n)
    i = int(input()) # O(n)
    arr.append(i) #O(n)

arr.sort() # O(nlogn)
found = False # O(1)
for i in range(len(arr) - 1): # O(n)
    if arr[i] == arr[i + 1]: # O(n)
        print("True") # O(1)
        found = True # O(1)
        break # O(1)

if not found: # O(1)
    print("False") # O(1)

# => Độ phức tạp của bài toán: O(nlogn)