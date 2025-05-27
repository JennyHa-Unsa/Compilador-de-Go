import ply.lex as lex

# Lista de palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'func': 'FUNC',
    'return': 'RETURN',
    'var': 'VAR',
    'int': 'INT',
    'bool': 'BOOL',
    'true': 'TRUE',
    'false': 'FALSE'
}

# Lista de tokens (palabras reservadas + otros)
tokens = [
    'ID',           # identificadores
    'NUMBER',       # números enteros
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',  # operadores aritméticos
    'AND', 'OR', 'NOT',                  # operadores lógicos
    'ASSIGN', 'EQ', 'NEQ',               # asignación y comparación
    'LT', 'GT', 'LE', 'GE',              # comparadores
    'LPAREN', 'RPAREN',                   # paréntesis
    'LBRACE', 'RBRACE',                   # llaves
    'SEMI', 'COMMA'                      # punto y coma, coma
] + list(reserved.values())

# Reglas de expresiones regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_AND     = r'&&'
t_OR      = r'\|\|'
t_NOT     = r'!'
t_ASSIGN  = r'='
t_EQ      = r'=='
t_NEQ     = r'!='
t_LT      = r'<'
t_GT      = r'>'
t_LE      = r'<='
t_GE      = r'>='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'
t_COMMA   = r','

# Ignorar espacios y tabs
t_ignore = ' \t'

# Definición de identificadores (variables, funciones, etc)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Revisar si la palabra está reservada
    t.type = reserved.get(t.value, 'ID')
    return t

# Definición de números enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Manejo de nuevas líneas para contar líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Error léxico: Caracter ilegal '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Prueba rápida
if __name__ == "__main__":
    data = '''
    var x int = 10;
    if x > 5 {
        x = x + 1;
    } else {
        x = 0;
    }
    '''
    lexer.input(data)
    for tok in lexer:
        print(tok)
