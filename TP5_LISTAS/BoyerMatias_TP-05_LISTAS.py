# EJ 1
lista = list(range(0, 101, 4))[1:]

# EJ 2
lista = [ "A", "B", "C", "D", "E" ]
print(f"Penúltimo: {lista[-2]}")

# EJ 3
lista_vacia = []

lista_vacia.append("Calle")
lista_vacia.append("Esquina")
lista_vacia.append("Cuadra")

# EJ 4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(f"Animales: {animales}")

# EJ 5
# El programa elimina la entrada con el valor más alto, utlizando la función "max" para obtenerlo.

# EJ 6
lista = list(range(10, 31, 5))
print(f"2 primeros: {lista[0:2]}")

# EJ 7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "208"
autos[2] = "fastback"

# EJ 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(f"Resultado: {dobles}")

# EJ 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(f"Compras x cliente: {compras}")

# EJ 10
lista_anidada = [
    15,
    True,
    [ 25.5, 57.9, 30.6 ],
    False
]

print(f"Lista anidada: {lista_anidada}")