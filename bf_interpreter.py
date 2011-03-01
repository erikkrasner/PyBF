class BFInterpreter:
    class BFException(Exception):
        pass
    def __init__(self, bf_string):
        self.loopStack = []
        self.tape = {}
        self.programCounter = 0
        self.currentPointer = 0
        self.semanticActions = {'+':self.inc,'-':self.dec,'<':self.move_left,'>':self.move_right,'[':self.begin_loop,']':self.end_loop,',':self.input_char,'.':self.output_char,'!':self.end}
        self.run(bf_string)
    def run(self, bf_string):
        while self.programCounter < len(bf_string):
            bf_char = bf_string[self.programCounter]
            if bf_char in self.semanticActions:
                self.semanticActions[bf_char]()
            else:
                raise BFException("Illegal BF character.")
            self.incrementProgramCounter()
        self.end()
    def incrementProgramCounter(self):
        self.programCounter += 1
    def getCurrentValue(self):
        if self.currentPointer not in self.tape:
            self.tape[self.currentPointer] = 0
        return self.tape[self.currentPointer]
    def setCurrentValue(self, amount):
        self.tape[self.currentPointer] = amount
    def inc(self):
        self.incrementCurrentValueBy(1)
    def dec(self):
        self.incrementCurrentValueBy(-1)
    def incrementCurrentValueBy(self,amount):
        self.setCurrentValue((self.getCurrentValue() + amount) % 256)
    def move_left(self):
        self.incrementCurrentPointerBy(-1)
    def move_right(self):
        self.incrementCurrentPointerBy(1)
    def incrementCurrentPointerBy(self,amount):
        self.currentPointer += amount
    def begin_loop(self):
        self.loopStack.append(self.programCounter)
    def end_loop(self):
        if self.loopStack:
            if self.getCurrentValue():
                self.programCounter = self.loopStack[-1]
            else:
                self.loopStack.pop()
        else:
            raise BFException("Loop close without corresponding loop open")
    def input_char(self):
        self.setCurrentValue(ord(raw_input()[0]))
    def output_char(self):
        print chr(self.getCurrentValue()),
    def end(self):
        sys.exit(0)
