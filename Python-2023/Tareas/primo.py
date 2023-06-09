#Elaborar un algoritmo para obtener los números primos comprendidos entre 1 y 500.

def primo():
    n=500
    x=2
    primos=[]
    while x != n:
        numdivisores=[]
        for i in range (1,x+1):
            if x%i==0:
                numdivisores.append(i)
        if len(numdivisores)==2:
            primos.append(x)
        x=x+1
    print(primos)

primo()