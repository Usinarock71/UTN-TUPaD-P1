# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2500

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 

frutas = {"Banana", "Ananá", "Melón", "Uva", "Naranja", "Manzana", "Pera"}

print(frutas)

# 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos 
# nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un 
# mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] 
# años." 

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais}, y tengo {self.edad} años")

persona1 = Persona("Tiziano", "Argentina", 18)
persona1.saludar()

# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y 
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente. 
# Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋. 

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        print(f"Area: {area:.2f}")

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        print(f"Perimetro: {perimetro:.2f}")

radio1 = Circulo(4)
radio1.calcular_area()
radio1.calcular_perimetro()

# 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente 
# balanceados usando una pila. 

def balanceado(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    
    for char in cadena:
        if char in "({[":
            pila.append(char)
        elif char in ")}]":
            if not pila or pila.pop() != pares[char]:
                return False
    return not pila

# 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir: 
# ● Agregar clientes (encolar). 
# ● Atender clientes (desencolar). 
# ● Mostrar el siguiente cliente en la fila.

from collections import deque

class Banco:
    def __init__(self):
        self.cola = deque()

    def encolar(self, cliente):
        self.cola.append(cliente)
        print(f"{cliente} ha tomado un turno.")

    def desencolar(self):
        if self.cola:
            atendido = self.cola.popleft()
            print(f"Atendiendo a {atendido}")
        else:
            print("No hay clientes en espera.")

    def siguiente(self):
        if self.cola:
            print(f"Siguiente cliente: {self.cola[0]}")
        else:
            print("No hay clientes en la fila.")

banco = Banco()
banco.encolar("Tiziano")
banco.encolar("Martina")
banco.siguiente()
banco.desencolar()
banco.siguiente()

# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar 
# los valores almacenados. 

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

lista = ListaEnlazada()
lista.insertar_inicio(10)
lista.insertar_inicio(20)
lista.insertar_inicio(30)
lista.mostrar()

# 9) Dada una lista enlazada, implementa una función para invertirla. 

def invertir_lista(lista):
    anterior = None
    actual = lista.cabeza

    while actual:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    lista.cabeza = anterior

invertir_lista(lista)
lista.mostrar()