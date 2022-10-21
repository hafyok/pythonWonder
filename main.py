class Wonder:
    words_all = ["Чудо", "Поле"]

    def __init__(self, word):
        len_word = len(word)
        print(len_word)

        def empty_cell(self, len_cell):
            for i in range(len_cell):
                print("___ ", end="")
            print("")
            for i in range(len_cell):
                print("| | ", end="")
            print("")
            for i in range(len_cell):
                print("--- ", end="")

        empty_cell(self, len_word)


o = Wonder("чудоkkk")
