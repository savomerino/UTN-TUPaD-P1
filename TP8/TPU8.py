# Práctica de la UNIDAD 8 - Manejo de Archivos
# Alumno: [Savo Merino]
# Comisión: [08]

# [Ejercicio 1]
# Crear archivo inicial con productos
# Se abre el archivo en modo 'w' (escritura).
# Esto crea el archivo si no existe, o lo sobrescribe si ya existe.
print("--- Actividad 1: Creando 'productos.txt' ---")
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,300.0,15\n")
    archivo.write("Goma,80.0,50\n")
print("Archivo 'productos.txt' creado con éxito.")

# [Ejercicio 2]
# Leer y mostrar productos
print("\n--- Actividad 2: Leyendo y mostrando productos ---")
# Se abre el archivo en modo 'r' (lectura).
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        # 1. Quitar el salto de línea (\n) del final
        linea_limpia = linea.strip()
        
        # 2. Separar la línea por las comas para obtener una lista
        partes = linea_limpia.split(",")
        
        # 3. Asignar las partes a variables para mostrarlas
        nombre = partes[0]
        precio = float(partes[1])
        cantidad = int(partes[2])
        
        # 4. Mostrar con el formato solicitado
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# [Ejercicio 3]
# Agregar productos desde teclado
print("\n--- Actividad 3: Agregar nuevo producto ---")
# Pedir los datos al usuario
nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevo_precio = input("Ingrese el precio: ")
nueva_cantidad = input("Ingrese la cantidad: ")

# Se abre el archivo en modo 'a' (append) para añadir al final sin borrar.
with open("productos.txt", "a") as archivo:
    # Escribimos el nuevo producto, asegurándonos de agregar el salto de línea \n
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")
print("Producto agregado con éxito.")

# [Ejercicio 4]
# Cargar productos en una lista de diccionarios
print("\n--- Actividad 4: Cargando datos del archivo a una lista de diccionarios ---")
productos_en_memoria = []
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        partes = linea_limpia.split(",")
        
        # Crear un diccionario por cada producto
        producto_dic = {
            "nombre": partes[0],
            "precio": float(partes[1]),
            "cantidad": int(partes[2])
        }
        # Agregar el diccionario a la lista
        productos_en_memoria.append(producto_dic)

print("Datos cargados en la lista 'productos_en_memoria'.")
# Opcional: imprimir la lista para verificar
# print(productos_en_memoria)

# [Ejercicio 5]
# Buscar producto por nombre
print("\n--- Actividad 5: Buscar un producto en la lista ---")
nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")

encontrado = False
for producto in productos_en_memoria:
    if producto["nombre"].lower() == nombre_buscar.lower():
        print("¡Producto encontrado!")
        print(f"  Nombre: {producto['nombre']}")
        print(f"  Precio: ${producto['precio']}")
        print(f"  Cantidad: {producto['cantidad']}")
        encontrado = True
        break # Detener el bucle una vez encontrado

if not encontrado:
    print(f"Error: El producto '{nombre_buscar}' no existe en la lista.")

# [Ejercicio 6]
# 6: Guardar los productos actualizados
print("\n--- Actividad 6: Guardando la lista de memoria en el archivo ---")
# Se sobrescribe el archivo (modo 'w') con los datos de la lista
with open("productos.txt", "w") as archivo:
    for producto in productos_en_memoria:
        # Reconstruir la línea de texto estilo CSV
        linea_para_guardar = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea_para_guardar)

print("Archivo 'productos.txt' actualizado con todos los datos de la memoria.")
