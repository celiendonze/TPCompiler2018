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

install:
	@pip install -r requirements.txt | python -m pip install -r requirements.txt
	@python --version

lex:
	${eval COMMAND = 'lex5.py'}

1: 
	${eval FILE = 'inputs/input1.txt'}

2: 
	${eval FILE = 'inputs/input2.txt'}

if:
	${eval FILE = 'inputs/inputIF.txt'}

com:
	${eval FILE = 'inputs/inputComment.txt'}

fun:
	${eval FILE = 'inputs/inputFUN.txt'}

testall:
	${eval FILE = 'inputs/inputALL.txt'}