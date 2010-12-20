import bf_library

test = bf_library.BFCompilerWithLibrary()
input = test.malloc(1)
divmod = test.malloc(2)
test.move_to(input)
test.input_char()
test.divmod_i(3, divmod)
test.move_to(divmod)
test.output_char()
test.move_to(divmod + 1)
test.output_char()
print test