import numpy as np
from word_database import dbWordSearch


class WordleHelper():
    """
    This class will do exhaustive for soulutions to a wordle word.
    """

    def __init__(self, word_length: int):
        self.word_length = word_length
        self.possible_letters = []
        self.known_letters = np.empty(word_length, dtype=str)
        self.illigal_letter = []

        self.db = dbWordSearch(self.word_length)

        self.known_letters.fill('_')

    def update_illigal_letters(self):
        """
        This method will add new letters to the illigel letters list
        """
        inpt = input("Input new unused char:")
        print(inpt)
        input()

        for i in inpt:
            if self.is_input_leagel(i) or i not in self.possible_letters or i not in self.known_letters:
                self.illigal_letter.append(i)


    def update_possible_letters(self):
        """This method will update the possible letters
        """
        inpt = input("Input new letters with unknown possition: ")

        for i in inpt:
            if self.is_input_leagel(i) and not self.used_letter(i):
                if len(self.possible_letters) <= self.word_length:
                    print("Appending letter")
                    self.possible_letters.append(i)
                else:
                    raise IndexError("You have more possible letters" +
                                     "then the length of the word")

    def update_known_letter(self):
        """
        This method will update a known position for a letter.
        The input asked for in the method takes a letter and position of
        this letter separated by a space.
        """
        inpt = input("Input new known letter: [letter pos] ")
        inpt = inpt.split(" ")
        inpt[1] = int(inpt[1])

        if not self.is_input_leagel(inpt[0]) or len(inpt[0]) > 1:
            print("Given non legal char or to many char.")
            return

        if inpt[1] >= self.word_length:
            print("Position out of range for given word length")
            return

        if self.known_letters[inpt[1]] == '_':
            self.known_letters[inpt[1]] = inpt[0]
        else:
            confirmation = inpt(f"Gvien position is already set, current letter is {self.known_letters[inpt[1]]}.\n Do you want to change this to {inpt[0]}: [y/n] ")
            if confirmation == "" or confirmation == "y":
                self.known_letters[inpt[1]] = inpt[0]
            else:
                return

    def is_input_leagel(self, letter):
        if 97 <=  ord(letter) <= 122:
            return True
        else:
            return False

    def used_letter_illigal(self, letter):
        if letter in self.possible_letters or letter in self.known_letters:
            return True
        return False

    def used_letter(self, letter):
        if letter in self.possible_letters or letter in self.illigal_letter:
            return True
        return False


    def print_kown_letters(self):
        print(f"Known letters with position:")
        print(self.known_letters)
        print(f"Known used letters: ")
        print(self.possible_letters)
        print(f"Known unused letters: ")
        print(self.illigal_letter)



    def get_words(self):
        words = self.db.search_words(''.join(self.known_letters), self.possible_letters, self.illigal_letter)
        print(words)

    def driver(self):
        keep_running = True

        welcome_mesasge = """Welcome to WorldeSolver!"""

        print(welcome_mesasge)

        main_menu =\
        """
        [1] Update known letters
        [2] Update possible letters
        [3] Update unused letters
        [4] Print status
        [5] Get possible words
        [!!] Exit program
        """

        case_actions = {"1": self.update_known_letter, "2": self.update_possible_letters,
                        "3": self.update_illigal_letters, "4": self.print_kown_letters, "5": self.get_words}


        while keep_running:
            print(main_menu)
            inpt = input("Select: ")
            if inpt == "!!":
                return
            if 49 <= ord(inpt) <= 53:
                case_actions[inpt]()
            else:
                print("Unkown option")




if __name__ == "__main__":
    inpt = int(input("How long is the word we are looking for? "))
    inst = WordleHelper(inpt)
    inst.driver()


