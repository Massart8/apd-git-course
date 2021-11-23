n=int(input("entrez un entier n: "))
for i in range (1,n):
    div=0
    for j in range (1,i):
        if i%j==0:
            div=div+j
    if div==i:
        print("nbre(s) parfait(s): ",i)
