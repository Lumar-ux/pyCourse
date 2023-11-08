us = "kodak"
print("Bienvenue dans le jeu du motus")
print("Deviner le mot en 5 tentative\n")
# motview = print("Mot Actuel : [_][_][_][_][_]") 
vie = 5
# print("Tentative restantes: " + str(vie))
# motin = input("Entrez un mot en 5 lettre : ")

while vie > 0:
    print("Tentative restantes: " + str(vie))
    motin = input("Entrez un mot en 5 lettre : ")
    # print("\n")
    if len(motin) != 5:
        print("Chaque mot introduit doivent etre 5 lettre de long\n")
        vie = vie - 1
        continue
    if motin == us:
        print("Bien jouez tu as trouver le motus")
        break
    mot_actuel = ""
    for i in range(5):
        if motin[i] == us[i]:
            mot_actuel = mot_actuel + "[" + motin[i] + "]"
        else:
            mot_actuel = mot_actuel + "[_]"
    print("Mauvaise propotition, Mot actuel : " + mot_actuel + "\n")
vie = vie - 1
if vie == 0:
    print("Plus aucun vie restant")