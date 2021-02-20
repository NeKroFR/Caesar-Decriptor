import string

alphabet = string.ascii_lowercase


text_base= input("Enter your  text here:")
encrypted_message = ""
letter =

for i in text_base:

        if i in alphabet:
            position = alphabet.find(i)
            new_position = letter+1
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += i

print(encrypted_message)

input('\npress enter to leave')
