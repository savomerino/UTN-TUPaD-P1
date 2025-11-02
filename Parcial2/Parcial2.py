#============================#
# PROGRAMACION 1 - PARCIAL 2 #
# Alumno: Savo Merino        #
# Comisión: 08               #
#============================#

#INICIO DEL PROGRAMA
#BIBLIOTECA CSV v2.0

import csv
import os

# Constante para el nombre del archivo
NOMBRE_ARCHIVO = "catalogo.csv"

# --- Funciones de Persistencia (CSV) ---

def cargar_catalogo_csv():
    """
    Carga el catálogo desde catalogo.csv al iniciar el programa.
    Si el archivo no existe, lo crea con encabezado y devuelve una lista vacía.
    """
    catalogo = []
    ruta = os.path.join(os.path.dirname(__file__), NOMBRE_ARCHIVO)

    # Si no existe, crear archivo con encabezado y devolver catálogo vacío
    if not os.path.exists(ruta):
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["TITULO", "CANTIDAD"])
        print(f"No se encontró '{NOMBRE_ARCHIVO}'. Se creó '{NOMBRE_ARCHIVO}' en la carpeta del script.")
        return catalogo

    # Si existe, leerlo de forma robusta
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        filas = list(lector)

        if not filas:
            print(f"El archivo '{NOMBRE_ARCHIVO}' está vacío.")
            return catalogo

        # Detectar encabezado (opcional, insensible a mayúsculas)
        inicio = 0
        primera = filas[0]
        if len(primera) >= 2 and primera[0].strip().lower() == "titulo" and primera[1].strip().lower() == "cantidad":
            inicio = 1

        for fila in filas[inicio:]:
            if len(fila) < 2:
                # Omitir filas mal formadas
                continue
            titulo = fila[0].strip()
            cantidad_str = fila[1].strip()
            if not cantidad_str.lstrip('-').isdigit():
                # Omitir si la cantidad no es un entero válido
                continue
            try:
                cantidad = int(cantidad_str)
            except ValueError:
                continue
            catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})

    print("Catálogo cargado exitosamente.")
    return catalogo

def guardar_catalogo_csv(catalogo):
    """
    Sobrescribe el archivo catalogo.csv (en la carpeta del .py) con la lista de diccionarios actualizada.
    Se llama después de cada operación que modifica el catálogo.
    """
    ruta = os.path.join(os.path.dirname(__file__), NOMBRE_ARCHIVO)
    with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        # Escribir el encabezado
        escritor.writerow(["TITULO", "CANTIDAD"])
        # Escribir cada libro
        for libro in catalogo:
            escritor.writerow([libro.get("TITULO", ""), libro.get("CANTIDAD", 0)])
    print("Catálogo guardado con éxito en", ruta)

# --- Funciones de Validación y Búsqueda (Helpers) ---

def normalizar_titulo(titulo):
    """
    Normaliza un título para comparaciones:
    lo convierte a minúsculas y quita espacios al inicio y al final.
    """
    return titulo.lower().strip()

def buscar_libro(catalogo, titulo_normalizado):
    """
    Busca un libro en el catálogo usando su título normalizado.
    Devuelve el índice (posición) si lo encuentra, o -1 si no.
    """
    for i in range(len(catalogo)):
        if normalizar_titulo(catalogo[i]["TITULO"]) == titulo_normalizado:
            return i # Devuelve el índice
    return -1 # No encontrado

def validar_cantidad(mensaje="Ingrese la cantidad: "):
    """
    Pide al usuario una cantidad hasta que ingrese un entero >= 0.
    """
    while True:
        cantidad_str = input(mensaje)
        if cantidad_str.isdigit() and int(cantidad_str) >= 0:
            return int(cantidad_str)
        else:
            print("Error: Debe ingresar un número entero positivo o cero.")

# --- Funciones del Menú ---

