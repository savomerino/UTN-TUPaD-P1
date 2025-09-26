# TP 5 - Listas
# Alumno: [Savo Merino]
# Comisión: [08]

# [Ejercicio 1]
#  Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

import random

# Crear una lista con las notas al azar de 10 estudiantes
notas = [round(random.uniform(1.0, 10.0), 2) for _ in range(10)]

# muestra la lista completa
print("--- Notas de los estudiantes ---")
for nota in notas:
    print(nota)

# calcula y muestra el promedio
promedio = sum(notas) / len(notas)
print(f"\nEl promedio de las notas es: {promedio:.2f}") # .2f formatea a 2 decimales

# indica la nota más alta y la más baja
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)
print(f"La nota más alta es: {nota_mas_alta}")
print(f"La nota más baja es: {nota_mas_baja}")



# [Ejercicio 2]
# Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista

# 1. pide al usuario que cargue 5 productos
productos = []
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

# 2. muestra la lista ordenada alfabéticamente
print("\n--- Lista de productos ordenada ---")
for producto in sorted(productos): # sorted() devuelve una nueva lista ordenada
    print(producto)

# 3. pregunta qué producto eliminar y actualizar la lista
producto_a_eliminar = input("\n¿Qué producto desea eliminar de la lista?: ")

if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print(f"\n--- Lista final actualizada ---")
    for producto in productos:
        print(producto)
else:
    print("El producto ingresado no se encuentra en la lista.")


# [Ejercicio 3]
# Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

# 1. genera una lista con 15 números enteros al azar
numeros = [random.randint(1, 100) for _ in range(15)]
print("--- Lista de números generada ---")
print(numeros)

# 2. crea una lista con los pares y otra con los impares
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# 3. muestra cuántos números tiene cada lista
print(f"\nHay {len(pares)} números pares:")
print(pares)
print(f"Hay {len(impares)} números impares:")
print(impares)


# [Ejercicio 4]
# Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

for dato in datos:
    if dato not in sin_repetidos:
        sin_repetidos.append(dato)

print("--- Lista original ---")
print(datos)
print("\n--- Lista sin elementos repetidos ---")
print(sin_repetidos)


# [Ejercicio 5]
# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

# 1. crea una lista inicial de estudiantes
estudiantes = ["Ana", "Marcos", "Carlos", "Lucía", "Sofía", "Juan", "Elena", "Pedro"]

print("--- Lista de estudiantes actual ---")
for estudiante in estudiantes:
    print(estudiante)

# 2. pregunta al usuario la acción a realizar
accion = input("\n¿Desea (a)gregar un nuevo estudiante o (e)liminar uno existente?: ").lower()

if accion == 'a':
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
elif accion == 'e':
    estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
    else:
        print("Ese estudiante no está en la lista.")
else:
    print("Opción no válida.")

# 3. muestra la lista final
print("\n--- Lista final de estudiantes ---")
for estudiante in estudiantes:
    print(estudiante)


# [Ejercicio 6]
# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

numeros = [1, 2, 3, 4, 5, 6, 7]
print(f"Lista original: {numeros}")

if len(numeros) > 0:
    # guarda el último elemento
    ultimo_elemento = numeros.pop()
    # inserta el último elemento en la primera posición
    numeros.insert(0, ultimo_elemento)

print(f"Lista rotada: {numeros}")



# [Ejercicio 7]
# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas 
# y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica

import random

# crear una matriz de 7x2 con temperaturas aleatorias (min, max). Para este ejemplo, min entre 5-15 y max entre 16-25
semana = [[random.randint(5, 15), random.randint(16, 25)] for _ in range(7)]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("--- Temperaturas de la semana (Min, Max) ---")
for i in range(len(semana)):
    print(f"{dias[i]}: {semana[i]}")

# 1. calcula promedios de mínimas y máximas
minimas = [dia[0] for dia in semana]
maximas = [dia[1] for dia in semana]

promedio_minimas = sum(minimas) / len(minimas)
promedio_maximas = sum(maximas) / len(maximas)

