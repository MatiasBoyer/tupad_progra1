# EJERCICIO 1
print ("Hola Mundo!")

# EJERCICIO 2
nombre = input("Ingrese su nombre >")
print (f"Hola {nombre}!")

# EJERCICIO 3
nombre = input("Ingrese su nombre >")
apellido = input("Ingrese su apellido >")
edad = input("Ingrese su edad >")
lugar_de_residencia = input("Ingrese su lugar de residencia >")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")


# EJERCICIO 4
radio = float(input("Ingrese el radio de un círculo >"))
area = 3.14159 * (radio ** 2)
perimetro = 3.14159 * radio * 2.0
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# EJERCICIO 5
cant_segundos = int(input("Ingrese una cantidad de segundos >"))
horas = cant_segundos / (60*60)
print (f"{cant_segundos} segundos son {horas} horas.")

# EJERCICIO 6
numero = int(input("Ingrese un número: "))
print (f"{numero}x1 es", numero*1)
print (f"{numero}x2 es", numero*2)
print (f"{numero}x3 es", numero*3)
print (f"{numero}x4 es", numero*4)
print (f"{numero}x5 es", numero*5)
print (f"{numero}x6 es", numero*6)
print (f"{numero}x7 es", numero*7)
print (f"{numero}x8 es", numero*8)
print (f"{numero}x9 es", numero*9)
print (f"{numero}x10 es", numero*10)


# EJERCICIO 7
num_1 = int(input("Ingrese un número distinto de 0: "))
num_2 = int(input("Ingrese un número distinto de 0: "))

print("El resultado de num1+num2 es:", num_1 + num_2)
print("El resultado de num1/num2 es:", num_1 / num_2)
print("El resultado de num1*num2 es:", num_1 * num_2)
print("El resultado de num1-num2 es:", num_1 - num_2)

# EJERCICIO 8
altura = int(input("Ingrese su altura en cm: "))/100
peso = int(input("Ingrese su peso en kg: "))
imc = peso/(altura** 2)

print("Su IMC es:", imc)

# EJERCICIO 9
temp_c = float(input("Ingrese una temperatura en celcius:"))
temp_f = (9/5)*temp_c + 32

print(f"{temp_c} celsius equivale a {temp_f} farenheit")


# EJERCICIO 10
num_promedios = int(input("Ingrese un número:"))
num_promedios += int(input("Ingrese un número:"))
num_promedios += int(input("Ingrese un número:"))

promedio = (num_promedios/3)

print(f"El promedio de esos 3 números es: {promedio}")