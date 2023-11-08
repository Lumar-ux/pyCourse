# 1.Créer une fonction qui va demander un mot de passe à l'utilisateur.
# 2.si le mot de passe est bon il afficheras un message 
# de Bienvenue sinon il redemanderas le mot de passe en boucle
mdp = input("Tapez votre mot de passe : ")
act = "mdpestlebon"

def modp(act1, new):
        while new != act1:
                        res = "Mauvais mod de passe"
                        new = input("Tapez votre mot de passe : ")
        if new == act1:
                res = "Bienvenue"
        return res

print(modp(act, mdp))