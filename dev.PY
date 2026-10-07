def MAX (note1 ,note2, note3, note4 ):
    sum=note1 + note2 + note3 + note4
    if note1 < note2  and note3 < note2 and note4 < note2:
         MAX = note2
    if note2 < note1  and note3 < note1 and note4 < note1:
         MAX = note1
    if note1 < note3  and note2 < note3 and note4 < note3:
         MAX = note3
    if note1 < note4  and note3 < note4 and note2 < note4:
         MAX = note4
    return MAX
#appel a la fonction 
print(MAX(2,55,90,8))
max= MAX(34,56,78,90)


