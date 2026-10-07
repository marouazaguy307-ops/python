joueurs =[]
for i in range (2):
        sous_list=[]
        for j in range(1):
                NJ= int(input("numero de joueurs : "))
                sous_list.append(NJ)
                NM= int(input("nombres de match joués : "))
                sous_list.append(NM)
                NB= int(input("nombres de buts marqués :"))
                sous_list.append(NB)
                NP= int(input("nombres de passes décisives : "))
                sous_list.append(NP)
        joueurs.append(sous_list)
print(joueurs)
def performance (buts, passes, matchs ):
        performance= (buts + passes)/matchs
        return performance
def preferance_max():
        preferance_max=0
        for i in range(len(joueurs)):
                if preferance_max < joueurs[i][1]:
                        preferance_max=joueurs[i][1]        
        print(f"le preferance  max est {preferance_max} :" )
        return preferance_max
