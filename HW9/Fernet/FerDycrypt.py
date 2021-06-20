from Utils import *


class Decrypt:
    def __init__(self, key, en_source_path=None, en_dest_path=None, mode=None):
        self.key = key
        self.en_source_path = en_source_path
        self.en_dest_path = en_dest_path
        self.mode = mode
        self.backup_file = None
        self.backup_path = None

    def decrypt(self):
        print(self.en_source_path)
        if not self.en_source_path:
            en_input = get_multiline_input()
            en_input = bytes(en_input, 'utf-8')
        else:
            with open(self.en_source_path, 'rb') as source:
                en_input = source.read()

        token = Fernet(self.key).decrypt(en_input)
        if self.en_dest_path:
            out_put_path = self.en_dest_path
        elif self.en_source_path and not self.en_dest_path:
            out_put_path = encrypted_dist_maker(self.en_source_path, key="_decrypted")
        else:
            out_put_path = path_generator.send("Fernet_decrypt")
            next(path_generator)

        with open(out_put_path, 'wb') as result_file:
            result_file.write(token)

    def __enter__(self):
        self.back_up_path = encrypted_dist_maker(self.en_source_path, key="backup")
        with open(self.back_up_path, 'wb') as output_file:
            with open(self.en_source_path, 'rb') as input_file:
                content = input_file.read()
                fer_obj = Fernet(self.key)
                encrypted_content = fer_obj.decrypt(content)
            output_file.write(encrypted_content)
            self.backup_file = self.back_up_path
            self.backup_file = open(self.back_up_path, self.mode)
        return self.backup_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.backup_file.close()
        if exc_type:
            os.remove(self.back_up_path)
            return True

        with open(self.back_up_path, 'rb') as in_file:
            content = in_file.read()
            fer_obj = Fernet(self.key)
            encrypted_output = fer_obj.encrypt(content)
            with open(self.en_source_path, 'wb') as out_file:
                out_file.write(encrypted_output)








