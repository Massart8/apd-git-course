import random
nm=random.randint(1,100)
for i in range(1,5):
    print("Essai n°",i)
    n=int(input("veuillez deviner un nbre: "))
    while n!=nm and n<100:
        if n>100:
            print("vous devez entrer un nbre inf à 100")
        if n>nm:
            print("Tres grand!Entrez un autre plus petit ")
            break
        else:
            print("Tres petit!Entrez un autre plus grand")
            if i==5:
                print("Game over!!!le nbre cherché etait",nm)
            break
    if  n==nm:
            print("Vous avez trouvé le nbre Aleatoire")
        





            
       
