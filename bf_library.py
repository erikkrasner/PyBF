import bfcore

class BFCompilerWithLibrary(bfcore.BFCompiler):
    def __init__(self):
        self.free_pointer = 0
        self.ADD, self.SUB = 0, 1
        self.LEFT, self.RIGHT = 0,1
        self.current_pointer, self.bf_string = 0, ""
    
    #"Allocates" a block of memory and returns an explicit
    # pointer to that block. In conjunction with move_to,
    # it provides a powerful way to navigate memory in
    # brainfuck. Note that this does not behave like a runtime
    # malloc call - it allocates a *fixed-size* block of memory
    # at compile time. For programs that use a variable amount
    # of memory, allocate a fixed-size block that uses more
    # memory than they will ever need.
    def malloc(self, size):
        temp, self.free_pointer = self.free_pointer, self.free_pointer + size
        return temp
    
    def moven(self, distance, direction):
        self.debug("\nmoven " + str(distance) + " " + str(direction) +"\n" )
        func = self.move_left if direction == self.LEFT else self.move_right
        for i in range(distance):
            func()
            
    #Move to the given pointer. For move_to to work properly,
    # your program must maintain the invariant that pybf knows
    # at compile-time where the program is in memory. Fortunately,
    # because brainfuck is so simple, this is easy to keep track
    # of: make sure that at every end_loop() the pointer is in the
    # same place as the corresponding begin_loop(). The wide range
    # of valid programs that don't maintain this invariant will
    # corrupt move_to.
    def move_to(self, pointer):
        self.debug("\nmove_to " + str(pointer) + "\n")
        current_pointer = self.current_pointer
        direction = self.LEFT if pointer < current_pointer else self.RIGHT
        self.moven(abs(pointer - current_pointer), direction)

    def add(self, integer):
        self.debug("\nadd " + str(integer) + "\n")
        for i in range(integer):
            self.inc()
        
    def sub(self, integer):
        self.debug("\nsub " + str(integer) + "\n")
        for i in range(integer):
            self.dec()

    def add_to(self, pointers):
        self.debug("\nadd_to " + str(pointers) + "\n")
        orig = self.current_pointer
        self.begin_loop()
        self.dec()
        for pointer in pointers:
            self.move_to(pointer)
            self.inc()
        self.move_to(orig)
        self.end_loop()
    
    def sub_from(self, pointers):
        self.debug("\nsub_from " + str(pointers) + "\n") #debug
        orig = self.current_pointer
        self.begin_loop()
        self.dec()
        for pointer in pointers:
            self.move_to(pointer)
            self.dec()
        self.move_to(orig)
        self.end_loop()
    
    def copy_to(self, pointers):
        self.debug( "\ncopy_to " + str(pointers) + "\n") #debug
        orig = self.current_pointer
        scratch = self.malloc(1)
        self.add_to(pointers + [scratch])
        self.move_to(scratch)
        self.add_to([orig])
        self.move_to(orig)

    def neg_copy_to(self, pointers):
        self.debug("\nneg_copy_to " + str(pointers) + "\n")
        orig = self.current_pointer
        scratch = self.malloc(1)
        self.copy_to([scratch])
        self.sub_from(pointers)
        self.move_to(scratch)
        self.add_to([orig])
        self.move_to(orig)

    def clean_copy_to(self, pointers):
        self.debug("\nclean_copy_to " + str(pointers) + "\n")
        orig = self.current_pointer
        for pointer in pointers:
            self.move_to(pointer)
            self.reset()
        self.move_to(orig)
        self.copy_to(pointers)

    def mult_by(self, pointer):
        self.debug("\nmult_by " + str(pointer) + "\n")
        orig = self.current_pointer
        scratch = self.malloc(1)
        self.add_to([scratch])
        self.move_to(pointer)
        self.begin_loop()
        self.dec()
        self.move_to(scratch)
        self.copy_to([orig])
        self.move_to(pointer)
        self.end_loop()
        self.move_to(orig)

    def mult_i(self, integer):
        self.debug("\nmult_i " + str(integer) + "\n")
        orig = self.current_pointer
        scratch = self.malloc(1)
        self.move_to(scratch)
        self.add(integer)
        self.move_to(orig)
        self.mult_by(scratch)
    
    def normalize(self):
        self.debug("\nnormalize " + str(pointer))
        orig = self.current_pointer
        scratch = self.malloc(1)
        self.begin_loop()
        self.reset()
        self.move_to(scratch)
        self.inc()
        self.move_to(orig)
        self.end_loop()
        self.move_to(scratch)
        self.copy_to(orig)
        sekf.move_to(orig)
    
    def div_by(self, pointer):
        orig = self.current_pointer
        
        
    def divmod_by(self, pointer, dest):
        self.debug("\ndivmod_by " + str(pointer) + " " + str(dest) + "\n")
        dividend = self.current_pointer
        divisor = pointer
        quotient = dest
        remainter = dest + 1
        tracker = malloc(1)
        test = malloc(1)
        self.move_to(divisor)
        self.copy_to([tracker])
        #Keep going until dividend is empty
        self.move_to(dividend)
        begin_loop()
        self.dec()
        #Set test to -1 if tracker == 0, 0 otherwise
        self.move_to(tracker)
        self.clean_copy_to([test])
        self.move_to(test)
        self.normalize()
        self.dec()
        #if tracker == 0, increment quotient, copy divisor to tracker
        self.begin_loop()
        self.move_to(quotient)
        self.inc()
        self.move_to(divisor)
        self.copy_to(tracker)
        self.move_to(test)
        self.inc()
        self.end_loop()
        #decrement tracker
        self.move_to(tracker)
        self.dec()
        self.move_to(dividend)
        end_loop()
        #copy mod(currently stored in tracker) to remainter
        self.move_to(tracker)
        self.copy_to([remainder])
        self.move_to(dividend)
    
    
    def divmod_i(self, integer, dest):
        self.debug("\ndivmod_i " + str(integer) + " " + str(dest) + "\n")
        orig = self.current_pointer
        scratch = self.malloc(1)
        self.move_to(scratch)
        self.add(integer)
        self.move_to(orig)
        self.divmod_by(scratch, dest)

    def reset(self):
        self.debug("\nreset\n")
        self.begin_loop()
        self.dec()
        self.end_loop()
    
    def set(self, integer):
        self.debug("\nset " + str(integer) + "\n")
        self.reset()
        self.add(integer)

    def output_current_string(self):
        self.debug("\noutput_current_string\n")
        self.begin_loop()
        self.output_char()
        self.move_right()
        self.end_loop()

    def enter_string(self, string):
        self.debug("\nenter_string " + string + "\n")
        orig = self.current_pointer
        string_ptr = self.malloc(len(string) + 1)
        self.move_to(string_ptr)
        for char in string:
            self.add(ord(char))
            self.move_right()
        self.move_to(orig)
        return string_ptr

    def output_string(self, string):
        self.debug("\noutput_string " + string + "\n")
        for char in string:
            self.set(ord(char))
            self.output_char()
        
if __name__ == "__main__":
    bfc = BFCompilerWithLibrary()
    bfc.output_string("Hello World")
    print bfc
