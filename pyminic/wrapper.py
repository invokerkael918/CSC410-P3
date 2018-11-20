import os

path = './tests/c_files/inputs'

for file in os.listdir(path):
	if not (file == 'new_p3_input1.c' or file == 'new_p3_input2.c' or file == 'new_p3_input3.c'):

		new_filename = 'new_' + file  + '.c' 
		new_inpt = open(os.path.join(path, new_filename), 'w')
		inpt = open(os.path.join(path, file), 'r')

		new_inpt.write('int dummy (){\n')

		for l in inpt:
			new_inpt.write('	')
	 		new_inpt.write(l)
	 	new_inpt.write('\n}')

	 	new_inpt.close()
	 	inpt.close()