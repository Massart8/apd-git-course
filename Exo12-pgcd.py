a=int(input("entrez un nbre: "))
b=int(input("entrez un autre nbre: "))
if a>b:
    nmin=a
else:
    nmin=b
for i in range(1,nmin+1):
    if a%i==0 and b%i==0:
        pgcd=i
print("le pgcd de",a,"et",b,"est",pgcd)
