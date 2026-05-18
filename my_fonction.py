'''def AfficherMessage():
    print("Bonjour! Biemvenue dans le systeme de gestion.")

AfficherMessage()
AfficherMessage()'''

'''def CalculerTTC(prixHT):

    resultat = prixHT * 1.20
    print(f'les prix TTC est{resultat}')
    return resultat
CalculerTTC(100);
CalculerTTC(50);'''

'''def VerifierStock(quantite):
    
    if quantite > 0:
        return True
    elif quantite < 0:
        return False
produit_dispo = VerifierStock(8)

if produit_dispo :
    print('stock suffisant')
elif produit_dispo :
    print('desole')'''


'''def calculer_prix_final(prix_total,est_vip):
    if est_vip and prix_total >= 100:
        prix_final = prix_total * 0.80
    else:
        prix_final = prix_total

    return prix_final
print(calculer_prix_final(120,True))'''


utilisateurs = [15, 22 , 8, 45, 12, 33]
age = 18
'''def analyser_utilisateurs():
    compteur_mineur = 0
    for age in utilisateurs:
        if age < 18:
            compteur_mineur =  compteur_mineur +1
            print( f"Acces Mineur: {age} ans" )
        elif age >= 18:
            print(f"Acces Adulte: {age} ans")
        
        return compteur_mineur'''


emails_bruts = ["test@gmail.com","info@yahoo.fr","admin@gmail.com","contact@outlook.com"]

def filtrer_emails(liste):
    emails_valides = []

    for emails in liste:
        if emails.endswith("@gmail.com"):
            emails_valides.append(emails)
        else:
            print(f'Email rejete : {emails}')
    

    return emails_valides

resultat = filtrer_emails(emails_bruts)
print(f'Emails retenus :{resultat}')