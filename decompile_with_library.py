import sys

input_file = open(sys.argv[1], 'r')
bf = input_file.read()
input_file.close()
output_file = open(sys.argv[2],'w')
output_file.write("from bfcore import *\n")
output_file.write("a=BFCompiler()\n")
while(bf != ""):
    output_file.write("a.")
    if bf[0] == "+":
        output_file.write("inc()")
    elif bf[0] == "-":
        output_file.write("dec()")
    elif bf[0] == "<":
        output_file.write("move_left()")
    elif bf[0] == "<":
        output_file.write("move_right()")
    elif bf[0] == ",":
        output_file.write("input_char()")
    elif bf[0] == ".":
        output_file.write("output_char()")
    output_file.write("\n")
output_file.write("print a\n")
output_file.close()