alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 27
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}.")

plain_text= input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))

encrypt(plain_text, shift_amount)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def decrypt(old_text, new_shift_amount):
    decrypted_cipher = ""
    for letter in old_text:
        position = alphabet.index(letter)
        new_position = position - new_shift_amount % 2
        new_letter = alphabet[new_position + 1]
        decrypted_cipher += new_letter
    print(f"The decoded text is: {decrypted_cipher}.")

decrypt(old_text = plain_text, new_shift_amount = shift_amount)