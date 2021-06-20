def read_input_file(input_path):
    upper_words_list =[]
    with open(input_path) as input_file:
        for line in input_file:
            words_list= line.split()
            if is_upper(words_list[0]):
                upper_words_list.append(words_list[0])
        with open("output-q-2-3.txt","a+") as outputfile:
            for word in upper_words_list:
                outputfile.write(word+", ")


def is_upper(word:str):
    if word[0].isupper():
        return True
    return False

#call the function to operate
read_input_file("output-q-2-2.txt")