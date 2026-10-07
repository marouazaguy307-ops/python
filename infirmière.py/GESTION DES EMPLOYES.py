list_employe=[]
for i in range(2):
        sous_list=[]
        for j in range(1):
                code =int(input("entrez le code de l'employeé :"))
                sous_list.append(code)       
                h=int(input("le nombre d'heures dans la semaine :")) 
                sous_list.append(h)       
                S=float(input("salaire horaire:"     "euros"))
                sous_list.append(S) 
                list_employe.append(sous_list)  
print(list_employe)
def maximal():
        salaire_max=0
        for i in range(len(list_employe)):
                if salaire_max < list_employe[i][1]:
                        salaire_max= list_employe[i][1]        
        print(f"le salaire max est {salaire_max} :" )
        return salaire_max
maximal()
def Etat_employe(code):
        cd= float(input("veillez entre le code d'employé:"))
for i in range(2):
        if  code == list_employe[i][0] :
                print(list_employe[i][1])
Etat_employe (sous_list[1])
def salaire():
        heures_salaires=float(input("le nombre d'heures travailles"))
        sous_list.append(heures_salaires)
        salaire_hebdomaire=int(input("son salaire hebdomadaire "))
        sous_list.append(salaire_hebdomaire)
        if salaire>=300 :
                print("bien payé")
        else:
                print("a ameliorer")
salaire()



                     
               

                


