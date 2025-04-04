# ACT 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# ACT 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# ACT 3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("Por favor, ingrese un número par")

# ACT 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

# ACT 5
contrasena = input("Ingrese la contraseña: ")
if 8 <= len(contrasena) and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ACT 6
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

import statistics

moda = statistics.mode(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)

# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")

# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
if media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")

# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
if media == mediana and mediana == moda:
    print("Sin sesgo")


# ACT 7
texto = input("Ingrese una frase o palabra:")

if texto[-1].upper() in ["A", "E", "I", "O", "U"]:
    print(texto + "!")
else:
    print(texto)

# ACT 8
nombre = input("Ingrese su nombre: ")
print ("Elija una opción:")
print ("1. Mayúsculas")
print ("2. Minúsculas")
print ("3. Primera letra mayúscula")
opcion = int(input("Opción: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción  inválida")

# ACT 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
    print("imperceptible")
elif 3 <= magnitud < 4:
    print("Leve")
    print("ligeramente perceptible")
elif 4 <= magnitud < 5:
    print("Moderado")
    print("sentido por personas, pero generalmente no causa daños")
elif 5 <= magnitud < 6:
    print("Fuerte")
    print("puede causar daños en estructuras débiles")
elif 6 <= magnitud < 7:
    print("Muy fuerte")
    print("puede causar daños significativos")
elif 7 <= magnitud:
    print("Extremo")
    print("puede causar graves daños a gran escala")

# ACT 10
hemisferio = input("¿Qué hemisferio es? (N/S): ").upper()
mes = int(input("Qué mes es? (1-12): "))
dia = int(input("Qué día es? (1-31): "))

print(f"La estación para el {dia}/{mes} en el hemisferio {hemisferio} es:")

# desde el 21 de dic hasta el 20 de marzo
# invierno en N, verano en S
if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        print("Invierno")
    elif hemisferio == "S":
        print("Verano")

# desde el 21 de marzo hasta el 20 de junio
# primavera en N, otoño en S
if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        print("Primavera")
    elif hemisferio == "S":
        print("Otoño")

# desde el 21 de junio hasta el 20 de septiembre
# verano en N, invierno en S
if (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        print("Verano")
    elif hemisferio == "S":
        print("Invierno")

# desde el 21 de septiembre hasta el 20 de diciembre
# otoño en N, primavera en S
if (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        print("Otoño")
    elif hemisferio == "S":
        print("Primavera")