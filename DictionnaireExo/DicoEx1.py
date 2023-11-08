# Créez un dictionnaire contenant des informations 
# sur une personne, avec les clés "nom", "âge" et "ville". 
# Utilisez une méthode pour obtenir la liste des clés du 
# dictionnaire.
dico = {
    "nom" : "lucas",
    "âge" : 22,
    "ville" : "Bruxelle" 
}
for cle in dico.keys():
    print(cle)