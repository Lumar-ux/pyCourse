number1 = input("choose third number : ")
number2 = input("choose third number : ")
number3 = input("choose third number : ")
v1 = int(number1)
v2 = int(number2)
v3 = int(number3)
x1 = [v1, v2, v3]
x1.sort()
if x1[2] % 2 == 0:
    print(x1[2]/2)
else:
    print(x1[2]*2)