print(f"\nPromedio de temperaturas mínimas: {promedio_minimas:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maximas:.2f}°C")

# 2. muestra día de mayor amplitud térmica
amplitud_maxima = 0
dia_max_amplitud = ""

for i in range(len(semana)):
    minima = semana[i][0]
    maxima = semana[i][1]
    amplitud = maxima - minima
    
    if amplitud > amplitud_maxima:
        amplitud_maxima = amplitud
        dia_max_amplitud = dias[i]

print(f"El día con mayor amplitud térmica fue el {dia_max_amplitud} con {amplitud_maxima}°C.")


# [Ejercicio 8]
# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

import random

# crear una matriz de 5x3 con notas aleatorias
notas_estudiantes = [[round(random.uniform(4.0, 10.0), 2) for _ in range(3)] for _ in range(5)]
estudiantes = ["Juan", "Ana", "Carlos", "Sofía", "Luis"]
materias = ["Matemática", "Física", "Química"]

print("--- Notas por estudiante ---")
print(notas_estudiantes)

# 1. muestra promedio de cada estudiante
print("\n--- Promedio por estudiante ---")
for i in range(len(notas_estudiantes)):
    promedio_estudiante = sum(notas_estudiantes[i]) / len(notas_estudiantes[i])
    print(f"{estudiantes[i]}: {promedio_estudiante:.2f}")

# 2. muestra promedio de cada materia
print("\n--- Promedio por materia ---")
for j in range(len(materias)):
    suma_materia = 0
    for i in range(len(notas_estudiantes)):
        suma_materia += notas_estudiantes[i][j]
    promedio_materia = suma_materia / len(notas_estudiantes)
    print(f"{materias[j]}: {promedio_materia:.2f}")


# [Ejercicio 9]
# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada

# 1. inicializar el tablero
tablero = [['-' for _ in range(3)] for _ in range(3)]
jugador_actual = "X"

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# bucle principal del juego
for _ in range(9):
    mostrar_tablero(tablero)
    print(f"\nTurno del jugador '{jugador_actual}'")
    
    # bucle para forzar una jugada válida
    while True:
        fila = int(input("Ingrese la fila (0, 1, 2): "))
        columna = int(input("Ingrese la columna (0, 1, 2): "))
        if 0 <= fila < 3 and 0 <= columna < 3:
            if tablero[fila][columna] == '-':
                tablero[fila][columna] = jugador_actual
                break
            else:
                print("Esa casilla ya está ocupada. Intente de nuevo.")
        else:
            print("Fila o columna fuera de rango. Intente de nuevo.")
    
    # cambiar de jugador
    if jugador_actual == "X":
        jugador_actual = "O"
    else:
        jugador_actual = "X"

print("\n--- Tablero final ---")
mostrar_tablero(tablero)


# [Ejercicio 10]
# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

import random

# crear una matriz de 4x7 con ventas aleatorias
ventas = [[random.randint(10, 50) for _ in range(7)] for _ in range(4)]
productos = ["Producto A", "Producto B", "Producto C", "Producto D"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# 1. mostrar total vendido por cada producto
print("--- Total vendido por producto ---")
total_por_producto = [sum(fila) for fila in ventas]
for i in range(len(productos)):
    print(f"{productos[i]}: {total_por_producto[i]} unidades")

# 2. mostrar el día con mayores ventas totales
print("\n--- Día con mayores ventas ---")
ventas_por_dia = [0] * 7
for i in range(len(ventas)):
    for j in range(len(ventas[i])):
        ventas_por_dia[j] += ventas[i][j]

max_ventas_dia = max(ventas_por_dia)
indice_dia_max = ventas_por_dia.index(max_ventas_dia)
print(f"El día de mayores ventas fue el {dias[indice_dia_max]} con {max_ventas_dia} unidades.")

# 3. indicar el producto más vendido en la semana
print("\n--- Producto más vendido de la semana ---")
max_ventas_producto = max(total_por_producto)
indice_producto_max = total_por_producto.index(max_ventas_producto)
print(f"El producto más vendido fue el {productos[indice_producto_max]} con {max_ventas_producto} unidades.")