# EJ 1
def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo()

# EJ 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

# EJ 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# EJ 4
import math
def calcular_area_circulo(radio):
    # pi * r ** 2
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese un radio: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")

# EJ 5
def segundos_a_horas(segundos):
    return segundos / 60 / 60

segundos = int(input("Ingrese una cantidad de segundos: "))
print(f"La cantidad de horas es: {segundos_a_horas(segundos)}")

# EJ 6
def tabla_multiplicar(numero):
    for x in range(1, 11):
        print(f"{numero}x{x} = {numero*x}")

numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)

# EJ 7
def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    return (suma, resta, multiplicacion, division)

num_A = int(input("Ingrese un número A: "))
num_B = int(input("Ingrese un número B: "))

op = operaciones_basicas(num_A, num_B)

print(f"Resultados SUMA : {op[0]}")
print(f"Resultados RESTA: {op[1]}")
print(f"Resultados MULTI: {op[2]}")
print(f"Resultados DIVIS: {op[3]}")

# EJ 8
def calcular_imc(peso, altura):
    return peso/(altura**2)

peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en M: "))

print(f"El IMC es: {calcular_imc(peso, altura):.2f}")

# EJ 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = float(input("Ingrese una temperatura en Celsius: "))
print(f"La temp en Farenheit es: {celsius_a_fahrenheit(temp_c)}")

# EJ 10
def calcular_promedio(a, b, c):
    return (a+b+c)/3

num_1 = float (input("Ingrese el número 1: "))
num_2 = float (input("Ingrese el número 2: "))
num_3 = float (input("Ingrese el número 3: "))

print(f"El promedio de los tres números es: {calcular_promedio(num_1, num_2, num_3)}")
