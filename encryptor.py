import os
from AesEverywhere import aes256
import argparse as ap
from getpass import getpass


def encryptor(filename, salt):
	if os.path.isfile(filename):
		with open(filename, mode='rb') as file:
			bytes = file.read()
			decoded_bytes = bytes.decode('latin1')
			with open(filename, mode='wb') as file2:
				cipher_bytes = aes256.encrypt(decoded_bytes, salt)
				bytes2 = cipher_bytes.decode().encode('latin1')
				file2.write(bytes2)
	else:
		print('No Such File')

def decryptor(filename, salt):
	if os.path.isfile(filename):
		with open(filename, mode='rb') as file:
			bytes = file.read()
			decoded_bytes = bytes.decode('latin1')
			with open(filename, mode='wb') as file2:
				normal_bytes = aes256.decrypt(decoded_bytes, salt)
				bytes2 = normal_bytes.decode().encode('latin1')
				file2.write(bytes2)
	else:
		print('No Such File')

arg = ap.ArgumentParser()
arg.add_argument('-d', action='store_true', help='This option use for decrypting the file.')
arg.add_argument('-e', action='store_true', help='This option use for encrypting the file.')
arg.add_argument('filename', type=str, help='Use to specify the file name.')

pa = arg.parse_args()

if pa.e:
	passwd = getpass('Enter File Password: ')
	encryptor(pa.filename, passwd)
	print('Encrypted successfully')
elif pa.d:
	passwd = getpass('Enter File Password: ')
	decryptor(pa.filename, passwd)
	print('Decrypted successfully')
