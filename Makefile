
all:
	@echo 'Starting run.py'
	@command time -f "%Mkb %Us" python3 src/run.py < test_inputs/run_input
