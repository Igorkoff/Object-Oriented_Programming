# author: Igor Alekhnovych
# date: 13-11-2020
# purpose: Lab 8

class WordGames:
    """
    Class to represent the word game's base class.
    Methods and attributes that every type of word
    game should have are defined here.
    ...
    Attributes:
    -----------
        __my_words : str
        Read from user input and identifies the word
        or sentence that a user has inputted.

    Methods:
    --------
        the_words:
            Property getter method that returns
            the value of the user inputted word
            or sentence

        word_play:
            Contains logic for playing the game.
            Child classes should override this
            method in order to implement their own
            game logic.
    """
    def __init__(self):
        """
        Constructs the necessary attributes for the
        WordGame object.

        Parameters: None.
        -----------

        Instance variables:
        -------------------
            __my_words : str
                Variable that holds the user inputted word or
                sentence. Set to enforced encapsulation via
                name mangling.
        """
        self.__my_words = input("Please enter a word or sentence: ")

    @property
    def the_words(self):
        """
        Property method to return the value of the user
        inputted word or sentence.

        Parameters: None.
        -----------

        Returns:
        ________
            __my_words : str
                The value of the word or sentence that has
                been inputted by a user.
        """
        return self.__my_words

    def word_play(self):
        """
        Plays the game. The base class version of playing
        the game simply prints the value that has been
        inputted.

        Parameters: None.
        -----------

        Returns: None.
        --------
        """
        print("User input was: " + self.the_words)

class WordDuplication(WordGames): # you provide docstrings
    def word_play(self):
        # Print user input
        super().word_play()

        # First Type: Duplicate Characters
        my_sentence = self.the_words
        result_1 = ''.join([char * 2 for char in my_sentence])

        # Second Type: Duplicate Words
        my_sentence = self.the_words.strip().split()
        my_list = []
        for index, words in enumerate(my_sentence):
            my_list.extend([my_sentence[index]] * 2)

        # Join all the words with spaces
        result_2 = ' '.join(my_list)

        # Print Results
        print('Duplication 1: ' + result_1)
        print('Duplication 2: ' + result_2)
        print('')

class WordScramble(WordGames): # you implement this and provide docstrings
    pass


# prints the docstrings info
# if this class was a python module
print(WordGames.__doc__)

# Create instances of the classes here:
wd = WordDuplication()
wd.word_play()

ws = WordScramble()
ws.word_play()