import random


class Wonder:
    words_all = ["Чудо", "Поле", "МИРЭА", "Чупакабра", "Valorant"]
    done_letters = []
    word = ""
    letter = " "

    def __init__(self):
        word = random.choice(self.words_all)
        len_word = len(word)
        self.word = word
        self.done_letters = [0] * len_word
        self.empty_cell(len_word)
        self.input_letter()


    def empty_cell(self, len_cell):
        for i in range(len_cell):
            print("___ ", end="")
        print("")
        for i in range(len_cell):
            #if self.letter in self.done_letters:
            if self.done_letters[i] != 0:
                print("|" + self.done_letters[i] + "| ", end="")
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
            self.done_letters[self.word.index(self.letter)] = self.letter
            print(self.done_letters)
            print("\n" * 100)
            self.empty_cell(len(self.word))
        else:
            print("неверно")
            self.input_letter()




o = Wonder()
