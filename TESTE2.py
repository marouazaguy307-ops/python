reponse ="0" 
while reponse == "0" : 
    math = float (input("entre la note de math"))   
    physique = float (input("entre la note de physique"))   
    fr = float (input("entre la note de fr"))   
    svt = float (input("entre la note de svt"))   
    anglais = float (input("entre la note de anglais")) 
    if (math>= 0 and math < 20) and ( physique >=0 and physique < 20 ) and (fr>= 0 and fr< 20 ) and (svt >= 0 and svt < 20 ) and (anglais>= 0 and anglais < 20)  :
        moyenne = (((math + physique)*5) +((anglais + svt))*2 +  (fr*4 ) )
        print("la moyenne est " , moyenne)
        reponse = (input("voulez-vous continue oui(o) /non (n)"  ))
    else:
        print("error")


    



    