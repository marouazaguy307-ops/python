# tableau 
Ref = []
prix = []
taille = []
Qte = []
# procedure saisir un articles 
def saisir_articles ():
        n= int(input("combien d'articles voullez-vous saisir :"))
        for i in range (n):
                print( f" \ narticles {i+1} :")
                R = int (input("la Referances est :"))
                Ref.append(R)
                p=float (input("prix(DH) :")) 
                prix.append(p)
                t=input("la taille (S/M/L/XL):")
                taille.append(t)
                Q=int (input("la qantite en stock :"))
                Qte.append(Q)
# AFICHER STOCK
n=int(input("nombre d'articles" ))
def afficher_stock ():
        saisir_articles()
        for i in range(n):
                print(Ref[i], "\t",taille[i],"\t",prix[i],"\t", "DH","\t" ,Qte[i])
def acheter ():
        sr = int (input(" donner la referance d'articles  "))
        qtd = int ( input(" donner la qantite desir"))
        for i in range(1):
                if Ref [i]==sr :
                        if Qte[i] >= qtd :
                                total = prix[i]* qtd
                                print("la referance est :" , Ref)
                                print(" prix de votre articles est :" , prix)
                                print(" votre total est" , total)
                                print(" qantite restant dans le stock est :" , Qte)
                        else:
                                print("la qantite inssufisant est :" , qtd)
saisir_articles()
afficher_stock()
acheter()


