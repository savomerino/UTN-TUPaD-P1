#============================#
# PROGRAMACION 1 - PARCIAL 1 #
# Alumno: Savo Merino        #
# Comisión: 08               #
#============================#

# --- Inicialización de Listas Paralelas ---
# Se definen las listas vacías que almacenarán los datos del catálogo.
# titulos[i] corresponde a ejemplares[i]
titulos = []
ejemplares = []

print("¡Bienvenido al Sistema de Gestión de la Biblioteca Escolar!")

# --- Bucle Principal del Menú ---
# El bucle while True mantiene el programa en ejecución hasta que el usuario elija la opción 8.
while True:
    # --- Impresión del Menú de Opciones ---
    print("\n--- Menú Principal ---")
    print("1. Ingresar títulos iniciales")
    print("2. Ingresar cantidad de ejemplares por título")
    print("3. Mostrar catálogo completo")
    print("4. Consultar disponibilidad de un título")
    print("5. Listar libros agotados")
    print("6. Agregar un nuevo título al catálogo")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")

    opcion = input("\nPor favor, seleccione una opción: ")

    # --- Lógica del Menú (equivalente a 'case') ---
    # Se utiliza una estructura if/elif/else para manejar la opción del usuario.

    if opcion == '1':
        print("\n--- 1. Ingresar títulos iniciales ---")
        cantidad_titulos = input("¿Cuántos títulos desea ingresar inicialmente?: ")
        if cantidad_titulos.isdigit() and int(cantidad_titulos) > 0:
            cantidad = int(cantidad_titulos)
            for i in range(cantidad):
                while True:
                    nuevo_titulo = input(f"Ingrese el título del libro {i+1}: ")
                    if nuevo_titulo: # Valida que el título no esté vacío
                        titulos.append(nuevo_titulo)
                        break
                    else:
                        print("El título no puede estar vacío.")
            print("Títulos agregados correctamente.")
        else:
            print("Error: Debe ingresar un número entero y positivo.")

    elif opcion == '2':
        print("\n--- 2. Ingresar cantidad de ejemplares ---")
        if not titulos:
            print("Primero debe ingresar los títulos en la opción 1.")
        else:
            ejemplares = [] # Se limpia la lista para cargar los nuevos valores
            for titulo in titulos:
                while True:
                    cantidad_ejemplares = input(f"Ingrese la cantidad de ejemplares para '{titulo}': ")
                    if cantidad_ejemplares.isdigit() and int(cantidad_ejemplares) >= 0:
                        ejemplares.append(int(cantidad_ejemplares))
                        break
                    else:
                        print("Error: Debe ingresar un número entero no negativo.")
            print("Ejemplares asignados correctamente.")

    elif opcion == '3':
        print("\n--- 3. Catálogo Completo ---")
        if not titulos or not ejemplares or len(titulos) != len(ejemplares):
            print("El catálogo está vacío o no está sincronizado. Por favor, use las opciones 1 y 2.")
        else:
            print("Título del Libro | Ejemplares Disponibles")
            print("------------------------------------------")
            for i in range(len(titulos)):
                print(f"{titulos[i]:<17} | {ejemplares[i]}")

    elif opcion == '4':
        print("\n--- 4. Consultar Disponibilidad ---")
        if not titulos:
            print("El catálogo está vacío.")
        else:
            titulo_buscar = input("Ingrese el título del libro que desea consultar: ").lower()
            encontrado = False
            for i in range(len(titulos)):
                if titulos[i].lower() == titulo_buscar:
                    print(f"Hay {ejemplares[i]} ejemplares disponibles de '{titulos[i]}'.")
                    encontrado = True
                    break
            if not encontrado:
                print("El título no se encuentra en el catálogo.")

    elif opcion == '5':
        print("\n--- 5. Libros Agotados ---")
        if not titulos:
            print("El catálogo está vacío.")
        else:
            agotados_encontrados = False
            print("Los siguientes títulos tienen 0 ejemplares:")
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f"- {titulos[i]}")
                    agotados_encontrados = True
            if not agotados_encontrados:
                print("No hay libros agotados en el catálogo.")

    elif opcion == '6':
        print("\n--- 6. Agregar Nuevo Título ---")
        nuevo_titulo = input("Ingrese el título del nuevo libro: ")
        
        # Validación de título no vacío y no duplicado
        titulo_valido = True
        if not nuevo_titulo:
            print("El título no puede estar vacío.")
            titulo_valido = False
        else:
            for titulo_existente in titulos:
                if titulo_existente.lower() == nuevo_titulo.lower():
                    print("Error: Este título ya existe en el catálogo.")
                    titulo_valido = False
                    break
        
        if titulo_valido:
            while True:
                nuevos_ejemplares_str = input(f"Ingrese la cantidad de ejemplares para '{nuevo_titulo}': ")
                if nuevos_ejemplares_str.isdigit() and int(nuevos_ejemplares_str) >= 0:
                    titulos.append(nuevo_titulo)
                    ejemplares.append(int(nuevos_ejemplares_str))
                    print(f"El libro '{nuevo_titulo}' ha sido agregado con éxito.")
                    break
                else:
                    print("Error: Debe ingresar un número entero no negativo.")

    elif opcion == '7':
        print("\n--- 7. Actualizar Ejemplares (Préstamo/Devolución) ---")
        if not titulos:
            print("El catálogo está vacío.")
        else:
            titulo_modificar = input("Ingrese el título del libro a modificar: ").lower()
            indice_libro = -1
            for i in range(len(titulos)):
                if titulos[i].lower() == titulo_modificar:
                    indice_libro = i
                    break

            if indice_libro != -1:
                operacion = input("¿Desea realizar un (p)réstamo o una (d)evolución?: ").lower()
                if operacion == 'p':
                    if ejemplares[indice_libro] > 0:
                        ejemplares[indice_libro] -= 1
                        print(f"Préstamo realizado. Quedan {ejemplares[indice_libro]} ejemplares de '{titulos[indice_libro]}'.")
                    else:
                        print(f"No hay ejemplares disponibles de '{titulos[indice_libro]}' para prestar.")
                elif operacion == 'd':
                    ejemplares[indice_libro] += 1
                    print(f"Devolución registrada. Ahora hay {ejemplares[indice_libro]} ejemplares de '{titulos[indice_libro]}'.")
                else:
                    print("Operación no válida. Por favor, elija 'p' o 'd'.")
            else:
                print("El título no se encuentra en el catálogo.")

    elif opcion == '8':
        print("\nGracias por utilizar el sistema. ¡Hasta luego!")
        break # Rompe el bucle while y termina el programa

    else:
        print("\nOpción no válida. Por favor, ingrese un número del 1 al 8.")