def opcion_1_ingresar_titulos(catalogo):
    """
    Permite al usuario cargar varios libros de una vez.
    Valida títulos no vacíos y no duplicados.
    """
    print("\n--- 1. Ingresar títulos (múltiples) ---")
    cantidad_a_cargar = validar_cantidad("¿Cuántos libros desea cargar?: ")
    
    agregados_count = 0
    for i in range(cantidad_a_cargar):
        print(f"\n--- Libro {i+1} de {cantidad_a_cargar} ---")
        
        # Validar Título (No vacío y No duplicado)
        while True:
            titulo_ingresado = input("Ingrese el TITULO: ")
            if not titulo_ingresado.strip():
                print("Error: El título no puede estar vacío.")
                continue
            
            titulo_norm = normalizar_titulo(titulo_ingresado)
            if buscar_libro(catalogo, titulo_norm) != -1:
                print("Error: El título ya existe en el catálogo.")
            else:
                break # Título válido
        
        # Validar Cantidad
        cantidad_ingresada = validar_cantidad("Ingrese la CANTIDAD (>= 0): ")
        
        # Agregar al catálogo
        catalogo.append({"TITULO": titulo_ingresado.strip(), "CANTIDAD": cantidad_ingresada})
        agregados_count += 1
        
    if agregados_count > 0:
        print(f"\nSe agregaron {agregados_count} libros nuevos.")
        guardar_catalogo_csv(catalogo) # Guardar al finalizar la carga
    else:
        print("No se agregaron libros.")

def opcion_2_ingresar_ejemplares(catalogo):
    """
    Suma una cantidad de ejemplares a un título existente.
    """
    print("\n--- 2. Ingresar ejemplares ---")
    titulo_ingresado = input("Ingrese el TITULO del libro: ")
    titulo_norm = normalizar_titulo(titulo_ingresado)
    
    indice = buscar_libro(catalogo, titulo_norm)
    
    if indice != -1: # Si se encontró el libro
        cantidad_a_sumar = validar_cantidad("Ingrese la cantidad de ejemplares a AÑADIR: ")
        catalogo[indice]["CANTIDAD"] += cantidad_a_sumar
        print(f"Stock actualizado. Nueva cantidad para '{catalogo[indice]['TITULO']}': {catalogo[indice]['CANTIDAD']}")
        guardar_catalogo_csv(catalogo) # Guardar cambios
    else:
        print("Error: Título no encontrado.")

def opcion_3_mostrar_catalogo(catalogo):
    """
    Muestra todos los libros del catálogo de forma ordenada.
    """
    print("\n--- 3. Catálogo Completo ---")
    if not catalogo:
        print("El catálogo está vacío.")
    else:
        print(f"{'TITULO':<30} | {'CANTIDAD':>10}")
        print("-" * 44)
        for libro in catalogo:
            print(f"{libro['TITULO']:<30} | {libro['CANTIDAD']:>10}")

def opcion_4_consultar_disponibilidad(catalogo):
    """
    Busca un título y muestra su cantidad disponible.
    """
    print("\n--- 4. Consultar Disponibilidad ---")
    titulo_ingresado = input("Ingrese el TITULO a consultar: ")
    titulo_norm = normalizar_titulo(titulo_ingresado)
    
    indice = buscar_libro(catalogo, titulo_norm)
    
    if indice != -1:
        libro = catalogo[indice]
        print(f"Hay {libro['CANTIDAD']} ejemplares disponibles de '{libro['TITULO']}'.")
    else:
        print("Error: Título no encontrado.")

def opcion_5_listar_agotados(catalogo):
    """
    Muestra una lista de todos los libros con CANTIDAD == 0.
    """
    print("\n--- 5. Libros Agotados (Stock 0) ---")
    encontrados = False
    for libro in catalogo:
        if libro["CANTIDAD"] == 0:
            print(f"- {libro['TITULO']}")
            encontrados = True
            
    if not encontrados:
        print("No hay libros agotados en el catálogo.")

