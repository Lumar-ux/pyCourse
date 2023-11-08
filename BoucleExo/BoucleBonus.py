import random
x = random.randint(10,100)
print(x)
play = input("Entrée un nombre entre 10 et 100 : ")
y = int(play)
while True:
    if y < x:
        print("Le nombre est plus petit que le nombre a trouver")
        y = int(input("Entrée un nombre entre 10 et 100 : "))
    elif y > x:
        print("Le nombre est plus grand que le nombre a trouver")
        y = int(input("Entrée un nombre entre 10 et 100 : "))
    elif y == x:
        print("Tu as trouver le nombre")
        break
 
