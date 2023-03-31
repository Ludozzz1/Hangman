from hangman import *

word = input("Say the word:\n")
game = Hangman(word)
end = False
win = False
while 1:
    guessed_letter = input("Guess a letter:\n")
    half_word = game.guess(guessed_letter)
    print(half_word)
    win = game.win_game()
    if win == True:
        print("You win!")
        break
    end = game.end_game()
    if end == True:
        print("You lose!")
        break