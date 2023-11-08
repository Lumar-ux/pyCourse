# Créer une fonction qui va prendre un string et faire 
# en sorte que la premiere lettre soit en majuscule 
# et que le reste soit en minuscule.
str0 = "Salut, comment tu vas ? 42mots quarante-Deux; cinquante+et+un"
def cap(a):
    reponse = a.capitalize()
    return reponse
print(cap(str0))

