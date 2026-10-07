def moyenne (M1, M2 ,M3 ) :
    moyenne = (M1 + M2 + M3) /3
    return moyenne
def saisir_CANDIDAT(): 
      nom = input ("entrez le nom :")
      SPLT = str(input("quelles ton splt S1 ou bien S2 :"))
      M1 = int(input("entrez la note de la  1er matier"))
      M2 = int(input("entrez la note de la  2eme matier"))
      M3 = int(input("entrez la note de la  3eme matier"))
def valider (SPLT,M1 ,M2 ,M3 ):
  list=[]
  if  SPLT =="S1" or SPLT=="S2 ":

     if M1 != 0 and M2 != 0 and M3 != 0 :
        n =moyenne (M1, M2 ,M3 )
        if  n >= 10 :
            print(" vrai ")
            list.append (n)
def afficher_CANDIDAT( nom , spécialité , moyenne):
    print(nom)
    print(spécialité) 
    print(moyenne)   
for i in range (1)    :
    saisir_CANDIDAT()
    valider()
    moyenne()
    afficher_CANDIDAT()





    

  
        


     
 





    
          











































