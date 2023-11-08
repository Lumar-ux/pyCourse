number = input("Tapez un nombre pour une vérification du signe : ")
x = int(number)
if x > 0:
    print("x est positif")
elif x == 0:
    print("x est null")
else:
    print("x est négatif")