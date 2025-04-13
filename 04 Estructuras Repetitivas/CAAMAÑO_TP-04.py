# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for c in range (101):
    print(c)
    c += 1

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

num_entero = int(input("Inserte un número entero: " ))
cont= 0

if num_entero < 0:
    num_entero = abs(num_entero)

while num_entero > 0:
    num_entero = num_entero // 10
    cont += 1

print("La cantidad de digitos del numero ingresado es",cont)


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

num_1 = int(input("Inserte un número: " ))
num_2 = int(input("Inserte otro número: " ))
sumatoria = 0

if num_1 < num_2:
    for c in range(num_1+1, num_2):
        sumatoria += c
elif num_2 < num_1: # Se crea un elif en base a la posibilidad de que el usuario ingrese un numero menor al primero repitiendo el recorrido desde el num_2 hasta num_1
    for c in range(num_2+1, num_1):
        sumatoria += c
else:
    sumatoria = 0 # no hay numeros entre ellos / son iguales

print(sumatoria)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

corte = 0
sumatoria_2 = 0
num_acumulativo = int(input("Ingrese un número entero (0 para cortar el bucle): " ))

while num_acumulativo != corte: # Usando de referencia el metodo de Cimino para que el ciclo no sea infinito
    sumatoria_2 += num_acumulativo # Se acumulan los valores ingresados
    num_acumulativo = int(input("Ingrese otro numero entero: ")) # Se pide el siguiente en bucle

print("El total de la suma de todos los numeros ingresados es",sumatoria_2) # Una vez se ingrese el caracter para cortar el bucle deberia darnos la sumatoria correcta

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

numero_random = random.randint(0, 9)
intento_numero = int(input("Intente adivinar el numero aleatorio (0-9): "))
contador = 1

if intento_numero >= 0 and intento_numero < 10:
    while intento_numero != numero_random:
        print(numero_random)
        contador += 1
        intento_numero = int(input("Has fallado, intentalo de nuevo: "))
    print("¡Adivinaste! tu cantidad de intentos fueron:",contador)
else:
    print("El numero debe estar entre el 0 y el 9")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

num_sumatoria = int(input("inserte un numero entero positivo para sumar todos los que esten entre el y el 0: "))
sumatoria_2 = 0

if num_sumatoria > 0:
    for i in range (0, num_sumatoria):
        sumatoria_2 += i
    print("La suma de todos los numeros entre 0 y el que ingresaste es de ",sumatoria_2)
else:
    print("Error, el numero debia ser positivo.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

# Se inicializan las variables que van a almacenar los valores positivos, negativos, pares e umpares
num_par = 0
num_impar = 0
num_negativo = 0
num_positivo = 0

for i in range(100):
    num_entero = int(input("Ingrese un numero entero cual sea: "))
    if num_entero % 2 == 0: # Se evalua si son pares o no por medio del modulo (resto)
        num_par += 1
    else:
        num_impar += 1

    if num_entero > 0: # Se evalua si son positivos o no por medio de ver si son mayores o no a 0
        num_positivo += 1
    elif num_entero < 0:
        num_negativo += 1

print("La cantidad de numeros positivos fue de:",num_positivo, \
        "La cantidad de negativos fue de",num_negativo, \
        "La cantidad de numeros pares fue de",num_par, \
        "La cantidad de numeros impares fue de",num_impar)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

sumatoria_media = 0

for i in range(100):
    num_entero_2 = int(input("Ingrese un numero entero: "))
    sumatoria_media += num_entero_2 # Se suman los valores ingresados a la sumatoria, acumulandose para el calculo posterior de la media

media = sumatoria_media / 100 # Se calcula la media
print("La media de los 100 valores ingresados es de",media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

num_invertir = int(input("Ingresa un número entero a invertir: "))
invertido = 0

while num_invertir > 0:
    ultimo_digito = num_invertir % 10 # se obtiene el ultimo digito por medio del resto de divirlo por 10
    invertido = invertido * 10 + ultimo_digito # se suman multiplicando primero el valor que se almacene por 10 y luego sumandole el ultimo digito obtenido dando como resultado el numero al reves
    num_invertir = num_invertir // 10 # Se le quita ese digito que ya se obtuvo previamente para seguir con los restantes

print("Número invertido:",invertido)
