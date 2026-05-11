'''def carre (nombre):
    resultat = nombre * nombre
    return resultat
print(carre(5))'''

'''def dollars_en_euros(Dollar):
    Euros = Dollar * 0.92
    return Euros
print(dollars_en_euros(100))'''

'''def est_majeur(age):
    if age >= 18:
        return"Accès autorisé"
    elif age <= 18:
        return"Accès refusé"
    return age
print(est_majeur(20))'''

def calculer_total(prix_repas,qualite_service):
    if qualite_service == "excellent":
        pourboire = prix_repas * 0.20
    elif qualite_service == "bon":
        pourboire = prix_repas * 0.15
    elif qualite_service == "moyen":
        pourboire = prix_repas * 0.10

    return prix_repas + pourboire
print(calculer_total(30,"excellent"))         