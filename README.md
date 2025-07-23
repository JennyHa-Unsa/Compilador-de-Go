# Compilador de subconjunto de Go

Construcción de un compilador para un subconjunto de Go.

## Requisitos

- Python 3.7 o superior
- Qemu - emulador de ARMv7 para Rasberry Pi 3 (Para pruebas)

## Instalación

- Clona el repositorio:

```
git clone https://github.com/JennyHa-Unsa/Compilador-de-Go.git
cd Compilador-de-Go
```

- Crea y activa un entorno virtual:
```
python3 -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
```

-Instala las dependencias:
```
pip install -r requirements.txt
```
- 🧪 Uso
Para compilar un archivo Go, ejecuta:
```
python main.py 
```
Esto generará un archivo en el directorio output/ con el código ensamblador correspondiente.

- Copiar y ejecutar el código ensamblador en Qemu

## Estructura del proyecto
```
Compilador-de-Go/
├── __pycache__/                 # Archivos compilados de Python
├── output/                      # Archivos generados
│   ├── ejemplo_bool_armv7
│   ├── ejemplo_bool
│   ├── ejemplo_completo_armv7
│   ├── ejemplo_completo
│   ├── ejemplo_saludo_armv7
│   └── ejemplo_saludo
├── tests/                       # Casos de prueba
│   ├── ejemplo_bool.go
│   ├── ejemplo_completo.go
│   ├── ejemplo_saludo.go
│   └── error_semantico.go
├── venv/                        # Entorno virtual de Python
├── .gitignore                   # Archivos y directorios ignorados por Git
├── codegen.py                   # Generador de código ensamblador
├── comands.md                   # Comandos y notas
├── main.py                      # Punto de entrada del compilador
├── mg_ast.py                    # Manejo de AST (Árbol de Sintaxis Abstracta)
├── mg_lexer.py                  # Analizador léxico
├── mg_parser.py                 # Analizador sintáctico
├── preprocessor.py              # Preprocesador de código Go
├── README.md                    # Este archivo
└── semant.py                    # Verificación semántica
