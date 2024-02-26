cos_matricula = 700.000

nombre = input ("ingrese el nombre del estudiante: ")

nota1  = float(input("ingrese su nota (1 a 5): "))

nota2 = float(input("ingrese su nota (1 a 5): "))

nota3 = float(input("ingrese su nota (1 a 5): "))

nota4 = float(input("ingrese su nota (1 a 5): "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if promedio >= 4:
    print("su promedio es excelente")

elif 3 <= promedio < 4:
    print("su promedio esta bien")

elif 2 <= promedio < 3:
    print("su promedio es deficiente")

if promedio >= 4:
    des_matricula = cos_matricula * 0.20
    cos_matricula = cos_matricula - des_matricula

print(nombre,"su matricula es: ",cos_matricula)




