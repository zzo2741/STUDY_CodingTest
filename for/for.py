# 구구단
# dan = int(input())
dan = 2
for i in range (1, 10):
    print('{0} * {1} = {2}'.format(dan, i, dan*i))
print()
# A+B-3
count = 5
# count = int(input())
list = list()
for i in range (0, count):
    # numStr = input().split(" ")
    numStr = "1 1".split(" ")
    num1 = numStr[0]
    num2 = numStr[1]
    result = int(num1) + int(num2)
    list.append(result)
for result in list:
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
# count = 5
count = int(input())
# list = list()
for _ in range (count):
    numStr = sys.stdin.readline().rstrip().split(" ")
    # numStr = "1 1".split(" ")
    num1 = numStr[0]
    num2 = numStr[1]
    result = int(num1) + int(num2)
    print(result)
print()

