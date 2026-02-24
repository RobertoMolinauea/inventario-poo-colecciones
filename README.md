# Sistema de Gestión de Inventario (POO + Colecciones + Archivos)

## Descripción
Programa de consola para gestionar productos con ID, nombre, cantidad y precio.
Permite agregar, eliminar, actualizar, buscar por nombre y mostrar el inventario.

## Cómo ejecutar
1. Abre la carpeta del proyecto
2. Ejecuta:
   python main.py

## Colecciones usadas
- Diccionario (dict): guarda productos por ID para acceso rápido (id -> Producto).
- Lista (list): se usa para acumular resultados al buscar por nombre.
- Conjunto (set): guarda IDs únicos para validar rápido si un ID ya existe.
- Tupla (tuple): la búsqueda por nombre devuelve una tupla (resultado inmutable).

## Archivos
- Se guarda y carga en `inventario.csv`.
- Al iniciar el programa, se carga el archivo y se reconstruye el inventario.

## Pruebas realizadas
- Agregar producto nuevo
- Evitar ID repetido
- Buscar por nombre
- Actualizar cantidad y precio
- Eliminar por ID
- Cerrar y abrir el programa para confirmar persistencia
