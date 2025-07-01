from parser import parse
from codegen import CodeGenerator

with open("tests/func_simple.go") as f:
    code = f.read()

ast = parse(code)
cg = CodeGenerator()
cg.generate(ast)

print(cg.module)  # Mostrar el LLVM IR generado
print("Código generado con éxito.")