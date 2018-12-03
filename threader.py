import AST
from AST import addToClass

@addToClass(AST.Node)
def thread(self, lastNode):
    for c in self.children:
        lastNode = c.thread(lastNode)
    lastNode.addNext(self)
    return self

@addToClass(AST.WhileNode)
def thread(self, lastNode):
    self.children[0].thread(lastNode).addNext(self)
    self.children[1].thread(self).addNext(lastNode.next[0])
    return self

def thread(tree):
    entry = AST.EntryNode()
    tree.thread(entry)
    return entry

if __name__ == "__main__":
    from parser5 import parse
    import sys, os
    try:
        with open(sys.argv[1]) as f:
            prog = f.read()
    except:
        print("passer un fichier en argument")
    
    ast = parse(prog)
    entry = thread(ast)

    graph = ast.makegraphicaltree()
    entry.threadTree(graph)
    
    name = os.path.splitext(sys.argv[1])[0]+'-ast-threaded.pdf'
    graph.write_pdf(name) 
    print ("wrote threaded ast to", name)    
