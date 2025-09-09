# TP 1 - Estructuras Secuenciales
# Alumno: [Savo Merino]
# Comisión: [08]

# [Ejercicio 1]
# Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".
print("Hola Mundo!")

# --- Ejercicio 2 ---
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla
nombre = input("ingrese su nombre: ")
print(f"¡Hola, {nombre}!")

# --- Ejercicio 3 ---
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
lugar = input("ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# --- Ejercicio 4 ---
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = float(input("ingrese el radio del circulo: "))
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio  

print(f"el area del circulo es {area} y el perimetro es {perimetro}")

# --- Ejercicio 5 ---
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos = int(input("ingrese la cantidad de segundos: "))
horas = segundos // 3600

print(f"{segundos} segundos equivalen a {horas} horas")

# --- Ejercicio 6 ---
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("ingrese un numero: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# --- Ejercicio 7 ---
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("ingrese un numero distinto de 0: "))
numero2 = int(input("ingrese otro numero distinto de 0: "))

suma = numero1 + numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2

print(f"la suma de {numero1} y {numero2} es {suma}")
print(f"la division de {numero1} y {numero2} es {division}")
print(f"la multiplicacion de {numero1} y {numero2} es {multiplicacion}")
print(f"la resta de {numero1} y {numero2} es {resta}")

# --- Ejercicio 8 --- 
#  Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: 𝐼𝑀𝐶 = (𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔) / (altura en m)^2
altura = float(input("ingrese su altura en metros: "))
peso = float(input("ingrese su peso en kg: "))

imc = peso / altura ** 2

print(f"su indice de masa corporal es {imc}")

# --- Ejercicio 9 ---
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝐹 = (𝐶 × 9/5) + 32
celsius = float(input("ingrese la temperatura en grados celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} grados celsius equivalen a {fahrenheit} grados fahrenheit")

# --- Ejercicio 10 ----
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
numero1 = float(input("ingrese un numero: "))
numero2 = float(input("ingrese otro numero: "))
numero3 = float(input("ingrese otro numero: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"el promedio de {numero1}, {numero2} y {numero3} es {promedio}")