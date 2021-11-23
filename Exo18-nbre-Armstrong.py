n=int(input("entrez un nbre: "))
c=n//100
d=n%100//10
u=n%100%10
if (c**3)+(d**3)+(u**3)==n:
    print(True)
else:
    print(False)
