import re


class Extractor:
    digit_regex = "[0-9]+"
    letter_regex = "[a-zA-Z]+"

    def __init__(self):
        # data sets to read in output file
        self.words_dict = {}
        self.numbers_dict = {}
        # flag_is_word | flag_is_number
        self.state = (0, 0)
        self.begin_index = 0
        self.length = 0

    def read_input_and_write_output(self, input_address):
        with open(input_address) as input_file:
            for line in input_file:
                word_list = line.split()
                self.process_word_list(word_list)
            with open("output-q-2-2.txt", "a+") as output_file:
                for key, value in self.words_dict.items():
                    if value == 1:
                        output_file.write("{} : {} \n".format(key, value))
                output_file.write("total word_num {} \n".format(len(self.words_dict)))
                output_file.write("***********************************************************\n")
                for key, value in self.numbers_dict.items():
                    output_file.write("{}:{} \n".format(key, value))

    def process_word_list(self, word_list):
        for word in word_list:
            self.process_word(word)

    def process_word(self, word: str):
        self.length = 0
        self.state = (0, 0)
        for let_index in range(len(word)):
            if let_index == len(word) - 1:
                if self.state == (1, 0):
                    if re.match(Extractor.letter_regex, word[let_index]):
                        self.length += 1
                        self.extract_word(word, self.begin_index, self.length)
                    elif re.match(Extractor.digit_regex, word[let_index]):
                        self.extract_word(word, self.begin_index, self.length)
                        self.begin_index = let_index
                        self.extract_number(word, self.begin_index, self.length)
                elif self.state == (0, 1):
                    if re.match(Extractor.digit_regex, word[let_index]):
                        self.length += 1
                    self.extract_number(word, self.begin_index, self.length)
                else:
                    pass
            else:
                if re.match(Extractor.digit_regex, word[let_index]):
                    state = (0, 1)
                elif re.match(Extractor.letter_regex, word[let_index]):
                    state = (1, 0)
                else:
                    state = (0, 0)

                if state == self.state:
                    self.length += 1
                else:
                    if let_index > 0:
                        self.call_state_func(word)
                    self.length = 0
                    self.begin_index = let_index
                    self.change_state(state)

    def change_state(self, state):
        self.state = state

    def call_state_func(self, word):
        if self.state == (1, 0):
            self.extract_word(word, self.begin_index, self.length)

        elif self.state == (0, 1):
            self.extract_number(word, self.begin_index, self.length)

    def extract_word(self, word, begin_index, length):
        if length >= 1:
            end_index = begin_index + length + 1
            if self.words_dict.get(word[begin_index:end_index]):
                self.words_dict[word[begin_index:end_index]] += 1
            else:
                self.words_dict[word[begin_index:end_index]] = 1

    def extract_number(self, word, begin_index, length):
        end_index = begin_index + length + 1
        if self.numbers_dict.get(word[begin_index:end_index]):
            self.numbers_dict[word[begin_index:end_index]] += 1
        else:
            self.numbers_dict[word[begin_index:end_index]] = 1


e = Extractor()
e.read_input_and_write_output("input-q-2.txt")
