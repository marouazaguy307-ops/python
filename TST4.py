#variable global hors fonction  
fil = "dev"
def affiche () :
    # variable local  dans la fonction 
    fil = "infra"
    print(" la fililère " , fil)
affiche()
print(fil)