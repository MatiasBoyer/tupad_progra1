# EJ 1
precios_frutas = {
    'Banana': 1200, 
    'Ananá':  2500, 
    'Melón':  3000, 
    'Uva':    1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(f"Precios EJ 1: {precios_frutas}")

# EJ 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(f"Precios EJ 2: {precios_frutas}")

# EJ 3
frutas = precios_frutas.keys()
print(f"Frutas: {frutas}")

# EJ 4
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# EJ 5
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# EJ 6
def balanceado(string):
    # Inicializo una pila
    pila = []

    # Por cada caracter, lo agrego a la pila
    for c in string:
        pila.append(c)
    
    # Si la longitud de la pila no es divisible por 2 o 3, es inválida
    if (len(pila) % 2 != 0) or (len(pila) % 3 != 0):
        return False
    
    # Navego por la pila hasta la mitad
    for i in range(int(len(pila)/2)):
        # Obtengo el caracter de la izquierda
        left = pila[i]
        # Obtengo el caracter de la derecha
        right = pila[len(pila)-i-1]
        
        # Si los valores de izquierda O derecha no coinciden, es incorrecto
        if left == '(' and right != ')':
            return False
        if left == '{' and right != '}':
            return False
        if left == '[' and right != ']':
            return False

    # Caso contrario, está OK
    return True

test = "({[]})"
print(f"Prueba balanceado con '{test}': {balanceado(test)}")

test = "({[})"
print(f"Prueba balanceado con '{test}': {balanceado(test)}")

# EJ 7
class TurnosBanco():

    def __init__(self):
        self.cola = []

    def AgregarCliente(self, numero, imprimir_proximo = False):
        self.cola.append(numero)
        if imprimir_proximo:
            self.PrintProximoCliente()

    def AtenderCliente(self, imprimir_proximo = False):
        if len(self.cola) > 0:
            print(f"Cliente atendido: {self.cola[0]}")
            self.cola.pop(0)
            if imprimir_proximo:
                self.PrintProximoCliente()

    def PrintProximoCliente(self):
        if len(self.cola) > 0:
            print(f"Siguiente cliente con número '{self.cola[0]}'")

    def PrintCola(self):
        print(f"COLA: {self.cola}")

turnos = TurnosBanco()
for i in range(20):
    turnos.AgregarCliente(i)

for i in range(20):
    print("\nNueva iteración")
    turnos.PrintCola()
    turnos.AtenderCliente(True)

# EJ 8 y 9
class Nodo:
    anterior = None
    proximo = None
    dato = None

    def __init__(self, dato, anterior, proximo):
        self.dato = dato
        self.anterior = anterior
        self.proximo = proximo

class ListaEnlazada:
    inicio = None

    def __init__(self):
        self.inicio = None

    def AgregarAlFinal(self, dato):
        if self.inicio == None:
            # No hay nodo inicial, creo uno nuevo
            self.inicio = Nodo(dato, None, None)
        else:
            # Obtengo el nodo inicial
            r = self.inicio

            # Voy tomando nodo x nodo, hasta llegar al final
            while r.proximo != None:
                r = r.proximo

            # En el final, indico que el próximo nodo es el nuevo, y el anterior es el presente
            r.proximo = Nodo(dato, r, None)

    def AgregarAlInicio(self, dato):
        if self.inicio == None:
            # No hay nodo inicial, creo uno nuevo
            self.inicio = Nodo(dato, None, None)
        else:
            # Obtengo el nodo de la izquierda de todo
            l = self.inicio
            # Genero un nodo nuevo
            newNodo = Nodo(dato, None, l)

            # Al nodo de la izquierda de todo, le indico que el nodo nuevo es el anterior
            l.anterior = newNodo

            # Actualizo el inicio de la lista, al nodo nuevo
            self.inicio = newNodo

    def InvertirLista(self):
        # Obtengo el último nodo
        r = self.inicio
        while r.proximo != None:
            r = r.proximo

        # Genero un nuevo nodo inicial, partiendo desde la derecha de todo
        newInicio = Nodo(r.dato, None, None)
        newR = newInicio

        # Navego nodo x nodo de derecha a izquierda
        while r.anterior != None:
            # Siempre que exista un nodo anterior en la lista anterior:

            # Obtengo el nuevo nodo de la derecha de todo
            while newR.proximo != None:
                newR = newR.proximo

            # Vuelvo para atrás en la lista original
            r = r.anterior

            # Genero un nodo nuevo
            newR.proximo = Nodo(r.dato, newR, None)
        
        # Completamos reemplazando x la lista nueva
        self.inicio = newInicio


    def ImprimirLista(self):
        if self.inicio == None:
            # Si no hay inicio, la lista está vacía
            print("Lista vacía")
            return

        l = self.inicio
        while l != None:
            # Navego dato por dato

            # Armo una string imprimiendo el dato del nodo
            t = f"Dato: {l.dato}"

            # Si el nodo tiene un dato anterior, lo muestro
            if l.anterior != None:
                t += f" / DatoAnterior: {l.anterior.dato}"

            # Si el nodo tiene un dato posterior, lo muestro
            if l.proximo != None:
                t += f" / DatoPosterior: {l.proximo.dato}"

            # Imprimo
            print(t)

            # Si el nodo tiene un dato posterior, entonces continuamos
            l = l.proximo

# Genero una lista nueva
l = ListaEnlazada()

# Agrego 5 valores al final
for i in range(5):
    l.AgregarAlFinal(i)

# Los imprimo
print("LISTA con AgregarAlFinal")
l.ImprimirLista()

# Agrego 5 valores al inicio
for i in range(5):
    l.AgregarAlInicio(i*-1)

# Los imprimo
print("LISTA con AgregarAlInicio")
l.ImprimirLista()

# Invierto la lista e imprimo
l.InvertirLista()
print("LISTA invertida")
l.ImprimirLista()