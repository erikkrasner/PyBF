import bf_library

test = bf_library.BFCompilerWithLibrary()
test.move_to(test.malloc(1))
test.input_char()
test.mult_i(3)
test.output_char()
print test