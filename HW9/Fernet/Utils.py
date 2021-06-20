from cryptography.fernet import Fernet
import os


def key_generator():
    """
    Generator which generates key every time which is called
    :return:
    """
    while True:
        key = Fernet.generate_key()
        yield key


def path_generator(source=None, name_input=None):
    """
    generates path for saving the keys in the current directory
    if we wanted to save file for keys
    name_input  = 'key'
    :return:
    """

    current_dir = os.getcwd()
    file_counter = -1
    while True:
        file_counter += 1
        file_name = yield
        if file_name or file_counter == 0:
            path = ''
            if file_name is not None:
                path = os.path.join(current_dir, file_name + str(file_counter))
            yield path


def key_saver(path, key):
    """
    store a Fernet key in a file we make path absolute before
    passing to this function if no error or exception
    occured function returns True  which mean the key is saved
    in the file
    :param path:
    :param key:
    :return: True
    """
    if not os.path.isfile(path):
        raise Exception("Error:File Not found make sure you enterd right path")
    with open(path, 'wb')as key_holder:
        key_holder.write(key)

    return True


def get_multiline_input():
    """
    this function returns a list of the lines we entered
    Process is finished when we have a keyboard interrupt
    :return List
    """
    input_str = []
    while True:
        try:
            temp_input = input(">")
            if not (temp_input.isspace() or temp_input == ''):
                input_str.append(temp_input)
        except KeyboardInterrupt:
            break

    return " ".join(input_str)


def encrypted_dist_maker(path, key):
    if not os.path.isfile(path):
        raise Exception("Error:File Not found make sure you enterd right path")

    full_path = os.path.abspath(path)
    dir_name = os.path.dirname(full_path)
    base_name = os.path.basename(full_path)
    file_name, file_ext = os.path.splitext(base_name)
    return os.path.join(dir_name, file_name + key + file_ext)


def key_extractor(key):
    if os.path.isfile(key):
        with open(key, 'rb') as key_file:
            key = key_file.read()
        return key
    else:
        return key


path_generator = path_generator()
key_generator = key_generator()

path_generator.send(None)
path_generator.send('')
next(path_generator)
