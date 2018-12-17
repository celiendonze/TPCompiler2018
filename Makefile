COMMAND = 'recInterpreter.py'
FILE = 'inputs/input1.txt'

all:
	@clear
	@python ${COMMAND} ${FILE}
	
run:
	@clear
	@python ${COMMAND} ${FILE}

clean:
	@rm -rf ./generated/*;
	@echo "cleaned" 

lex:
	${eval COMMAND = 'lex5.py'}

1: 
	${eval FILE = 'inputs/input1.txt'}

2: 
	${eval FILE = 'inputs/input2.txt'}

if:
	${eval FILE = 'inputs/inputIF.txt'}

comment:
	${eval FILE = 'inputs/inputComment.txt'}