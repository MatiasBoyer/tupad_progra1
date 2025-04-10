# EJ 1
for i in range(-1, 101):
    print(i)

# EJ 2
numero = int(input("Ingrese un número:"))
cant_digitos = 0
while numero != 0:
    numero = int(numero/10)
    cant_digitos += 1
print(f"El número tiene {cant_digitos} dígitos.")

# EJ 3
num1 = int(input("Ingrese el número menor:"))
num2 = int(input("Ingrese el número mayor:"))
res = 0
for i in range(num1, num2):
    res += i
print(f"El resultado es {res}")

# EJ 4
res = 0
num = -1
while num != 0:
    num = int(input("Ingrese un número (0 para detener):"))
    res += num
print(f"Total acumulado: {res}")

# EJ 5
import random

print("Adivine el número")
num = random.randint(0, 9)
intentos = 1
while int(input("Ingrese un número:")) != num:
    intentos += 1
print(f"Correcto!! Se necesitaron {intentos} intentos para adivinarlo.")

# EJ 6
for i in range(101, -1, -1):
    if i % 2 == 0:
        print(i)

# EJ 7
num = int(input("Ingrese un número:"))
res = 0
for i in range(num+1):
    res += i
print(f"La suma es: {res}")

# EJ 8
pares = 0
impares = 0
negativos = 0
positivos = 0

ingresados = 0

while ingresados < 100:
    num = int(input("Ingrese un número: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

    ingresados += 1

print("Cantidad de IMPARES:", impares)
print("Cantidad de PARES:", pares)
print("Cantidad de POSITIVOS:", positivos)
print("Cantidad de NEGATIVOS:", negativos)

# EJ 9
total = 0
ingresados = 0
while ingresados < 100:
    num = int(input("Ingrese un número: "))
    total += num
    ingresados += 1

media = total/ingresados
print(f"La media es: {media}")

# EJ 10
numero = int(input("Ingrese un número:"))

# Obtengo la cantidad de dígitos
num = numero
cant_digitos = 0
while num != 0:
    num = int(num/10)
    cant_digitos += 1

numero_reversado = 0
for i in range(cant_digitos):
    # Toma el dígito de la derecha, uno a la vez
    digito = (numero//(10**i)) % 10

    # Obteno la unidad dependiendo la posición, y la multiplico por el número.
    # El resultado se suma a 'numero_reversado'
    numero_reversado += (10**(cant_digitos-i-1))*digito

print(numero_reversado)