import os
from lexer import lexer  # Asumiendo que el lexer está en lexer.py

def guardar_tokens(codigo, nombre_archivo):
    # Crear la carpeta 'tabs_tokens' si no existe
    if not os.path.exists('tabs_tokens'):
        os.makedirs('tabs_tokens')

    # Generar los tokens
    lexer.input(codigo)
    tokens_generados = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_generados.append(f"Token: {tok.type}, Valor: {tok.value}, Línea: {tok.lineno}, Posición: {tok.lexpos}")
        # tokens_generados.append(f"Token: {tok.type}, Valor: {tok.value}")

    # Guardar los tokens en un archivo
    ruta_archivo = os.path.join('tabs_tokens', f"{nombre_archivo}_tokens.txt")
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        for token in tokens_generados:
            f.write(token + '\n')

def cargar_y_guardar_tests(ruta_carpeta='tests'):
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
            print(f"Generando tokens para archivo: {archivo}")
            guardar_tokens(codigo, archivo)

if __name__ == "__main__":
    cargar_y_guardar_tests()
