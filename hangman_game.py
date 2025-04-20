import csv

class HangmanGame:
    def __init__(self, word, chances):
        self.word = word.upper() # convert str to uppercase
        self.chances = word.len() # game starts with chances = word length
        self.guessed_chars = set() # collect guessed UNIQUE chars
        self.correct_chars = set() # place char indices in the correct position in the word

#
    def guess_char(self, char):
        self.guessed_chars.add(char)

        if char in self.word:
            char_positions = [i for i, c in enumerate(self.word) if c == char] # match
            self.correct_chars.update(char_positions) # add indices to char_positions
            print(char_positions)
            return True
        else:
            self.chances -= 1 # if guess is wrong, - 1 chance
            return False

    def win(self):
        return True # write logic later

    def lose(self):
        return self.chances <= 0 # game is lost when chances = 0