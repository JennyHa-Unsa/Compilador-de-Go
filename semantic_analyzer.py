# semantic_analyzer.py

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}
        self.errors = []

    def add_variable(self, name, var_type):
        """ Agrega una variable a la tabla de símbolos """
        if name in self.symbol_table:
            self.errors.append(f"Error: La variable '{name}' ya está declarada.")
        else:
            self.symbol_table[name] = var_type

    def check_variable(self, name):
        """ Verifica si una variable está declarada """
        if name not in self.symbol_table:
            self.errors.append(f"Error: La variable '{name}' no está declarada.")

    def check_types(self, left_type, right_type, op):
        """ Verifica la compatibilidad de los tipos de datos en operaciones """
        if left_type != right_type:
            self.errors.append(f"Error: Tipos incompatibles en operación {op}. '{left_type}' y '{right_type}' no son compatibles.")
    
    def analyze_expression(self, node):
        """ Analiza una expresión """
        nodetype = node[0]
        if nodetype == 'number':
            return 'int'
        elif nodetype == 'id':
            self.check_variable(node[1])
            return self.symbol_table[node[1]]
        elif nodetype == 'binop':
            left_type = self.analyze_expression(node[2])
            right_type = self.analyze_expression(node[3])
            self.check_types(left_type, right_type, node[1])
            return left_type  # Supone que la operación no cambia el tipo
        elif nodetype == 'not':
            expr_type = self.analyze_expression(node[1])
            if expr_type != 'bool':
                self.errors.append(f"Error: El operador 'not' requiere un tipo 'bool'.")
            return 'bool'
        else:
            raise NotImplementedError(f"Tipo de nodo no implementado para análisis semántico: {nodetype}")

    def analyze(self, node):
        """ Realiza el análisis semántico en un nodo """
        nodetype = node[0]

        if nodetype == 'program':
            for stmt in node[1]:
                self.analyze(stmt)

        elif nodetype == 'var_decl':
            self.add_variable(node[1], 'int' if node[2] is None else self.analyze_expression(node[2]))

        elif nodetype == 'assign':
            var_type = self.symbol_table.get(node[1])
            if var_type is None:
                self.errors.append(f"Error: La variable '{node[1]}' no está declarada.")
            else:
                expr_type = self.analyze_expression(node[2])
                self.check_types(var_type, expr_type, '=')

        elif nodetype == 'func_def':
            # Aquí podrías verificar las firmas de las funciones
            pass

        elif nodetype == 'return':
            expr_type = self.analyze_expression(node[1])
            return expr_type

        return None

    def get_errors(self):
        return self.errors
