# 고양이
print("\    /\ ")
print(" )  ( ') ")
print("(  /  ) ")
print(" \(__)| ")
print()
# 개
print("|\_/| ")
print("|q p|   /} ")
print('( 0 )"""\ ')
print('|"^"`    | ')
print("||_/=\\\__| ")
print()
# A+B
numStr = "1 2"
num = numStr.split(" ")
print(int(num[0]) + int(num[1]))
print()
# A-B
numStr = "3 2"
num = numStr.split(" ")
print(int(num[0]) - int(num[1]))
print()
# A*B
numStr = "3 2"
num = numStr.split(" ")
print(int(num[0]) * int(num[1]))
print()
# A/B
numStr = "1 3"
num = numStr.split(" ")
print(int(num[0]) / int(num[1]))
print()
# 사칙연산
numStr = "7 3"
num = numStr.split(" ")
print(int(num[0]) + int(num[1]))
print(int(num[0]) - int(num[1]))
print(int(num[0]) * int(num[1]))
print(int(int(num[0]) / int(num[1])))
print(int(num[0]) % int(num[1]))
print()
# 나머지
numStr = "5 8 4"
num = numStr.split(" ")
A = int(num[0])
B = int(num[1])
C = int(num[2])
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print( ((A%C)*(B%C))%C)
print()
# 곱셈

# numStr1 = "472"
# numStr2 = "385"
numStr1 = input()
numStr2 = input()
num1 =  int(numStr1)
i = 2
gob = 1
result = 0
while i>=0:
    gobNum1 = (num1 * int(numStr2[i])) * gob
    gobNum2 = (num1 * int(numStr2[i]))
    i = i - 1
    gob = gob * 10
    result = result + gobNum1
    print(gobNum2)
print(result)


