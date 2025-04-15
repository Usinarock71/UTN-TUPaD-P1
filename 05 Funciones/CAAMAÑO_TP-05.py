#  1. Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal.

# Definicion de Funciones

def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa Final

imprimir_hola_mundo()

#  2. Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario.

# Definicion de Funciones

def saludar_nombre(nombre):
    print(f"Hola {nombre}!")

# Programa Final

nombre_saludo = input("Ingrese un nombre: ")
saludar_nombre(nombre_saludo)

#  3. Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados.

# Definicion de Funciones

def informacion_personal(nombre, apellido, edad, residencia):
        print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa Final

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

import math

# Definicion de Funciones

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa Final

radio = float(input("Ingrese el radio de un circulo: "))

print("Area:",calcular_area_circulo(radio),"Perimetro:",calcular_perimetro_circulo(radio))

#  5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

# Definicion de Funciones

def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas} horas")

# Programa Final

segundos = int(input("Ingresa la cantidad de segundos: "))
segundos_a_horas(segundos)

#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

# Definicion de Funciones

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(F"{numero} X {i} = {resultado}")
        i += 1

# Programa Final

numero_multiplicar = int(input("Ingrese un numero para calcular su tabla de multiplicar: "))
tabla_multiplicar(numero_multiplicar)

#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

# Definicion de Funciones

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicar = a * b
    dividir = a / b
    print(f"RESULTADOS: \n {a} + {b} = {suma} \n {a} - {b} = {resta} \n {a} X {b} = {multiplicar} \n {a} / {b} = {dividir}")

# Programa Final

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))
operaciones_basicas(num_1, num_2)

#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

# Definicion de Funciones

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Su IMC es: {imc:.2f}")

# Programa Final

peso_usuario = int(input("Ingrese su peso en kilogramos: "))
altura_usuario = float(input("Ingrese su altura en metros: "))
calcular_imc(peso_usuario, altura_usuario)

#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

# Definicion de Funciones

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# Programa Final

celsius_user = float(input("Ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit(celsius_user)

#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

# Definicion de Funciones

def calcular_promedio(a, b, c):
    total = a + b + c
    promedio = total / 3
    print(f"El promedio es: {promedio}")

# Programa Final

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese un ultimo numero: "))
calcular_promedio(num1, num2, num3)