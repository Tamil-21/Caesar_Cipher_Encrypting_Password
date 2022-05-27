
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction =  input("Enter 'Encode' to encode the message or type 'Decode' to decode:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Enter the shift amount to be shifted:\n"))

def encryption(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"Your encoded text is {cipher_text}")

def decryption(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"Your decoded text is {plain_text}")

if direction == 'encode':
    encryption(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decryption(cipher_text = text, shift_amount = shift)

