us = "kodak"
print("Bienvenue dans le jeu du motus")
print("Deviner le mot en 5 tentative\n")
vie = 5
actuel_fix = ""
while vie > 0:
    # print("Mot actuel : " + mot_actuel)
    print("Tentative restantes: " + str(vie))
    motin = input("Entrez un mot en 5 lettre : ")
    if len(motin) != 5:
        print("Introduit un mot en 5 lettre\n")
        vie = vie - 1
        continue
    if motin == us:
        print("Bonne propotition, tu as trouver le motus")
        break
    actuel_tmp = ""
    for i in range(5):
        if motin[i] == us[i]:
            actuel_tmp = actuel_tmp + "[" + motin[i] + "]"
        elif actuel_tmp[i] != " ":
           actuel_fix = actuel_tmp + actuel_tmp
        else:
            actuel_tmp = actuel_tmp + "[_]"
    print("Mauvaise propotition, Mot actuel : " + actuel_tmp + "\n")
    vie = vie - 1
    if vie == 0:
        print("Fin du jeu, Plus aucune vie restant")