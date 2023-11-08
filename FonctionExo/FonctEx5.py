# Créer une fonction calcul qui prendras trois réponse 
# de l'utilisateur: choisir le premier nombre, choisir 
# l'operateur du calcul, choisir le deuxième nombre 
# de ce calcul. Ensuite, retournez le résultat du calcule 
# selon l'opérateur mathématique choisie.
rep1B = input("Choisi le premier nombre de l'opération : ")
rep2B = input("Choisi le deuxiéme nombre de l'opération : ")
rep1 = int(rep1B)
rep2 = int(rep2B)
signB = input("Choisi l'opérateur de l'opération (+ - * / %) : ")

def opp(a, b, sign):
    if sign == "-":   
        opp1 = a - b
    elif sign == "+":
        opp1 = a - b
    elif sign == "*":
        opp1 = a * b
    elif sign == "/":
        opp1 = a / b
    else:
        print("ERROR")
    return opp1

print(opp(rep1, rep2, signB))