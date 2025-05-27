import lexer  # Asumiendo que el lexer está en lexer.py
import os

def probar_lexer(codigo, nombre_archivo):
    print(f"\n--- Probando archivo: {nombre_archivo} ---\n")
    print(f"TOKEN \t VALOR \t\t LÍNEA \t POSICIÓN \t")
    lexer.lexer.input(codigo)
    while True:
        tok = lexer.lexer.token()
        if not tok:
            break
        print(f"{tok.type} \t {tok.value} \t\t {tok.lineno} \t {tok.lexpos} \t")

def cargar_y_probar_tests(ruta_carpeta='tests'):
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
            probar_lexer(codigo, archivo)

if __name__ == "__main__":
    cargar_y_probar_tests()
