destino = input("ingrese destino de llamada: (estados unidos, canada, europa, resto del mundo): ")
duracion = int(input("ingrese la duracion de la llamada por minutos"))


if destino == "estados unidos":
    costo = duracion *  900

if destino == "canada":
    costo = duracion * 800

if destino == "europa":
    costo = duracion * 950

if destino == "resto de mundo":
    costo = duracion * 1250

if duracion > 15:
    des_costo = costo * 0.20
    costo = costo - des_costo

print("el costo de la llamada:", costo)
