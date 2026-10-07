list1= []
max=0
nombre_repèter =0
positon =[]
for i in range(10):
    N= int(input(f"entrez un nombre {i+1} :"))
    list1.append(N)
    if N > max:
        max=N

for i in range(len(list1)):
    if list1[i] == max :
        nombre_repèter=list1.count(max)
        positon.append(i + 1)
print()
print("le plus grand nombre est:",max)
print("tabl:",list1)
print("rèpetè:" ,nombre_repèter, "fois") 
print("sa position est:",positon)       









