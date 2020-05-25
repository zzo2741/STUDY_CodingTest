num = input()
num1 = num.split(" ")
A = int(num1[0])
B = int(num1[1])

if(A > B):
    print(">")
elif(A < B):
    print("<")
else:
    print("==")
