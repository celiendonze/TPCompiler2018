COMMAND = 'recInterpreter.py'
FILE = 'inputs/inputALL.txt'

all:
	@clear
	@python ${COMMAND} ${FILE}
	
run:
	@clear
	@python ${COMMAND} ${FILE}

clean:
	@rm -rf ./generated/*;
	@echo "generated directory cleaned" 

install:
	@python --version || echo "Python is not installed on this machine!"
	@pip install -r requirements.txt || python -m pip install -r requirements.txt

lex:
	${eval COMMAND = 'lex5.py'}

if:
	${eval FILE = 'inputs/inputIF.txt'}

fun:
	${eval FILE = 'inputs/inputFUN.txt'}

testall:
	${eval FILE = 'inputs/inputALL.txt'}