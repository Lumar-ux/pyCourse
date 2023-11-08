us = "kodak"
print("Bienvenue dans le jeu du motus")
print("Devinez le mot en 5 tentatives\n")

vie = 5
actuel_fix = ["_"] * len(us)  # On initialise le tableau des lettres fixes avec des underscores

while vie > 0:
    print("Tentative restantes: " + str(vie))
    # On affiche le mot actuel avec des espaces entre les lettres pour une meilleure lisibilité
    print("Mot actuel : " + " ".join(actuel_fix))

    motin = input("Entrez un mot de 5 lettres : ")

    if len(motin) != 5:
        print("Veuillez introduire un mot de 5 lettres.\n")
        continue

    if motin == us:
        print("Bonne proposition, vous avez trouvé le motus!")
        break

    actuel_tmp = []  # On utilise une liste pour construire le mot temporaire
    for i in range(5):
        if motin[i] == us[i]:
            actuel_tmp.append(motin[i])  # On ajoute la lettre trouvée
            actuel_fix[i] = motin[i]  # Mise à jour des lettres fixes
        else:
            actuel_tmp.append("_")  # On ajoute un underscore pour une lettre non trouvée

    # On affiche le mot temporaire avec des crochets pour indiquer les lettres non trouvées
    print("Mauvaise proposition, mot actuel : " + " ".join(["[" + char + "]" if char != "_" else "[_]" for char in actuel_tmp]))
    print("\n")
    vie -= 1

    if vie == 0:
        print("Fin du jeu, plus aucune vie restante. Le mot était : " + us)
