import sys

translation = {'+':'a.inc()\n',
               '-':'a.dec()\n',
               '<':'a.move_left()\n',
               '>':'a.move_right()\n',
               '[':'a.begin_loop()\n',
               ']':'a.end_loop()\n',
               ',':'a.input_char()\n',
               '.':'a.output_char()\n'}
input_file = open(sys.argv[1], 'r')
bf = input_file.read()
input_file.close()
output_file = open(sys.argv[2],'w')
output_file.write("from bfcore import *\n")
output_file.write("a=BFCompiler()\n")
for char in bf:
    if char in translation:
        output_file.write(translation[char])
output_file.write("print a\n")
output_file.close()