def opcion_6_agregar_titulo(catalogo):
    """
    Da de alta un (1) nuevo libro en el catálogo.
    """
    print("\n--- 6. Agregar un nuevo título ---")
    
    # Validar Título (No vacío y No duplicado)
    while True:
        titulo_ingresado = input("Ingrese el TITULO: ")
        if not titulo_ingresado.strip():
            print("Error: El título no puede estar vacío.")
            continue
        
        titulo_norm = normalizar_titulo(titulo_ingresado)
        if buscar_libro(catalogo, titulo_norm) != -1:
            print("Error: El título ya existe en el catálogo.")
        else:
            break # Título válido
    
    # Validar Cantidad
    cantidad_ingresada = validar_cantidad("Ingrese la CANTIDAD inicial (>= 0): ")
    
    # Agregar al catálogo
    catalogo.append({"TITULO": titulo_ingresado.strip(), "CANTIDAD": cantidad_ingresada})
    print(f"Libro '{titulo_ingresado.strip()}' agregado con éxito.")
    guardar_catalogo_csv(catalogo) # Guardar cambios

def opcion_7_actualizar_ejemplares(catalogo):
    """
    Permite realizar un préstamo (restar 1) o una devolución (sumar 1).
    """
    print("\n--- 7. Actualizar Ejemplares (Préstamo/Devolución) ---")
    titulo_ingresado = input("Ingrese el TITULO del libro: ")
    titulo_norm = normalizar_titulo(titulo_ingresado)
    
    indice = buscar_libro(catalogo, titulo_norm)
    
    if indice != -1:
        libro = catalogo[indice]
        print(f"Libro seleccionado: '{libro['TITULO']}' (Stock actual: {libro['CANTIDAD']})")
        
        operacion = input("¿Desea realizar un (P)réstamo o (D)evolución?: ").lower().strip()
        
        if operacion == 'p':
            if libro["CANTIDAD"] > 0:
                libro["CANTIDAD"] -= 1
                print(f"Préstamo realizado. Nuevo stock: {libro['CANTIDAD']}")
                guardar_catalogo_csv(catalogo) # Guardar cambios
            else:
                print("Operación fallida: No hay ejemplares disponibles para prestar.")
        
        elif operacion == 'd':
            libro["CANTIDAD"] += 1
            print(f"Devolución realizada. Nuevo stock: {libro['CANTIDAD']}")
            guardar_catalogo_csv(catalogo) # Guardar cambios
        
        else:
            print("Operación no válida. Debe ser 'P' o 'D'.")
            
    else:
        print("Error: Título no encontrado.")

# --- Programa Principal (Menú) ---

def main():
    # Cargar el catálogo desde el CSV al iniciar
    catalogo_principal = cargar_catalogo_csv()
    
    # Bucle 'while' para el menú interactivo
    while True:
        print("\n--- Menú Principal - Gestión de Biblioteca ---")
        print("1. Ingresar títulos (múltiples)")
        print("2. Ingresar ejemplares (sumar stock)")
        print("3. Mostrar catálogo completo")
        print("4. Consultar disponibilidad de un título")
        print("5. Listar libros agotados")
        print("6. Agregar un nuevo título (individual)")
        print("7. Actualizar ejemplares (Préstamo/Devolución)")
        print("8. Salir")
        
        opcion = input("Por favor, seleccione una opción: ")
        
        if opcion == '1':
            opcion_1_ingresar_titulos(catalogo_principal)
        
        elif opcion == '2':
            opcion_2_ingresar_ejemplares(catalogo_principal)
        
        elif opcion == '3':
            opcion_3_mostrar_catalogo(catalogo_principal)
            
        elif opcion == '4':
            opcion_4_consultar_disponibilidad(catalogo_principal)
            
        elif opcion == '5':
            opcion_5_listar_agotados(catalogo_principal)
            
        elif opcion == '6':
            opcion_6_agregar_titulo(catalogo_principal)
            
        elif opcion == '7':
            opcion_7_actualizar_ejemplares(catalogo_principal)
            
        elif opcion == '8':
            print("\nGracias por utilizar el sistema. ¡Hasta luego!")
            break # Termina el bucle while
            
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

# --- Ejecución del programa ---
main()
