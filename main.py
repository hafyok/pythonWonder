class Wonder:
    words_all = ["Чудо", "Поле"]
    word = ""
    letter = " "

    def __init__(self, word):
        len_word = len(word)
        self.word = word
        self.empty_cell(len_word)
        self.input_letter()


    def empty_cell(self, len_cell):
        for i in range(len_cell):
            print("___ ", end="")
        print("")
        for i in range(len_cell):
            if self.letter == self.word[i]:
                print("|" + self.letter + "| ", end="")
            else:
                print("| | ",end="")
        print("")
        for i in range(len_cell):
            print("--- ", end="")
        print("")
        self.input_letter()



    def input_letter(self):
        letter = input()
        if letter in self.word:
            self.letter = letter
            self.empty_cell(len(self.word))
            print("верно")
        else:
            print("неверно")
        self.empty_cell(len(self.word))





o = Wonder("Чудо")
