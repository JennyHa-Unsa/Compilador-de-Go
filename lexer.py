import ply.lex as lex

from analizador_lexico.reserved import reserved
from analizador_lexico.tokens_list import tokens
from analizador_lexico.token_regex import *

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