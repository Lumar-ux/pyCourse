us = "kodak"
print("Bienvenue dans le jeu du motus")
print("Devinez le mot en 5 tentatives\n")

vie = 5
actuel_fix = [" "] * len(us)  # Initialise tableau fixes
while vie > 0:
    print("Tentative restantes: " + str(vie))
    print("Mot actuel : " + "[" + "".join(actuel_fix) + "]")  # Affiche tableau fix en un seul mots
    motin = input("Entrez un mot de 5 lettres : ")

    if len(motin) != 5:
        print("Veuillez introduire un mot de 5 lettres.\n")
        vie = vie - 1
        continue

    if motin == us:
        print("Bonne proposition, vous avez trouvé le motus!")
        break

    actuel_tmp = "" # Initialise tableau tmp
    for i in range(5):
        if motin[i] == us[i]:
            actuel_tmp = actuel_tmp +  motin[i]
            actuel_fix[i] = motin[i]  # Mise à jour lettres fixes
        elif actuel_fix[i] != " ":
            actuel_tmp = actuel_tmp + actuel_fix[i] # Utilise les lettres fixes déjà découvertes
        else:
             actuel_tmp = actuel_tmp + "[_]"
    print("Mauvaise proposition, mot actuel : " + "[" + actuel_tmp + "]" + "\n")
    vie = vie - 1

    if vie == 0:
        print("Fin du jeu, plus aucune vie restante. Le mot était : " + us)
