list=[]
moyenne =None
while  True:
 n = int(input( "entrez un nombre "))
if n > 0 and n <= 10:
     print(" le valeur de T :")
for i in range(1, n) :
    sum = sum + n
print("la somme des element est :" , sum)
moyenne = sum/n
print(" la moyenne des element est :" , moyenne)
