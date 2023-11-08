us = "kodak"
print("Bienvenue dans le jeu du motus")
print("Deviner le mot en 5 tentative\n")
motview = print("Mot Actuel : [_][_][_][_][_]") 
vie = 5
# j = 0
print("Tentative restantes: " + str(vie))
motin = input("Entrez un mot en 5 lettre : ")
lt = []
lt.append(motin)
lettre = list(lt)
print(lettre)

while lt != us and vie > 0
    vie = vie - 1
    i = 0
    while j < 5:
        lt[j] = us[j]
        print(lt)
        j = j + 1
    print("Bienvenue dans le jeu du motus")
    print("Deviner le mot en 5 tentative\n")
    #[""]
    motview2 = print("Mot Actuel : ["+ lt[j] + "]"+"["+lt[j]+"]"+"["+lt[j]+"]"+"["+lt[j]+"]"+"["+lt[j]+"]")
    print("Tentative restantes: " + str(vie))
    motin2 = input("Entrez un mot en 5 lettre : ")
    print("\n")
   # while 
if vie == 0:
    print("Plus aucun vie restant")
if lt == us:
    print("Bien jouez tu as trouver le motus")
