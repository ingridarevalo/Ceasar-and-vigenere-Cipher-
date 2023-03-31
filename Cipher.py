#Ceasar Cipher and Vigenere Ciper
letters = 'abcdefghijklmnopqrstuvwxyz'
#Ceasar Cipher Encrypt
def encrypt(message, key):
    ciphertext = []
    for letter in message:
        letter = letter.lower()
        if letter.isspace():
            ciphertext.append(letter)
        else:
            index = letters.find(letter)
            if index == -1:
                ciphertext.append(letter)
            else:
                new_index = (index + key) % 26
                ciphertext.append(letters[new_index])
    return ''.join(ciphertext)
#Ceasar Cipher
def decrypt(ciphertext, key):
    message = []
    for letter in ciphertext:
        letter = letter.lower()
        if letter.isspace():
            message.append(letter)
        else:
            index = letters.find(letter)
            if index == -1:
                message.append(letter)
            else:
                new_index = (index - key) % 26
                message.append(letters[new_index])
    return ''.join(message)
# vigenere Cipher
def vigenere_encrypt(message, key):
    ciphertext = []
    message = message.lower()
    key = key.lower()
    key_length = len(key)
    
    for i, letter in enumerate(message):
        if letter.isspace():
            ciphertext.append(letter)
        else:
            index = letters.find(letter)
            if index == -1:
                ciphertext.append(letter)
            else:
                key_index = letters.find(key[i % key_length])
                new_index = (index + key_index) % 26
                ciphertext.append(letters[new_index])
    return ''.join(ciphertext)

# vigenere Cipher decrypt
def vigenere_decrypt(ciphertext, key):
    message = []
    ciphertext = ciphertext.lower()
    key = key.lower()
    key_length = len(key)
    
    for i, letter in enumerate(ciphertext): 
        if letter.isspace():
            message.append(letter)
        else:
            index = letters.find(letter)
            if index == -1:
                message.append(letter)
            else:
                key_index = letters.find(key[i % key_length])
                new_index = (index - key_index) % 26
                message.append(letters[new_index])
    return ''.join(message)

# menu
def get_option(available_options, type_option):
    while True:
        print()
        print(f'Choose a {type_option}')
        
        for option in available_options:
            print('_' + option)
        print()
        user_option = input('Option: ')
        
        if user_option in available_options:
            return user_option
        else:
            print('Enter a valid option')
#option
        
cipher_options = ('Caesar', 'Vigenere')
action_options = ('Encrypt', 'Decrypt')
#input_option = (Enter Key, )
#main,  loop to repeat. 
def main():
    while True:
        
        cipher_choice = get_option(cipher_options, 'cipher')
        action_choice = get_option(action_options, 'action')

        if cipher_choice == 'Caesar':
            
            if action_choice == 'Encrypt':
                key = int(input('Enter the key (1 through 26): '))
                text = input('Enter the text to encrypt: ')
                ciphertext = encrypt(text, key)
                print(f'Ciphertext: {ciphertext}')
                
            elif action_choice == 'Decrypt':
                
                key = int(input('Enter the key (1 through 26): '))
                text = input('Enter the text to decrypt: ')
                message = decrypt(text, key)
                print(f'Message: {message}')
                
        elif cipher_choice == 'Vigenere':
            
            key = input('Enter the key (a sequence of letters): ')
            
            if action_choice == 'Encrypt':
                text = input('Enter the text to encrypt: ')
                ciphertext = vigenere_encrypt(text, key)
                print(f'Ciphertext: {ciphertext}')
                
            elif action_choice == 'Decrypt':
                text = input('Enter the text to decrypt: ')
                message = vigenere_decrypt(text, key)
                print(f'Message: {message}')
        print()
        user_exit = input("Type 'exit' to quit or press Enter to continue: ").lower()
        if user_exit == 'exit':
            break

if __name__ == '__main__':
    main()