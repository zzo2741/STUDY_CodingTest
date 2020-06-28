# 구구단
# dan = int(input())
dan = 2
for i in range (1, 10):
    print('{0} * {1} = {2}'.format(dan, i, dan*i))
print()
# A+B-3
count = 5
# count = int(input())
list1 = list()
for i in range (0, count):
    # numStr = input().split(" ")
    numStr = "1 1".split(" ")
    num1 = numStr[0]
    num2 = numStr[1]
    result = int(num1) + int(num2)
    list1.append(result)
for result in list1:
    print(result)
print()
# 합
# num = int(input())
num = 3
result = 0
for i in range(1, num +1):
    result = result + i
print(result)
# 빠른 A+B
import sys
count = 5
# count = int(input())
# list = list()
for _ in range (count):
    # numStr = sys.stdin.readline().rstrip().split(" ")
    numStr = "1 1".split(" ")
    num1 = numStr[0]
    num2 = numStr[1]
    result = int(num1) + int(num2)
    print(result)
print()
# N찍기
# count = int(input())
count = 5
for i in range (1, count+1):
    print(i)
# 기찍N
count = 5
# count = int(input())
for i in range (0, count):
    print(count - i)
print()
# A+B - 7
# 빠른 A+B
import sys
count = 5
# count = int(input())
# list = list()
for i in range (count):
    # numStr = sys.stdin.readline().rstrip().split(" ")
    numStr = "1 1".split(" ")
    num1 = numStr[0]
    num2 = numStr[1]
    result = int(num1) + int(num2)
    print("Case #{0}: {1} + {2} = {3}".format(i+1, num1, num2, result))
print()
# 별 찍기 - 1
start_amount = 5 
# start_amount = int(input())
for i in range (start_amount):
    print("*" * (i+1))
print()
# 별 찍기 - 2
start_amount = 5
# start_amount = int(input())
for i in range (start_amount):
    print(" " * (start_amount - (i+1)) + "*" * (i+1))
print()
# X보다 작은 수
input_data = input().split(" ")
n = int(input_data[0])
x = int(input_data[1])
a = list(map(int, input().split(' ')))

for i in a:
    if x > i:
        print(i)
