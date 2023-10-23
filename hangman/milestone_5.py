import random
class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_gusses: list
        A list of guesses that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the guess is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for char in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_gusses = []

    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked

        '''
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
        '''
        Asks the user to input a letter and checks two things:
        1. If the user did indeed input a single letter
        2. If the user has already made that guess
        If it passes both checks, it calls the check_guess method.
        '''
        print(f'\nGuessed so far: {self.word_guessed}')
        guess = input('Guess a letter: ')
        if not guess.isalpha() or len(guess) != 1:
            print('Invalid letter. Please, enter a single alphabetical character')
        elif guess in self.list_of_gusses:
            print('You already tried that letter!')
        else:
            self.check_guess(guess)
            self.list_of_gusses.append(guess)

def play_game(word_list):
    print(type(word_list))
    '''
    Function contains the main game loop
    Sets number of lives and initalizes Hangman
    The game will last until:
    - When the reaminng number of lives in num_lives is 0
    - or when there are no more unique letter to guess, counted by num_letters

    Parameters:
    ----------
    word_list: list
        List of words to be randomly picked

    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost')
            print('The word was:', game.word)
            return
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            return


if __name__ == '__main__':
    word_list = ['apples',  'banana', 'blueberriers', 'melons', 'corn']
    play_game(word_list)