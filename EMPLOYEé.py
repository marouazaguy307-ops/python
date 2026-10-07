list = [[ 123416 ,"maroua", "zaguy" , "30/07/2007" , "celebataire" ,"CASA20520"] , [ 112233 ,"nour" ,"samar" , "10/07/2007" , "celebataire" , " CASA20550"] , [226789 , "nada" ,"dez" , "16/02/2004" , "celebataire " ,"berchid 26402"]]
def employer ( matricule ) :
    for i in range(3) :
        for j in range (6) :
            if list[i][0]  == matricule :
              print( list[i])
              break

employer(226789)
employer(123416)
employer(112233)
   

