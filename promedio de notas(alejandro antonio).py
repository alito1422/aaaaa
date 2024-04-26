nombre=input("ingrese su nombre: ")
nota1=int(input("ingrese nota 1: "))
nota2=int(input("ingrese nota 2: "))
nota3=int(input("ingrese nota 3: "))
 
suma= nota1+nota2+nota3 
div= suma / 3

if div >= 7:
    print ( nombre," esta abrobado con:",div)
elif div >= 4:
    print( nombre," tiene un promedio regular:", div)
else:
    print(nombre, " esta reprobado con: ", div)


