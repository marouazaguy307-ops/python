# passage par valeur : on crée  un copie de b et on  l'affecte a la variable 'a' a et b sont de type int 
" passage par valeur :(type : int , floot , str)"
a = 3
b = 8
a = b
b+=1
print( id(a) ) == id(b)
print(id(b))

#passage par réference : list1 list2 font reference au meme emplacement memoire 
list = [1,2,4,6]
list2 = list
list.append(10)
print( id(list))
print(id(list2))



