import random
import string

chars = " "+ string.punctuation + string.digits + string.ascii_letters
chars= list(chars)
keys = chars.copy()
random.shuffle(chars)

"""print(f"chars: {chars}")
print(f"keys:  {keys}")"""

#ENCRYPT
plain_text = input("Enter a message to encrypt:  ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"original message  : {plain_text}")
print(f"Encrypted message : {cipher_text}")
    

#DECRYPT
cipher_text = input("Enter a message to decrypt:  ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"Encrypted message : {cipher_text}")
print(f"Orginal   message : {plain_text}")
