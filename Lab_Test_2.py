# author: Igor Alekhnovych
# date: 11-12-2020
# purpose: Lab Test 2

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """

    def __init__(self, file_name = 'file.txt'):
        self._cursor = 0
        self._characters = []
        self._filename = file_name

    # cursor getter and setter

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, value):

        # raise an exception if cursor is not an integer
        # raise an exception if cursor is negative number

        if not isinstance(value, int):
            raise TypeError('Not an Integer (Cursor)')
        else:
            if value < 0:
                raise ValueError('Negative Number (Cursor)')
            else:
                self._cursor = value

    # characters getter and setter

    @property
    def characters(self):
        return self._characters

    @characters.setter
    def characters(self, value):

        # raise an exception if characters is not a string
        # raise an exception if characters is an empty string

        if not isinstance(value, str):
            raise TypeError('Not a String (Characters)')
        else:
            if not value.strip():
                raise ValueError('Empty String (Characters)')
            else:
                self._filename = value

    # filename getter and setter

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):

        # raise an exception if file name is not a string
        # raise an exception if file name extension is invalid
        # raise an exception if file name is an empty string

        if not isinstance(value, str):
            raise TypeError('Not a String (File Name)')
        else:
            if not value.strip():
                raise ValueError('Empty String (File Name)')
            else:
                if not value.endswith('.txt'):
                    raise ValueError('Wrong File Extension (File Name)')
                else:
                    self._filename = value


    def insert(self, character):
        """
        Method inserts a character at
        the current cursor position.

        Argument:
        ---------
        character : str
            The character to insert

        Returns: no return
        -------
        """
        self.characters.insert(self.cursor, character)
        self.cursor += 1

    def delete(self):
        """
        Method deletes a character from
        the current cursor position.

        Arguments: none
        Returns: none
        """

        # catch an exception if cursor is out of range

        try:
            del self.characters[self.cursor]

        except IndexError as index_error:
            print(index_error)

    def save(self):
        """
        Method saves all characters in
        the characters list to a file.

        Arguments: none
        Returns: none
        """

        # catch an exception if the file was not found

        try:
            with open(self.filename, 'w') as f:
                f.write(''.join(self.characters))

            print(f"Hey, I have created {self.filename}")

        except FileNotFoundError as file_error:
            print(file_error)

    def forward(self, steps):
        """
        Method forward to a particular
        position in characters [].

        Argument:
        ----------
        steps : int
            The amount of steps the cursor
            should be pushed forward by

        Returns: no return
        -------
        """

        self.cursor += steps
        print(f"Update: I am going {steps} steps forwards")

    def backward(self, steps):
        """
        Method backward moves the cursor position to
        that specific location in the characters list.

        Argument:
        ----------
        steps : int
            The amount of steps to go back

        Returns: no return
        -------
        """

        # raise an exception if number of steps is
        # greater than number of characters or negative

        if steps > len(self.characters) or steps < 1:
            raise ValueError('invalid number of steps')
        else:
            self.cursor -= steps
            print(f"Update: I am going {steps} steps backwards")


# initialising an object and using the class

doc = Document("lab_test_2.txt")
characters = 'steve hobs'

for letter in characters:
    doc.insert(letter)

doc.backward(5)
doc.forward(1)

doc.delete()
doc.insert('j')

doc.save()