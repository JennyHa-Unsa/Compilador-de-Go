import ply.yacc as yacc
from lexer import lexer
from analizador_lexico.tokens_list import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: fin inesperado")

parser = yacc.yacc()

def parse(data):
    return parser.parse(data, lexer=lexer)

if __name__ == "__main__":
    codigo = "3 + 4 * 10"
    resultado = parse(codigo)
    print(resultado)
