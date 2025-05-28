from .reserved import reserved


tokens = [
    'ID',
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'AND', 'OR', 'NOT',
    'ASSIGN', 'EQ', 'NEQ',
    'LT', 'GT', 'LE', 'GE',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'SEMI', 'COMMA'
] + list(reserved.values())
