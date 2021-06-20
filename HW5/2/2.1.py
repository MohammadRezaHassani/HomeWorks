import re
EOF_regex = "\.(\[[0-9]+\])+(\s)+|\.(\[[0-9]+\])+\n|\.\n|\.(\[[0-9]+)\n|\.(\s)+"


def convert_file_to_list(in_path):
    file_lines_list = []
    with open(in_path) as input_file:
        for lines in input_file:
            file_lines_list.append(lines)

    return file_lines_list


def make_output_file(out_path):
    processed_list=lines_list_process()
    with open(out_path, "a+") as output:
        for i in range(len(processed_list)):
            output.write(processed_list[i]+"\n")



def lines_list_process():
    processed_list=[]
    regex=re.compile(EOF_regex)
    input_list = convert_file_to_list("input-q-2.txt")
    for line in input_list:
        if re.search(EOF_regex,line):
            begin_index=0
            for i in regex.finditer(line):
                begin =i.start()
                length=len(i.group())
                end_endex=begin+length
                processed_list.append(line[begin_index:end_endex])
                begin_index=end_endex

    return processed_list

make_output_file("output-q-2-1.txt")
