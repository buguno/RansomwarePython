def changeFiles(fileName, cryptoFunc, blockSize=16):
    with open(fileName, 'r+b') as _file:
        rawValue = _file.read(blockSize)
        while rawValue:
            cipherValue = cryptoFunc(rawValue)
            # Compara tamanho do bloco cifrado e plano (plainText)
            if len(rawValue) != len(cipherValue):
                raise ValueError('O valor cifrado {} tem um tamanho diferente do valor plano {}'.format(
                    len(cipherValue), len(rawValue)))

            _file.seek(- len(rawValue), 1)
            _file.write(cipherValue)
            rawValue = _file.read(blockSize)
