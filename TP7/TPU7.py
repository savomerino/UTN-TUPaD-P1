# TP 6 - Estructuras de datos complejas
# Alumno: [Savo Merino]
# Comisión: [08]

# [Ejercicio 1]
# Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print(f"Diccionario original: {precios_frutas}")

# Añadir las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"Diccionario actualizado: {precios_frutas}")

# [Ejercicio 2]
# (El diccionario precios_frutas se mantiene del ejercicio anterior)
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f"Diccionario con precios actualizados: {precios_frutas}")

# [Ejercicio 3]
# Crear una lista de frutas (claves)
# (El diccionario precios_frutas se mantiene del ejercicio anterior)
lista_de_frutas = list(precios_frutas.keys())

print("Lista de frutas (claves):")
print(lista_de_frutas)

# [Ejercicio 4]
# Agenda de números telefónicos
contactos = {}

print("Carga de 5 contactos telefónicos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese el número de teléfono de {nombre}: ")
    contactos[nombre] = telefono

print("\n--- Agenda de contactos cargada ---")

# Consultar un contacto
nombre_buscar = input("¿Qué número de contacto desea consultar?: ")

# Usamos 'in' para verificar si la clave existe
if nombre_buscar in contactos:
    print(f"El número de teléfono de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print(f"El contacto '{nombre_buscar}' no se encuentra en la agenda.")

# [Ejercicio 5]
# Analizador de frases (Sets y Diccionarios)
frase = input("Ingrese una frase: ")
# Convertimos la frase a minúsculas y la dividimos en una lista de palabras
palabras = frase.lower().split()

# 1. Palabras únicas (usando un set)
# Convertir la lista a un set elimina automáticamente los duplicados
palabras_unicas = set(palabras)
print(f"\nPalabras únicas: {palabras_unicas}")

# 2. Diccionario con recuento de palabras
recuento_palabras = {}
for palabra in palabras:
    if palabra in recuento_palabras:
        recuento_palabras[palabra] += 1
    else:
        recuento_palabras[palabra] = 1

print(f"Recuento de palabras: {recuento_palabras}")

# [Ejercicio 6]
# Promedio de notas de alumnos (Diccionario y Tuplas)
alumnos = {}

print("Carga de notas para 3 alumnos:")
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    # Pedimos las 3 notas
    nota1 = float(input(f"  Ingrese la nota 1 de {nombre}: "))
    nota2 = float(input(f"  Ingrese la nota 2 de {nombre}: "))
    nota3 = float(input(f"  Ingrese la nota 3 de {nombre}: "))
    
    # Almacenamos las notas en una tupla
    notas_tupla = (nota1, nota2, nota3)
    alumnos[nombre] = notas_tupla

print("\n--- Promedio de cada alumno ---")

# Usamos .items() para recorrer el diccionario y obtener clave y valor
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

# [Ejercicio 7]
# Operaciones de conjuntos (Sets)
# Legajos de estudiantes (ejemplo)
parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {103, 104, 106, 107, 108}

# 1. Aprobaron ambos parciales (Intersección)
aprob_ambos = parcial_1.intersection(parcial_2)
# También se puede usar: aprob_ambos = parcial_1 & parcial_2
print(f"Estudiantes que aprobaron ambos parciales: {aprob_ambos}")

# 2. Aprobaron solo uno de los dos (Diferencia simétrica)
aprob_solo_uno = parcial_1.symmetric_difference(parcial_2)
# También se puede usar: aprob_solo_uno = parcial_1 ^ parcial_2
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {aprob_solo_uno}")

# 3. Total de estudiantes que aprobaron al menos un parcial (Unión)
total_aprobados = parcial_1.union(parcial_2)
# También se puede usar: total_aprobados = parcial_1 | parcial_2
print(f"Lista total de estudiantes que aprobaron (sin repetir): {total_aprobados}")

# [Ejercicio 8]
# Gestor de stock de productos
stock = {"Manzana": 150, "Banana": 100, "Naranja": 200}

while True:
    print("\n--- Gestor de Stock ---")
    print("1. Consultar stock")
    print("2. Agregar stock (o nuevo producto)")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in stock:
            print(f"Hay {stock[producto]} unidades de {producto}.")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")

    elif opcion == '2':
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))

        if producto in stock:
            stock[producto] += cantidad
            print(f"Stock actualizado. {producto} ahora tiene {stock[producto]} unidades.")
        else:
            stock[producto] = cantidad
            print(f"Se agregó el nuevo producto '{producto}' con {cantidad} unidades.")

    elif opcion == '3':
        print("Saliendo del gestor de stock.")
        break
    else:
        print("Opción no válida.")

# [Ejercicio 9]
# Agenda con clave de tupla
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:00"): "Presentación a cliente",
    ("viernes", "11:00"): "Dentista"
}

print("--- Consultar Agenda ---")
dia = input("Ingrese el día (ej: lunes): ").lower()
hora = input("Ingrese la hora (ej: 10:00): ")

# Creamos la tupla que servirá como clave
clave_agenda = (dia, hora)

if clave_agenda in agenda:
    print(f"La actividad programada es: {agenda[clave_agenda]}")
else:
    print("No hay ninguna actividad programada en ese día y hora.")

# [Ejercicio 10]
# Invertir un diccionario
capitales_original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima",
    "Uruguay": "Montevideo"
}

capitales_invertido = {}

# Usamos .items() para obtener la clave (pais) y el valor (capital) en cada iteración
for pais, capital in capitales_original.items():
    capitales_invertido[capital] = pais

print(f"Diccionario original: {capitales_original}")
print(f"Diccionario invertido: {capitales_invertido}")
