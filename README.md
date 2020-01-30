Ransomware Python :snake:
========================

O Ransomware é feito completamente em Python, tem por finalidade entender como funciona um ataque e é usado apenas para fins de estudo.
Por segurança, apenas os arquivos que estão no diretório **files** serão criptografados.

Instalção das dependências
--------------------------

Instalando usando pip;

	pip install -r requirements.txt

Alterando a chave de criptografia
---------------------------------

* Abra o arquivo main.py e altere a variavél global **HARDCODED_KEY**;
* Por padrão, a chave usada é de 32 caractres (Chave AES de 256 bits);
* **Fique atento à tabela abaixo**;

| bits | Qtd caracteres |
| :--: | :------------: |
| 128  |       16       |
| 192  |       24       |
| 256  |       32       |

Usando o ransomware
-------------------

Criptografando os arquivos:

	python3 main.py

Descriptografando os arquivos:

	python3 main.py -d