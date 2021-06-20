import argparse
import binascii

import cryptography
from cryptography.fernet import Fernet

import FerDycrypt
import FerEncrypt
import Utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key_gen", action="store_const", const=True,
                        help="A fernet key generator", dest='key_gen')
    parser.add_argument("-s", "--save_path", help="identifying the save_path for generated key ",
                        dest='save_path')

    subparsers = parser.add_subparsers(help="the Encryptor services", dest="service")
    encryptor = subparsers.add_parser('encrypt', help="File encryptor")
    decryptor = subparsers.add_parser('decrypt', help="File decryptor")

    encryptor.add_argument("-enk", "--key", required=True,
                           help="key for encrypting content", dest='en_key')
    encryptor.add_argument("-s", "--source", help="source file for encrypting", dest='source')
    encryptor.add_argument("-d", "--destination", help="dest file for storing encrypted file", dest='dest')
    decryptor.add_argument("-dek", "--key", required=True,
                           help="key for encrypting content", dest='de_key')
    decryptor.add_argument("-s", "--source", help="source file for encrypting", dest='source')
    decryptor.add_argument("-d", "--destination", help="dest file for storing decrypted file", dest='dest')

    container = parser.parse_args()
    print(container)

    try:
        if container.service:
            if container.service == 'encrypt':
                key = Utils.key_extractor(container.en_key)
                encryptor = FerEncrypt.Encrypt(key=key, en_source_path=container.source,
                                               en_dest_path=container.dest)
                encryptor.fernet_encrypt()
            elif container.service == 'decrypt':
                key = Utils.key_extractor(container.de_key)
                decryptor = FerDycrypt.Decrypt(key=key, en_source_path=container.source,
                                               en_dest_path=container.dest)
                decryptor.decrypt()
        else:
            if container.save_path:
                key = next(Utils.key_generator)
                with open(container.save_path, 'wb') as key_holder:
                    key_holder.write(key)
                    print(f"KEY saved in {container.save_path}")
            else:
                key = next(Utils.key_generator)
                print(key)

    except FileNotFoundError as fe:
        print(fe)
    except FileExistsError as fee:
        pass
    except cryptography.fernet.InvalidToken:
        print("Invalid key or operation")
    except binascii.Error as be:
        print("Error: wrong key for encryption or decryption")




