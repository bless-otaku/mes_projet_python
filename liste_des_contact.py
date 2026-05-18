stock = [
    {"nom":"ordinateur","prix":500,"quantite":10},
    {"nom":"souris","prix":15,"quantite":50}
]
def ajouter_produit(nom, prix, qte):
    nouveau = {"nom":nom,"prix":prix,"quantite":qte}
    stock.append(nouveau)
    print(f'le produit {nom} a ete ajouter')


def afficher_stock():
    print("\n---ETAT ACTUEL DES STOCK---")
    for produit in stock:
        print(f"produit:{produit['nom']} | Prix: {produit['prix']}$ | Quantité: {produit['quantite']}")

def calculer_valeur_totale():
    generale_totale = 0
    for produit in stock:
        valeur_produit = produit["prix"] * produit["quantite"]
        generale_total =  generale_total +  valeur_produit
        return  generale_total

