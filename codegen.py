from llvmlite import ir

class CodeGenerator:
    def __init__(self):
        self.module = ir.Module(name="main")
        self.builder = None
        self.func_symtab = {}

    def generate(self, node):
        nodetype = node[0]

        if nodetype == 'program':
            for stmt in node[1]:
                self.generate(stmt)

        elif nodetype == 'var_decl':
            name = node[1]
            value = node[2]
            typ = ir.IntType(32)
            ptr = self.builder.alloca(typ, name=name)
            self.func_symtab[name] = ptr
            if value:
                val = self.generate(value)
                self.builder.store(val, ptr)

        elif nodetype == 'assign':
            name = node[1]
            val = self.generate(node[2])
            self.builder.store(val, self.func_symtab[name])

        elif nodetype == 'number':
            return ir.Constant(ir.IntType(32), node[1])

        elif nodetype == 'id':
            return self.builder.load(self.func_symtab[node[1]])

        elif nodetype == 'binop':
            op, left, right = node[1], node[2], node[3]
            l = self.generate(left)
            r = self.generate(right)
            if op == '+':
                return self.builder.add(l, r)
            elif op == '-':
                return self.builder.sub(l, r)
            elif op == '*':
                return self.builder.mul(l, r)
            elif op == '/':
                return self.builder.sdiv(l, r)

        elif nodetype == 'func_def':
            fname = node[1]
            body = node[3]
            func_type = ir.FunctionType(ir.IntType(32), [])
            func = ir.Function(self.module, func_type, name=fname)
            block = func.append_basic_block(name="entry")
            self.builder = ir.IRBuilder(block)
            self.func_symtab = {}
            for stmt in body:
                self.generate(stmt)

        elif nodetype == 'return':
            val = self.generate(node[1])
            self.builder.ret(val)

        else:
            raise NotImplementedError(f"Nodo no implementado: {nodetype}")
