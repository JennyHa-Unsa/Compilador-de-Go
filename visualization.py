from rich import print
from rich.tree import Tree
import os

# Reúso de tu función de construcción de Tree
def build_rich_tree(ast, tree=None):
    label = ast[0] if isinstance(ast, tuple) else str(ast)
    if tree is None:
        tree = Tree(label)
    else:
        tree = tree.add(label)
    if isinstance(ast, tuple):
        for child in ast[1:]:
            if isinstance(child, list):
                for item in child:
                    build_rich_tree(item, tree)
            else:
                build_rich_tree(child, tree)
    return tree

def visualize_from_file(ast_file):
    # Reconstruir la tupla AST con eval
    with open(ast_file, "r", encoding="utf-8") as f:
        ast = eval(f.read())
    tree = build_rich_tree(ast)
    print(tree)

if __name__ == "__main__":
    # Por ejemplo, visualizar todos los ASTs guardados
    for fname in os.listdir("asts"):
        if not fname.endswith(".txt"):
            continue
        print(f"\n=== {fname} ===")
        visualize_from_file(os.path.join("asts", fname))
