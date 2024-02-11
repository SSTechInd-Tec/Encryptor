#  imported modules 
import os
import argparse as ap
from getpass import getpass
from AesEverywhere import aes256


# Hi this is me 

#  encryptor function that encrypt files using aes256
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


#  decryptor function that decrypt files using aes256
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


#  command line arguments use to define what to do
arg = ap.ArgumentParser()
#  -d for decryption
arg.add_argument('-d', action='store_true', help='This option use for decrypting the file.')
#  -e for encryption
arg.add_argument('-e', action='store_true', help='This option use for encrypting the file.')
#  filename which we will define our file name instead of filename
arg.add_argument('filename', type=str, help='Use to specify the file name.')

pa = arg.parse_args()

#  check what to when any of above arguments use

#  if user enter -e
if pa.e:
	#  ask for password. this password is use to encrypt file
	passwd = getpass('Enter File Password: ')
	encryptor(pa.filename, passwd)
	print('Encrypted successfully')

#  if user enter -d
elif pa.d:
	#  ask for password. this password is use to decrypt file
	passwd = getpass('Enter File Password: ')
	decryptor(pa.filename, passwd)
	print('Decrypted successfully')
