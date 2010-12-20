import sys
class BFCompiler:
    def __init__(self):
        self.current_pointer = 0
        self.bf_string = ""

    def inc(self):
        self.add_string("+")

    def dec(self):
        self.add_string("-")
    
    def move_left(self):
        self.current_pointer -= 1
        self.add_string("<")
    
    def move_right(self):
        self.current_pointer += 1
        self.add_string(">")
    
    def begin_loop(self):
        self.add_string("[")

    def end_loop(self):
        self.add_string("]")

    def input_char(self):
        self.add_string(",")
    
    def output_char(self):
        self.add_string(".")
    
    def add_string(self, string):
        self.bf_string += string

    def debug(self, string):
        #self.bf_string += string + " current_pointer = " + str(self.current_pointer) + "\n"
        pass
    
    def __repr__(self):
        return self.bf_string
    
    def execute(self):
        output_file = sys.argv[1]
        #bf_libraries = sys.argv[2:]
        #main_bf = sys.argv[-1]
        #for library in bf_libraries:
        #    __import__(library)
        #main_bf.main()
        open(output_file, 'w').write(bf_string)
        print(bf_string)