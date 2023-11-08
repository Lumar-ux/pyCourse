number = input("Tapez un nombre pour une vérification : ")
x = int(number)
if x % 2:
    print("x est impair")
elif x == 0:
    print("x est NULL")
else:
    print("x est pair")