list_principales =[]
def saisir():
        for i in range(4):
                sous_list = []
                n=float(input("le code de patient :"))
                sous_list.append(n)
                temp=float(input("la température pour le patient :"))
                sous_list.append(temp)
                list_principales.append(sous_list)
def Etat_patient(temp):
        
        if temp>=36.5 and temp<=37.5 :
                print("l'etat est normal")
                return "etat est normal"
        else :
                print("l'etat est a survieller")
                return "etat a survieller"
for i in range(4):
        n= list_principales[i][1]
print(Etat_patient (n))

def maximal(list_principales):
        max=list_principales[0][1]
        for i in range(4):
                if max < list_principales[i][1]:
                        max=list_principales[i][1]
                        code=list_principales[i][0]        
        print("la température maximale est:",max)
        print(" le maximale chez le patient:" , code )

def afficher():
        code = int(input("veillez entre le code de patient "))
        for i in range(4):
          if  code ==list_principales[i][0] :
                print(list_principales[i][1])
afficher(list_principales[1])

saisir()
Etat_patient()
maximal()










