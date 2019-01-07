import AST
from AST import addToClass
from functools import reduce

# operateurs mathematiques
operations = {
    '+': lambda x, y : x + y,
    '-': lambda x, y : x - y,
    '*': lambda x, y : x * y,
    '/': lambda x, y : x / y,
}

# operateurs de comparaison
compOperations = {
    '<': lambda x, y : x < y,
    '>': lambda x, y : x > y,
    '<=': lambda x, y : x <= y,
    '>=': lambda x, y : x >= y,
    '==': lambda x, y : x == y,
}

vars = {}
globalVars = {}

@addToClass(AST.ProgramNode)
def execute(self):
    for c in self.children:
        c.execute()

@addToClass(AST.TokenNode)
def execute(self):
    if isinstance(self.tok, str):
        try:
            # we check if it exists in the local variables, if not we also check the globals and otherwise it's undefined
            try:
                return vars[self.tok]
            except:
                return globalVars[self.tok]
        except KeyError:
            print("*** Error : variable %s undefined!" % self.tok)
    return self.tok

@addToClass(AST.OpNode)
def execute(self):
    args = [c.execute() for c in self.children]
    if len(args) == 1:
        args.insert(0, 0)
    try:
        return reduce(operations[self.op], args)
    except:
        print(f"*** Error : invalid operation between operands {args[0]} and {args[1]}")

@addToClass(AST.CompOpNode)
def execute(self):
    args = [c.execute() for c in self.children]
    if len(args) == 2:
        try:
            return compOperations[self.op](float(args[0]), float(args[1]))
        except:
            print(f"*** Error : Invalid comparison between operands {args[0]} and {args[1]}")
    else:
        return False

@addToClass(AST.StringNode)
def execute(self):
    return str(self)

@addToClass(AST.BooleanNode)
def execute(self):
    return self.val

@addToClass(AST.AssignNode)
def execute(self):
    if(not self.isGlobal):
        vars[self.children[0].tok] = self.children[1].execute()
    else:
        globalVars[self.children[0].tok] = self.children[1].execute()

@addToClass(AST.PrintNode)
def execute(self):
    print(self.children[0].execute())

@addToClass(AST.WhileNode)
def execute(self):
    while self.children[0].execute():
        self.children[1].execute()

@addToClass(AST.IfNode)
def execute(self):
    if self.children[0].execute():
        self.children[1].execute()

if __name__ == '__main__':
    from parser5 import parse
    import sys
    
    try:
        with open(sys.argv[1]) as f:
            prog = f.read()
    except:
        print("passer un fichier en argument")
    
    ast = parse(prog)

    ast.execute()
