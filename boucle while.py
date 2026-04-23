mot_de_passe = "ordinateur"
tentatives = 0
while tentatives < 3:
     saisie = input("mot de passe : ")

     if saisie == mot_de_passe:
          print("Acces autorise")
          break
     else:
          print("Incorect")
          tentatives += 1
     
          # Donner des indices
          if tentatives == 1:
             print("Indice : le mot de passe commence par '0' ")   
          elif tentatives == 2:
               print(" Indice: le mot de passe est un mot informatique")
if tentatives == 3:
    print("acce refuser")
            