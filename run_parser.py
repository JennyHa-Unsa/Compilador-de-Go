import os
from parser import parse  # Importamos la función parse desde parser.py

def cargar_y_parsear_tests(ruta_carpeta='tests'):
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
            print(f"\n *Parseando archivo: {archivo}")
            resultado = parse(codigo)
            print(f"Resultado para {archivo}: {resultado}")

if __name__ == "__main__":
    cargar_y_parsear_tests()
