# EJ 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n 

def mostrar_factorial(n):
    print(f"El factorial de {n} es: {factorial(n)}")
    if n == 1:
        return
    else:
        return mostrar_factorial(n-1)

n = int(input("Ingrese un número:"))
mostrar_factorial(n)


# EJ 2
# pos : 0 1 2 3 4 5 6  7  8
# fibo: 0 1 1 2 3 5 8  13 21
# pos0 -> 0
# pos1 -> 1
# pos2 -> pos1 + pos0 -> 0 + 1 = 1
# pos3 -> pos2 + pos1 -> 1 + 1 = 2
# pos4 -> pos3 + pos2 -> 2 + 1 = 3
# pos5 -> pos4 + pos3 -> 3 + 2 = 5
# pos6 -> pos5 + pos4 -> 5 + 3 = 8
# pos7 -> pos6 + pos5 -> 8 + 5 = 13
def fibo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibo(pos-1) + fibo(pos-2)
    
n = int(input("Ingrese una posición FIBONACCI:"))
for i in range(0, n):
    print(f"El número fibonacci en la posición {i} es: {fibo(i)}")

# EJ 3
# n**m = n * (n **(m-1))
def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m-1)
    
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

# EJ 4
# 24 dec -> bin
# num 24 -> 24 / 2 -> 12 , resto 0
# num 12 -> 12 / 2 -> 6  , resto 0
# num 6  -> 6  / 2 -> 3  , resto 0
# num 3  -> 3  / 2 -> 1  , resto 1
# num 1  -> 1  / 2 -> 0  , resto 1
# 24 dec -> 11000 binario
# dec -> número decimal
# res -> resto actual (str)
def dec_to_bin(dec, res=""):
    if dec >= 1:
        return dec_to_bin(dec//2, str(dec%2) + res)
    else:
        return res

n = int(input("Ingrese un número decimal: "))
p = dec_to_bin(n)
print(f"El resultado de '{n}' dec -> bin, es: {dec_to_bin(n)}")