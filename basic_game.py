import bf_library
class GuessingGame(bf_library.BFCompilerWithLibrary):
    def __init__(self):
        self.free_pointer = 0
        self.ADD, self.SUB = 0, 1
        self.LEFT, self.RIGHT = 0,1
        self.current_pointer, self.bf_string = 0, ""
        
    def make_game(self):
        #organize memory
        write_buffer = self.malloc(1)
        seed = self.malloc(1)
        guess = self.malloc(1)
        hash = self.malloc(2)
        win_loss_message = self.enter_string(" Correct! You win! Too bad! You fail!")
        loss_message = win_loss_message + 18
        #strategically place a couple of zeros for navigation
        self.move_to(win_loss_message)
        self.reset()
        self.move_to(loss_message)
        self.reset()
        
        #Write introductory message
        self.move_to(write_buffer)
        self.output_string("Welcome to Guess A Number!\n")
        self.output_string("Enter a one-character seed:\n")  
        #take seed character  
        self.move_to(seed)
        self.input_char()
    
        #prompt user to pick a message
        self.move_to(write_buffer)
        self.output_string("\nPick a number between 1 and 7:\n")
        self.move_to(guess)
        self.input_char()
        self.sub(49)
    
        #Generate a "pseudorandom" number from the seed
        self.move_to(seed)
        self.mult_i(3)
        self.divmod_i(7, hash)
        #Check if the guess was correct
        self.move_to(hash + 1)
        self.neg_copy_to([guess])
        self.move_to(guess)
        self.clean_copy_to([win_loss_message])
    
        #if guess is not correct, skip win message
        self.move_to(win_loss_message)
        self.begin_loop()
        self.begin_loop()
        self.move_to(loss_message)
        self.end_loop()
        self.end_loop()
    
        self.move_right()
        self.output_current_string()

if __name__ == '__main__':
    gg = GuessingGame()
    gg.make_game()
    print gg