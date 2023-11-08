us = "kodak"
print("Bienvenue dans le jeu du motus")
print("Devinez le mot en 5 tentatives\n")

vie = 5
actuel_fix = ["_"] * len(us)  # Initialise la liste des lettres fixes avec des underscores

while vie > 0:
    print("Tentative restantes: " + str(vie))
    print("Mot actuel : " + "".join(actuel_fix))  # Affiche le mot avec les lettres trouvées jusqu'à présent
    motin = input("Entrez un mot de 5 lettres : ")

    if len(motin) != 5:
        print("Veuillez introduire un mot de 5 lettres.\n")
        continue

    if motin == us:
        print("Bonne proposition, vous avez trouvé le motus!")
        break

    actuel_tmp = ""
    for i in range(5):
        if motin[i] == us[i]:
            actuel_tmp += "[" + motin[i] + "]"
            actuel_fix[i] = motin[i]  # Mise à jour de la liste des lettres fixes
        else:
            actuel_tmp += "[" + actuel_fix[i] + "]"  # Utilise les lettres fixes déjà découvertes

    print("Mauvaise proposition, mot actuel : " + actuel_tmp + "\n")
    vie -= 1

    if vie == 0:
        print("Fin du jeu, plus aucune vie restante. Le mot était : " + us)
