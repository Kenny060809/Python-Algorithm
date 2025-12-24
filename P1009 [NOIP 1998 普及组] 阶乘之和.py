# 解法一
n = int(input())
S = 0
for i in range(1, n+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    S += factorial
print(S)
# 解法二
n = int(input())
S = 0
current_factorial = 1
for i in range(1,n+1):
    current_factorial *= i
    S += current_factorial
print(S)