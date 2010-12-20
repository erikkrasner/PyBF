import sys
import re

input_file = open(sys.argv[1], 'r')
bf = input_file.read()
input_file.close()
output_file = open(sys.argv[2],'w')
output_file.write("from bfcore import *\n")
output_file.write("a=BFCompiler()\n")
while(bf != ""):
    output_file.write("a.")
    first_char = bf[0]
    if first_char in "+-<>":
        match = re.match('\\' + bf[0] + '+', bf)
        length = len(match)
        output_file.write(
                "add" if first_char == "+" else 
                "sub" if first_char == "-" else
                "move_left" if first_char == "<" else
                "move_right"
                + "(" + length + ")")
    elif bf[0] == "[":
        output_file.write("begin_loop()")
        legnth = 1
    elif bf[0] == "]":
        output_file.write("end_loop()")
        length = 1
    elif bf[0] == ",":
        output_file.write("input_char()")
        length = 1
    elif bf[0] == ".":
        output_file.write("output_char()")
        length = 1
    bf = bf[length:]
    output_file.write("\n")
output_file.write("print a\n")
output_file.close()