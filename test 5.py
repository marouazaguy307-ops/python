referance = []
prix = []
Qte = []
def saisir_produit():
    for i in range(3) :
        print(f"nproduit{i+ 1} :")
        r=int(input("referance : "))
        p = float( input(" prix :" , "DH"))
        q = int(input(" quantite:" , "kg"))
        referance.append(r)
        prix.append(p)
        Qte.append(q)
saisir_produit()
def afiicher_produit():
         print("les referance des produits :",referance)
         print("les prix de prouduits :",prix)
         print("la quantite de produit:", Qte)
afiicher_produit()
def commande ():
      print("nouvelle commande ")
      referance=int(input("referance du produit"))
      Qte=int(input("quantite"))
      if referance in referance:
            i=referance.__index__(referance)
            if Qte [i] >=Qte:
                  total = prix[i]*Qte

                  print("commande acceptee")
                  print("prix total :",total)
                  print("quantite restante :",Qte[i] )
      else :
            print("stock insuffisant ")
commande()
def rechercher_produit(r):
      for i in range (len(referance)):
            if referance[i] == referance : 
                  print("produit introuvable ")
            return r
            
                                                                                                                                                                                                        