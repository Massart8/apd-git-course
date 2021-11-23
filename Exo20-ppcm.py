a=int(input("entrez un nbre: "))
b=int(input("entrez un autre nbre: "))
if a>b:
    pg=a
else:
    pg=b
i=a*b
while i>=pg:
    if i%a==0 and i%b==0:
        ppcm=i
    i=i-1
print("le ppcm de",a,"et",b,"est",ppcm)
