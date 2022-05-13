import sqlite3 as sl


class dbWordSearch():
    """
    Wrapper for sqlite db. This class will provide a way to 
    search for all possible word given known letter and word length.
    """
    def __init__(self, word_length):
        self.word_length = word_length
        self.db = sl.connect("dictionary-english.db")

    def create_querry(self, known_pos, known_letters, excluded_letters):
        """
        Method to build the SQL querry
        """
        base_querry = "SELECT DISTINCT word FROM english WHERE "
        querry_word_length = f"(LENGTH(word) LIKE {self.word_length}) "
        querry_known_letters = f"word LIKE \"{known_pos}\""
        querry_possible_letters = [f"word LIKE \"%{i}%\"" for i in known_letters]
        querry_excluded_letters = [f"word NOT LIKE \"%{i}%\"" for i in excluded_letters]

        base_querry += querry_word_length
        base_querry += "AND " + querry_known_letters + " "

        for i in querry_possible_letters:
            #print(i)
            #print("AND " + i + " ")
            base_querry += "AND " + i + " "

        for i in querry_excluded_letters:
            base_querry += "AND " + i + " "


        #print(base_querry)
        return base_querry + ";"



    def search_words(self, known_pos, known_letters = "", excluded_letters = ""):
        get_querry = self.create_querry(known_pos, known_letters, excluded_letters)
        exec_querry = self.db.execute(get_querry)
        return [i for i in exec_querry]




if __name__ == "__main__":
    testCase = dbWordSearch(5)
    known_pos = "_e___"
    known_letters = "ok"
    excluded = "c"
    print(testCase.search_words(known_pos, known_letters, excluded))


