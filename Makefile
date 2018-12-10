all:
	@python recInterpreter.py input2.txt
clean:
	@rm -rf ./generated/*;
	@echo "cleaned" 
1: 
	@python recInterpreter.py input1.txt