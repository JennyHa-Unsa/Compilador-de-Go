import ply.yacc as yacc
from lexer import lexer
from analizador_lexico.tokens_list import tokens
import os

# Precedencia de operadores para resolver ambigüedades
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NEQ'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT'),
)

# Regla inicial
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Declaración de variable, con o sin inicialización
def p_statement_var_decl(p):
    '''statement : VAR ID INT SEMI
                 | VAR ID INT ASSIGN expression SEMI'''
    if len(p) == 5:
        p[0] = ('var_decl', p[2], None)
    else:
        p[0] = ('var_decl', p[2], p[5])

# Asignación
def p_statement_assign(p):
    '''statement : ID ASSIGN expression SEMI'''
    p[0] = ('assign', p[1], p[3])

# Expresiones aritméticas y lógicas
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression AND expression
                  | expression OR expression
                  | expression EQ expression
                  | expression NEQ expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_not(p):
    '''expression : NOT expression'''
    p[0] = ('not', p[2])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = ('number', p[1])

def p_expression_id(p):
    '''expression : ID'''
    p[0] = ('id', p[1])

# Sentencia if-else
def p_statement_if(p):
    '''statement : IF expression LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
                 | IF expression LBRACE statement_list RBRACE'''
    if len(p) == 10:
        p[0] = ('if_else', p[2], p[4], p[8])
    else:
        p[0] = ('if', p[2], p[4])

# Ciclo for
def p_statement_for(p):
    '''statement : FOR ID ASSIGN expression SEMI expression SEMI ID ASSIGN expression LBRACE statement_list RBRACE'''
    p[0] = ('for', p[2], p[4], p[6], p[8], p[10], p[12])

# Funciones y return
def p_statement_func(p):
    '''statement : FUNC ID LPAREN RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('func_def', p[2], [], p[6])

def p_statement_return(p):
    '''statement : RETURN expression SEMI'''
    p[0] = ('return', p[2])


# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error sintáctico en token '{p.value}' (tipo {p.type}) en línea {p.lineno}")
    else:
        print("Error sintáctico: fin inesperado de entrada")

# Construcción del parser
parser = yacc.yacc()

# Función para parsear el código fuente
def parse(data):
    return parser.parse(data, lexer=lexer)

if __name__ == "__main__":
    tests_dir = "tests"
    output_dir = "asts"
    os.makedirs(output_dir, exist_ok=True)

    for fname in os.listdir(tests_dir):
        if not fname.endswith(".go"):
            continue
        path = os.path.join(tests_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            src = f.read()
        ast = parse(src)

        out_path = os.path.join(output_dir, fname + ".txt")
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(repr(ast))

        print(f"AST de {fname} guardado en {out_path}")
