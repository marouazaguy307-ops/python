N1= int(input("entrez le premier nombre"))
N2 = int(input(" entrez le deuxième nombre"))
N3 = int(input("rntrez le troisième nombre"))
if(N1 == N2 + N3 or N2 == N3 + N1 or N3 == N2 + N1) :
    if(N1 == N2 + N3 ) :
        print("validée")
    if( N2 == N3 + N1 ) :
        print("validée")
    if (N3 == N2 + N1) :
        print("validée")
else : 
    print("error")
     
       

if(N1 == N2 + N3 ) :
    print("validée")
elif ( N2 == N3 + N1 ) :
    print("validée")
elif (N3 == N2 + N1) :
    print("validée") 
else :
    print("error")
       
    