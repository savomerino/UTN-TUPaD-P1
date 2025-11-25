# Trabajo Práctico Integrador: Gestión de Países 🌍

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar una base de datos de países. Permite realizar operaciones CRUD (Crear, Leer, Actualizar), así como filtrar, ordenar y generar estadísticas sobre la población y superficie.

## 📋 Datos del Proyecto
* **Universidad:** Universidad Tecnológica Nacional (UTN)
* **Carrera:** Tecnicatura Universitaria en Programación
* **Materia:** Programación 1
* **Año:** 2025 - 2do Cuatrimestre

## 👥 Integrantes
* [SAVO GABRIEL MERINO]
* [FACUNDO ANDRÉS DE LA ROSA]

## 🚀 Funcionalidades
El sistema cuenta con un menú interactivo con las siguientes opciones:
1.  **Agregar País:** Permite ingresar nuevos registros validando que los datos numéricos sean correctos.
2.  **Actualizar País:** Modificación de población y superficie de un país existente.
3.  **Buscar:** Búsqueda por nombre (coincidencia parcial o exacta).
4.  **Filtros:**
    * Por Continente.
    * Por Rango de Población.
    * Por Rango de Superficie.
5.  **Ordenamiento:** Ascendente o descendente por nombre, población o superficie.
6.  **Estadísticas:** Cálculo de promedios, máximos, mínimos y conteo por continente.
7.  **Persistencia:** Todos los datos se guardan automáticamente en un archivo `paises.csv` al salir.

## 🛠️ Instalación y Ejecución
1.  Asegúrate de tener Python 3.x instalado.
2.  Clona este repositorio o descarga los archivos.
3.  Ejecuta el script principal:
    ```bash
    python tpi1.py
    ```
4.  El archivo `paises.csv` se generará automáticamente si no existe.

## 📄 Estructura del Proyecto
* `tpi_programacion_1.py`: Código fuente principal.
* `paises.csv`: Archivo de base de datos (texto plano).
* `README.md`: Documentación del proyecto.
