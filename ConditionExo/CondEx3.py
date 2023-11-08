number = input("Tapez votre âge : ")
x = int(number)
if x >= 18:
    print("Majeur")
elif x <= 0:
   print("NULL") 
else:
    print("Mineur")