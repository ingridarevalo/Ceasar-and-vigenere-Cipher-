#Ingrid Berenice Arevalo Aguilar 
#https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=&cad=rja&uact=8&ved=2ahUKEwjx1KrF78n-AhXICjQIHWt8C58QtwJ6BAgDEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQYng_rXg5OQ&usg=AOvVaw2MEiKm9lVtnj9gnOMgC2oG
#CSCI 233 
#Demo
#Date: 04/28/2023

#Ceasar Cipher 

letters = 'abcdefghijklmnopqrstuvwxyz' # Define the alphabet string

# Define a cipher helper function that takes in message, key, and operation (encrypt/decrypt)
def cipher_helper(message, key, operation):

    result = [] # Initialize the result list
    # Convert the message and key to lowercase
    message = message.lower() 
    key = key.lower()
    
    key_length = len(key)# Calculate the length of the key

    # Loop through each character in the message
    for i, letter in enumerate(message):
       
        if letter.isspace(): # If the character is a space
            result.append(letter) #append it to the result list
        else:
            # Find the index of the character in the alphabet
            index = letters.find(letter)
            
            if index == -1:# If the character is not in the alphabet.
                result.append(letter) #append it to the result list
            else:
                # Find the index of the corresponding character in the key
                key_index = letters.find(key[i % key_length]) # (i % key_length) ensures that the key is repeated as needed for each character in the message
                # If the operation is encryption, calculate the new index
                if operation == 'Encrypt':
                    #calculate by adding the index and the key index alfabeth
                    new_index = (index + key_index) % 26 #takes the result modulo 26 to ensure that the new index is within the range of the alphabet
                # If the operation is decryption, calculate the new index
                else:
                    new_index = (index - key_index) % 26
                # Append the new character to the result list
                result.append(letters[new_index])
    # Join the result list into a string and return it
    return ''.join(result)

# Define the Caesar encryption function
def caesar_encrypt(message, key):
        #calls the cipher_helper function to perform Caesar encryption on the message. 
    return cipher_helper(message, letters[key % 26], 'Encrypt')

# Define the Caesar decryption function
def caesar_decrypt(ciphertext, key):
     #calls the cipher_helper function to perform Caesar decryption on the ciphertext. 
    return cipher_helper(ciphertext, letters[key % 26], 'Decrypt')
