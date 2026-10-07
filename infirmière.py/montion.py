list_principales =[]
def moyenne ():
        note = float(input(" veuillez entrez un nombre  :"))
        for i in range(note):
                if note  <= 10 :
                        print(" insuffisant ")
                if note <=10 and note >=12:
                        print( " passable ")
                if note <=12 and note >=14:
                        print( " assez_bien ")
                if note <=14 and note >=16:
                        print( " bien ")
                if note >= 16:
                        print( " tres_bien ")
print(moyenne())

def mention():
        N= float(input("donnez les nombres des eleves :"))
        for i in range(N):
                if N <=10 :
                        print("insuffisant")
                else:
                        print("admis")
mention()


