# TP 4 - Estructuras Repetitivas
# Alumno: [Savo Merino]
# Comisión: [08]


# [Ejercicio 1]
#  Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


# [Ejercicio 2]
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un numero entero: "))
cantidad_digitos = 0

while numero > 0:
    numero //= 10
    cantidad_digitos += 1

print(f"La cantidad de digitos es: {cantidad_digitos}")


# [Ejercicio 3]
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

suma = 0

inicio = min(num1, num2)
fin = max(num1, num2)

for i in range(inicio + 1, fin):
    suma += i

print(f"La suma de los numeros entre {num1} y {num2} es: {suma}")


# [Ejercicio 4]
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando 
# el usuario ingrese un 0.

suma_total = 0
while True:
    numero = int(input("Ingrese un numero entero: (ingrese 0 para terminar)"))
    if numero == 0:
        break #si el numero es cero se rompe el bucle
    suma_total += numero

print(f"La suma total es: {suma_total}")


# [Ejercicio 5]
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

print("Adivina el numero entre 0 y 9")

while not adivinado:
    intento_usuario = int(input("Ingrese un numero: "))
    intentos += 1
    if intento_usuario == numero_secreto:
        adivinado = True
    elif intento_usuario < numero_secreto:
        print("El numero es mayor")
    else:
        print("El numero es menor")

print(f"Adivinaste el numero en {intentos} intentos")  


# [Ejercicio 6]
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)


# [Ejercicio 7]
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un numero entero positivo: "))
suma = 0

for i in range(numero + 1):
    suma += i

print(f"La suma de los numeros entre 0 y {numero} es: {suma}")


# [Ejercicio 8]
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio)

# Se usa una cantidad menor para facilitar la prueba
cantidad_numeros = 10 # Cambiar a 100 para la versión final

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Por favor, ingrese {cantidad_numeros} números enteros.")

for i in range(cantidad_numeros):
    numero = int(input(f"Número {i+1}: "))
    
    # Clasificación por signo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    
    # Clasificación por paridad
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n--- Resultados ---")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")



# [Ejercicio 9]
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 10 # Cambiar a 100 para la versión final
suma_de_numeros = 0

print(f"Por favor, ingrese {cantidad_numeros} números enteros.")

for i in range(cantidad_numeros):
    numero = int(input(f"Número {i+1}: "))
    suma_de_numeros += numero

media = suma_de_numeros / cantidad_numeros

print(f"\nLa media de los números ingresados es: {media}")


# [Ejercicio 10]
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_original = int(input("Ingrese un número entero para invertir: "))
numero_invertido = 0
numero_temp = numero_original # Usamos una copia para no perder el original

while numero_temp > 0:
    # Obtenemos el último dígito
    ultimo_digito = numero_temp % 10
    
    # Añadimos el último dígito al número invertido
    numero_invertido = (numero_invertido * 10) + ultimo_digito
    
    # Quitamos el último dígito del número original
    numero_temp //= 10

print(f"El número {numero_original} invertido es: {numero_invertido}")