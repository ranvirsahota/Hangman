import random
class Hangman:
    def __init__(self, word_list, num_lives = 5) -> None:
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for char in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = 3
        self.word_list = word_list
        self.list_of_gusses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for index in range(len(self.word)):
                if guess == self.word[index]: self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            print(f'Guessed so far: {self.word_guessed}')
            print(f'Live left: {self.num_lives}')
            guess = input('Guess a letter: ')
            if not guess.isalpha and len(guess) == 1:
                print('Invalid letter. Please, enter a single alphabetical character')
            elif guess in self.list_of_gusses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_gusses.append(guess)

game = Hangman(['apples',  'banana', 'blueberriers', 'melons', 'corn'])
game.ask_for_input()