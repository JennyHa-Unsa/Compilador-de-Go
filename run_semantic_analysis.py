# run_semantic_analysis.py

import os
from parser import parse  # Importamos el parser desde parser.py
from semantic_analyzer import SemanticAnalyzer  # Importamos el SemanticAnalyzer desde semantic_analyzer.py

def cargar_y_parsear_tests(ruta_carpeta='tests'):
    """ Función para cargar los archivos de prueba desde la carpeta y procesarlos """
    if not os.path.exists(ruta_carpeta):
        print(f"La carpeta '{ruta_carpeta}' no existe.")
        return
    
    archivos = [f for f in os.listdir(ruta_carpeta) if os.path.isfile(os.path.join(ruta_carpeta, f))]
    
    if not archivos:
        print(f"No se encontraron archivos en la carpeta '{ruta_carpeta}'.")
        return
    
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
            print(f"\n* Parseando archivo: {archivo}")
            
            # Paso 1: Parseo del código fuente
            ast = parse(codigo)
            
            # Paso 2: Análisis semántico
            semantic_analyzer = SemanticAnalyzer()
            semantic_analyzer.analyze(ast)

            # Paso 3: Mostrar los errores si los hay
            errors = semantic_analyzer.get_errors()
            if errors:
                print(f"Errores semánticos en {archivo}:")
                for error in errors:
                    print(error)
            else:
                print(f"Análisis semántico exitoso para {archivo}, no se encontraron errores.")
    
if __name__ == "__main__":
    cargar_y_parsear_tests()  # Ejecutar el análisis en todos los archivos de la carpeta 'tests'
