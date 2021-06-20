numbers_tuple = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
    ("ten", "10"),
    ("eleven", "11"),
    ("twelve", "12"),
    ("thirteen", "13"),
    ("fourteen", "14"),
    ("fifteen", "15"),
    ("sixteen", "16"),
    ("seventeen", "17"),
    ("eighteen", "18"),
    ("nineteen", "19"),
    ("twenty", "20")
]


def change(String: str):
    numbers_tuple1 = list.copy(numbers_tuple)
    numbers_tuple1.reverse()
    new_String = String
    for key in numbers_tuple1:
        if key[0] in String:
            String = new_String
            new_String = String.replace(key[0], key[1])
    return new_String


def file_writer(file_path, dist_path):
    with open(file_path, "r") as reader:
        with open(dist_path, "w") as writer:
            for line in reader:
                line = line.lower()
                new_line = change(line)
                writer.write(new_line)


file_writer("input-q-1.txt", "output-q-1.txt")
