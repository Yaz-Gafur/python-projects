alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for  i in plain_text:
        position = alphabet.index(i)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded test is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for i in cipher_text:
         position = alphabet.index(i)
         new_position = position - shift_amount
         new_letter = alphabet[new_position]
         plain_text += new_letter
    print(f"The decoded test is {plain_text}")

if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
else:
    decrypt(cipher_text = text, shift_amount = shift)

#* 2nd way of doing function above *

def caesar(text, shift_amount):
    if direction == "encode":
        cipher_text = ""
        for  i in text:
            position = alphabet.index(i)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded test is {cipher_text}")
    else:
        plain_text = ""
        for i in text:
            position = alphabet.index(i)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            plain_text += new_letter
        print(f"The decoded test is {plain_text}")

caesar(text = text, shift_amount = shift)