# CSC410-P3
First check-in

Using pyminic and PyCParser

The raw input files are in the ./tests/c_files/inputs folder To run the tool, type (in the pyminic directory):

python tool.py [input_name] (ex: python tool.py p3_input2)

The tool will first run the wrapper.py, which wrap each raw input files in a dummy C function definition, and write in a new input file. (p3_input1 -> new_p3_input1.c)

Then it will start parsing the new input file and print the requested output on the terminal.
