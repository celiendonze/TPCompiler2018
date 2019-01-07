import ply.yacc as yacc

from lex5 import tokens
import AST

# def p_newprogram_recursive(p):
#     '''newprogram : func newprogram
#     | func
#     '''
#     try:
#         p[0] = p[1] + p[2]
#     except:
#         p[0] = p[1]




# def p_returninstr(p):
#     '''returninstr : RETURN expression'''



def p_programme_recursive(p):
    ''' programme : statement ';' programme
    | structure programme
    | statement ';' 
    | structure'''
    try:
        p[0] = AST.ProgramNode([p[1]]+p[3].children)
    except:
        try:
            p[0] = AST.ProgramNode([p[1]]+p[2].children)
        except:
            p[0] = AST.ProgramNode([p[1]])
      
def p_statement(p):
    ''' statement : assignation
    | funcCall'''
    p[0] = p[1] 

def p_structure(p):
    '''structure : funcDec '''
    p[0] = p[1]

def p_funcDec(p):
    '''funcDec : FUN IDENTIFIER '(' ')' '{' programme '}'
    '''
    p[0] = AST.FunNode(p[2], p[6])
    #print(p[0].body)
    
def p_funcCall(p):
    '''funcCall : IDENTIFIER '(' ')' '''
    p[0] = AST.FunCallNode(p[1])

def p_statement_print(p):
    ''' statement : PRINT expression '''
    p[0] = AST.PrintNode(p[2])

def p_structure_while(p):
    ''' structure : WHILE expression '{' programme '}' '''
    p[0] = AST.WhileNode([p[2],p[4]])

def p_structure_if(p):
    ''' structure : IF expression '{' programme '}' '''
    p[0] = AST.IfNode([p[2], p[4]])

def p_expression_add_strings(p):
    '''expression : STRING '+' STRING'''
    string = p[1] + p[3]
    p[0] = AST.StringNode(string)

def p_expression_op(p):
    '''expression : expression ADD_OP expression
    | expression MUL_OP expression'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_expression_comp(p):
    '''expression : expression COMP_OP expression'''
    p[0] = AST.CompOpNode(p[2], [p[1], p[3]])

def p_expression_num_or_var(p):
    '''expression : NUMBER
    | IDENTIFIER '''
    p[0] = AST.TokenNode(p[1])

def p_expression_boolean(p):
    '''expression : BOOLEAN'''
    p[0] = AST.BooleanNode(p[1])

def p_expression_string(p):
    ''' expression : STRING '''
    p[0] = AST.StringNode(p[1].replace("\"",""))

def p_expression_paren(p):
    '''expression : '(' expression ')' '''
    p[0] = p[2]

def p_minus(p):
    ''' expression : ADD_OP expression %prec UMINUS'''
    p[0] = AST.OpNode(p[1], [p[2]])
    	
def p_assignation(p):
    ''' assignation : IDENTIFIER '=' expression
    | GLOBAL IDENTIFIER '=' expression  '''
    # if it's the second part of the rule it means we have 4 lexemes and it's a global var and we set True to the isGlobal parameter
    try:
        p[0] = AST.AssignNode([AST.TokenNode(p[2]),p[4], True])
    except:
        p[0] = AST.AssignNode([AST.TokenNode(p[1]),p[3]])

def p_error(p):
    if p:
        print ("Syntax error in line %d" % p.lineno)
        yacc.errok()
    else:
        print ("Sytax error: unexpected end of file!")


precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('left', 'COMP_OP'),
    ('right', 'UMINUS'),  
)

def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys
    	
    try:
        with open(sys.argv[1]) as f:
            prog = f.read()
    except:
        print("passer un fichier en argument")
    
    result = yacc.parse(prog)
    if result:
        print (result)
            
        import os
        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
        graph.write_pdf(name) 
        print ("wrote ast to", name)
    else:
        print ("Parsing returned no result!")