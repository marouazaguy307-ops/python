N = 3
max = 1 
M = 0
while  N != 0 :
       N =  float(input ("entrez un nombre "))
       M += 1
       if max < N :
              max= N  
              position= M
       if N == 0 :
              break
print ( max,"le plus grand nombre est sa position   :" ,  position )





              
