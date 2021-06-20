from Utils import *


class Encrypt:
    # Todo search how to give value to a generator

    def __init__(self, key, en_source_path=None, en_dest_path=None):
        self.key = key
        self.en_source_path = en_source_path
        self.en_dest_path = en_dest_path

    def fernet_encrypt(self):
        """
        this function encrypts input base on four possible scenarios
        if input and output file exist the encrypted input_file
        is saved in the output
        if input exists and output file not specified
        encrypted input is saved in the same location as input
        if input is doesn't exists but output exists
        the written lines from console are saved
        if none of input and output exists
        the written line from console are
        saved with the name Fernet(number).ext
        :return:
        """
        if not self.en_source_path:
            en_input = get_multiline_input()
            en_input = bytes(en_input, 'utf-8')
        else:
            with open(self.en_source_path, 'rb') as source:
                en_input = source.read()

        token = Fernet(self.key).encrypt(bytes(en_input))
        if self.en_dest_path:
            out_put_path = self.en_dest_path
        elif self.en_source_path and not self.en_dest_path:
            out_put_path = encrypted_dist_maker(self.en_source_path, key="_encrypted")
        else:
            out_put_path = path_generator.send("Fernet_encrypt")
            next(path_generator)
            # here we write our encrypted file
        with open(out_put_path, 'wb') as result_file:
            result_file.write(token)


