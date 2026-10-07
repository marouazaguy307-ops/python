"""
[1,3,5,4,2] = [1,2,3,4,5]
[1,3,4,2,5]
[1,3,2,4,5]
[1,2,3,4,5]

"""
def tri_a_bulle(L) :
    n = len(L)
    for i in range (n-1) :
        for j in range(n-i-1) :
            if L[j] > L[j+1] :
                L[j],L[j+1] = L[j+1],L[j]
L=[2004,16,2,30,7, 2007]
tri_a_bulle(L)
print(L)


def tri_par_insertion(L) :
    for i in range( 1,len(L)) :
        cle = L[i]
        j=i-1
        while j >= 0 and cle < L[j] :
            L[j],L[j+1] = L[j+1],L[j]
            j-=1
L= [12,14,78,2004,189,367,564,9000 ]    
tri_par_insertion(L)
print(L)       


    
        
 
    




