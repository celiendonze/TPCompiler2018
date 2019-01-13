import ply.lex as lex

reserved_words = (
	'while',
	'print',
	'if',
	'fun',
	'global',
	'return',
)

tokens = (
	'NUMBER',
	'ADD_OP',
	'MUL_OP',
	'IDENTIFIER',
	'STRING',
	'BOOLEAN',
	'COMP_OP',
) + tuple(map(lambda s:s.upper(),reserved_words))

literals = '();={},'

def t_COMMENT(t):
	r'/[*][^*]*[*]+([^/*][^*]*[*]+)*/|//[^\n]*'
	t.lexer.lineno += len(t.value.split("\n")) - 1

def t_ADD_OP(t):
	r'[+-]'
	return t
	
def t_MUL_OP(t):
	r'[*/]'
	return t

def t_COMP_OP(t):
	r'[<>!][=]?|=='
	return t

def t_STRING(t):
	r'"[^"]*"'
	return t

def t_BOOLEAN(t):
	r'False|True'
	return t

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	try:
		t.value = float(t.value)    
	except ValueError:
		print ("Line %d: Problem while parsing %s!" % (t.lineno,t.value))
		t.value = 0
	return t

def t_IDENTIFIER(t):
	r'[A-Za-z_]\w*'
	if t.value in reserved_words:
		t.type = t.value.upper()
	return t
	
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
	print ("*** Illegal character '%s' at line %i" % (repr(t.value[0]), t.lexer.lineno))
	t.lexer.skip(1)

lex.lex()

if __name__ == "__main__":
	import sys
	try:
		with open(sys.argv[1]) as f:
			prog = f.read()
	except:
		print("passer un fichier en argument")
    
	lex.input(prog)

	while 1:
		tok = lex.token()
		if not tok: break
		print ("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))
