# author: Igor Alekhnovych
# date: 30 Oct 2020
# purpose: Lab 5

from tkinter import *

# to use the queue FIFO
from queue import Queue

# to use the shuffle for shuffling the cards
from random import shuffle


class CardGame():

    # initialises the application

    def __init__(self):

        # set up game logic here:
        # shuffle the cards before first use
        # variable for holding the score

        self.player_score = 0
        self.the_cards = self.load_cards()
        self.check = False

        self.init_window()


    # used by __init__
    # initialises the GUI window

    def init_window(self):
        root = Tk()
        root.geometry("300x200")
        root.title("Card Game")

        master_frame = Frame(master=root)
        master_frame.pack(expand=True)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design

        cards_frame = LabelFrame(master=master_frame)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(master=master_frame)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(master=master_frame)
        score_frame.grid(row=1, column=0, columnspan=2)

        # add elements into the frames

        self.open_card = Button(cards_frame)

        # set the card to the current card

        current_card = self.the_cards.get()
        self.update_score(current_card)

        the_card = PhotoImage(file=f'cards/{current_card[1]}_{current_card[0]}.gif')
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        closed_deck = Button(cards_frame, command=self.pick_card)
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        closed_deck.config(image=closed_card)
        closed_deck.grid(row=0, column=1, padx=2, pady=2)
        closed_deck.photo = closed_card

        done_button = Button(button_frame, text="I'm done!", command=self.done_playing)
        done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.reset_game)
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score), justify=LEFT)
        self.score_label.pack()

        root.mainloop()


    # called by the exit_button Button
    # ends the GUI application

    def game_exit(self):
        exit()


    # helper function to load the cards
    # puts everything in a list first as it needs to be shuffled
    # returns a queue

    def load_cards(self):
        cards = Queue(maxsize=52)
        suits = ("hearts", "diamonds", "spades", "clubs")
        types = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "queen", "jack", "king")
        card_list = []

        # Load cards into a list and shuffle them
        for c in suits:
            for t in types:
                card_list.append([c, t])

        shuffle(card_list)

        # Load the list into the Queue
        for card in card_list:
            cards.put(card)

        return cards


    # called when clicking on the closed deck of cards
    # picks a new card from the card FIFO
    # updates the display
    # updates the score

    def pick_card(self):
        if not self.check:
            new_card = self.the_cards.get()
            self.update_score(new_card)

            self.score_label.config(text="Your score: " + str(self.player_score))
            self.score_label.update_idletasks()

            the_card = PhotoImage(file=f'cards/{new_card[1]}_{new_card[0]}.gif')
            self.open_card.config(image=the_card)
            self.open_card.photo = the_card
            self.open_card.update_idletasks()

            self.check_scores()


    # contains the logic to compare if the score
    # is smaller, greater or equal to 21
    # sets a label

    def check_scores(self):
        if (self.player_score) == 21:
            self.score_label.config(text="Your score: 21. You hit the jack pot!")
            self.check = True  # used here to stop another card after the jackpot
        elif (self.player_score) < 21 and self.check:
            self.score_label.config(text="Your score: " + str(self.player_score) + " Well done! Play again?")
        elif (self.player_score) > 21:
            self.score_label.config(text="Your score: " + str(self.player_score) + " Bad luck, Game OVER!")
            self.check = True  # used here to stop another card after the game is over

        self.score_label.update_idletasks()


    # calculates the new score
    # takes a card argument of type

    def update_score(self, card):
        if card[1] == 'queen' or card[1] == 'king' or card[1] == 'jack':
            self.player_score += 10
        else:
            self.player_score += int(card[1])


    # this method is called when the "Done" button is clicked
    # it means that the game is over and we check the score
    # but we don't allow any further game play. When clicking
    # on the closed deck after this button is pressed, nothing
    # should happen. Only options are to ask for a new game or
    # exit the program after this button was pressed.

    def done_playing(self):
        self.check = True
        self.check_scores()


    # this method is called when the "New Game" button is clicked
    # resets all variables
    # sets the game's cards to the initial stage, with a freshly
    # shuffled card deck

    def reset_game(self):
        self.player_score = 0
        self.check = False
        self.the_cards.queue.clear()  # not threadsafe version
        self.the_cards = self.load_cards()
        self.pick_card()


# object creation here:
app = CardGame()
