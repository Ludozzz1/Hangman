class Hangman:
    def __init__(self, word: str) -> None:
        self.passingthru = word
        self.word = list(word)
        self.letters = len(word)
        self.guesses = []
        self.guesses_left = 6
        for i in range(self.letters):
            self.guesses.append("_")
    def guess(self, guessed_letter: str) -> str:
        guessed_right = False
        if guessed_letter in self.word:
            guessed_right = True
            for i in range(self.letters):
                if self.word[i] == guessed_letter:
                    self.guesses[i] = guessed_letter
        if guessed_right == False:
            self.guesses_left -= 1
            print("You have " + str(self.guesses_left) + " guesses left.")
        return self.guesses
    
    def end_game(self) -> bool:
        if self.guesses_left == 0:
            return True
        return False
    
    def win_game(self) -> bool:
        print(self.guesses)
        if self.guesses == self.word:
            return True
        return False

