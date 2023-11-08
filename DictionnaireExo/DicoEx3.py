# Créez deux dictionnaires contenant des informations 
# sur des étudiants, avec les clés "nom", "âge" 
# et "moyenne". Utilisez une méthode pour fusionner 
# les deux dictionnaires en un seul.
A = {
    "nom" : "Mia",
    "age" : 18,
    "moyenne" : 15
}
B = {
    "nom" : "Myra",
    "age" : 17,
    "moyenne" :  19
}
school = dict(A, **B)
# {
#      "Std1" : A,
#      "Std2" : B
# }
print(school)