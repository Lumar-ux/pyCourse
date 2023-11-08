# Créez un dictionnaire contenant des noms de fruits 
# et leurs quantités. Utilisez une méthode pour obtenir 
# le nombre total de fruits dans le dictionnaire.
dico = {
    "pomme" : 2,
    "apple" : 4,
    "orange" : 6
}
value = dico.values()
print(sum(value))