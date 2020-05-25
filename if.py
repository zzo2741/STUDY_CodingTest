# 두 수 비교하기
# num = input()
num = "1 2"
num1 = num.split(" ")
A = int(num1[0])
B = int(num1[1])
if(A > B):
    print(">")
elif(A < B):
    print("<")
else:
    print("==")
print()
# 시험 성적
score = 100
# score = int(input())
if(90 <= score and score <= 100):
    print("A")
elif(80 <= score and score <= 89):
    print("B")
elif(70 <= score and score <= 79):
    print("C")
elif(60 <= score and score <= 69):
    print("D")
else:
    print("F")
print()
# 윤년
leapYear = 2000
# leapYear = int(input())
answer = 0
if(leapYear % 4 == 0):
    if(leapYear % 100 != 0 or leapYear % 400 == 0):
        answer = 1;
print(answer)

# 사분면
# x = int(input())
# y = int(input())
x = 9
y = -13
if(0 < x):
    if(0 < y):
        print(1)
    else:
        print(4)
else:
    if (0 < y):
        print(2)
    else:
        print(3)



