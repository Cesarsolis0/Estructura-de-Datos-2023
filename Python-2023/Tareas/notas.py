#Diseña un programa que, dado un número real que debe representar la calificación
#numérica de un examen, proporcione la calificación cualitativa correspondiente al número
#dado. La calificación cualitativa será una de las siguientes: “Reprobado” (nota menor a 4,0),
#“Aprobado” (nota mayor a 4,0, pero menor a 5,0), “Notable” (nota mayor a 5,0 pero menor a
#6,0), “Sobresaliente” (nota mayor a 6,0)

x=float(input("ingrese el valor de la nota:"))

def nota(x):
    if x >= 1 and x < 4:
        print ("usted a reprobado")
    elif x >= 4 and x < 5:
        print("usted a aprobado")
    elif x>= 5 and x < 6:
        print("su nota fue notable")
    elif x>=6 and x<=7:
        print("su nota fue sobresaliente")
    
nota(x)
    