class Wonder:
    words_all = ["Чудо", "Поле"]
    word = ""
    letter = " "

    def __init__(self, word):
        len_word = len(word)
        self.word = word
        self.empty_cell(len_word)


    def empty_cell(self, len_cell):
        for i in range(len_cell):
            print("___ ", end="")
        print("")
        for i in range(len_cell):
            print("|" + self.letter + "| ", end="")
        print("")
        for i in range(len_cell):
            print("--- ", end="")
        print("")



    def input_letter(self):
        letter = input()
        if letter == self.word[0]:
            self.letter = letter
            self.empty_cell(len(self.word))
            print("верно")
        else:
            print("неверно")





o = Wonder("Чудо")
o.input_letter()
