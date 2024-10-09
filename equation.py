solution = 0
a = int(input("valeur de a:"))
b = int(input("valeur de b:"))
c = int(input("valeur de c:"))
max = int(input("valeur maximale de x,y,z:"))

for x in range(1,max):
    for y in range(1,max):
        for z in range(1,max):
            if x*a+yb == z*c:
                print("x=",x,"y=",y,"z=",z)
                solution+=1

if solution == 0:
    print("pas de solution")
else:
    print(solution,"solution trouvées")