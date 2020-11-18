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

class WordDuplication(WordGames):
    """
    Class to represent the word duplication game.
    This class inherits from the WordGames base class.

    Attributes: Inherited from WordGames
    -----------
        __my_words : str
            Read from user input and identifies the 
            word or sentence that a user has inputted.

    Methods:
    --------
        word_play:
            Overriden method from the base class's
            word_play. The gameplay happens here.
    """

    def word_play(self):
        """
        Plays the game. Overrides super().word_play().
        This game duplicates every word that the user has
        entered. The result is printed to standard output.

        Attributes: None.
        -----------
        
        Returns: None.
        --------
        """

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

class WordScramble(WordGames):
    """
    Class to represent the word scrambling game.
    This class inherits from the WordGames base class.

    Attributes: Inherited from WordGames
    -----------
        __my_words : str
            Read from user input and identifies the word
            or sentence that a user has inputted.
        
    Methods:
    --------
        word_play:
            Overriden method from the base class's
            word_play. The gameplay happens here.
    """

    def word_play(self):
        """
        Plays the game. Overrides super().word_play().
        This game scrambles every word that the user has
        entered. The result is printed to standard output.
        Words need to be longer than 3 characters in length
        to be scrambled.

        Attributes: None.
        -----------

        Returns: None.
        --------
        """

        # Print user input
        super().word_play()

        my_sentence = self.the_words.strip().split()

        # Get the word from the sentence
        for index, word in enumerate(my_sentence):
            # check the length of the word > 3
            if len(word) > 3:
                # swap the indices of the 2 and last element
                temp_word = list(word)
                if (',' in temp_word) or ('.' in temp_word):
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-3]
                    temp_word[-3] = temp
                else:
                    # split the word in to a list of characters and swap
                    # this swap leaves first and last in tact
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-2]
                    temp_word[-2] = temp

                # Join the characters together and form the word
                swapped_word = ''.join(temp_word)
                # Replace the previous word at that position with the new swapped word
                my_sentence[index] = swapped_word
            else:
                # Since the length of the word < 3 don't swap the word
                my_sentence[index] = word

        # Join all the words with a space
        the_swap = ' '.join(my_sentence)
        # Print word
        print('Scramble: ' + the_swap)

# prints the docstrings info
# if this class was a python module
# print(WordGames.__doc__)

# Create instances of the classes here:
wd = WordDuplication()
wd.word_play()

ws = WordScramble()
ws.word_play()