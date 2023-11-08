number1 = input("choose the first number : ")
number2 = input("choose the second number : ")
x1 = int(number1)
x2 = int(number2)
sign = input("choose a sign between this one + - / * : ")
if sign == "+":
    print(x1 + x2)
elif sign == "-":
    print(x1 - x2)
elif sign == "/":
    print(x1 / x2)
elif sign == "*":
    print(x1 * x2)
else:
    print("ERROR")