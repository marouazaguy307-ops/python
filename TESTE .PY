reponse = "0"
somme = 0
M = 0 
while True  :
    n_n = int(input("entre nombre des note "))
    for i in range (0 , n_n) :
        note =float(input ("entre vote note")) 
        coefficien =int(input ("entre vote coefficien")) 
        M += note*coefficien  
        somme += coefficien
    moyenne = (M) / somme
    print ("votre moyenne est :" , moyenne)
    reponse = input("voullez continue oui(o) / non(n)")
    if reponse =="n":
        break

    
    