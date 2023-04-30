import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox, QLineEdit #import the required modules

from Cipher_func import caesar_encrypt, caesar_decrypt, vigenere_encrypt, vigenere_decrypt, cipher_helper #import the functions from the Cipher.py


class CipherApp(QWidget): #create a class that inherits from QWidget
    #initializes the instance and calls the initUI method
    def __init__(self): #initialize the class
        super().__init__() #call the super class constructor

        self.initUI() #call the initUI method

    def initUI(self):   #create the UI
        layout = QVBoxLayout() #create a vertical layout
        # Cipher selection
        self.cipher_label = QLabel('Choose a Cipher:') #create a label
        layout.addWidget(self.cipher_label) #add the label to the layout
        self.cipher_combobox = QComboBox() #create a combobox
        self.cipher_combobox.addItems(['Caesar', 'Vigenere']) #add the items to the combobox
        layout.addWidget(self.cipher_combobox) #add the combobox to the layout
        # Action selection
        self.action_label = QLabel('Choose an Action:') #create a label
        layout.addWidget(self.action_label) #add the label to the layout
        self.action_combobox = QComboBox() #create a combobox
        self.action_combobox.addItems(['Encrypt', 'Decrypt']) #add the items to the combobox
        layout.addWidget(self.action_combobox) #add the combobox to the layout
        # Key input#create a label for the key input
        self.key_label = QLabel(' Enter key: \n *Caesar Cipher: Numbers only \n *Vigenere Cipher: key optional and words only.') 
        layout.addWidget(self.key_label) #add the label to the layout
        #create a line edit for the key input
        self.key_input = QLineEdit() 
        layout.addWidget(self.key_input) #add the line edit to the layout 
        # Text input
        self.text_label = QLabel('Enter text:') #create a label
        layout.addWidget(self.text_label) #add the label to the layout
        self.text_input = QTextEdit() #create a text edit
        layout.addWidget(self.text_input) #add the text edit to the layout
        # Result display
        self.result_label = QLabel('Result:') #create a label
        layout.addWidget(self.result_label) #add the label to the layout
        self.result_display = QTextEdit() #create a text edit
        self.result_display.setReadOnly(True) #set the text edit to read only
        layout.addWidget(self.result_display) #add the text edit to the layout

        # Execute button
        self.execute_button = QPushButton('Execute') #create a button
        self.execute_button.clicked.connect(self.execute_action) #connect the button to the execute_action method
        layout.addWidget(self.execute_button) #add the button to the layout

        self.setLayout(layout) #set the layout to the window

    def execute_action(self):  # create the execute_action method
        cipher = self.cipher_combobox.currentText()  # get the current text from the cipher combobox
        action = self.action_combobox.currentText()  # get the current text from the action combobox
        key = self.key_input.text()  # get the text from the key input
        text = self.text_input.toPlainText()  # get the text from the text input

        if cipher == 'Caesar':  # check if the cipher is Caesar
            try:
                key = int(key)  # convert the key to an integer
            except ValueError:
                result = 'Invalid key for Caesar cipher. Please enter a number.'
            else:
                if action == 'Encrypt':  # check if the action is Encrypt
                    result = caesar_encrypt(text, key)  # call the caesar_encrypt function

                elif action == 'Decrypt':  # check if the action is Decrypt
                    result = caesar_decrypt(text, key)  # call the caesar_decrypt function
                else:  # if the action is not Encrypt or Decrypt
                    result = 'No key option not supported for Caesar cipher'  # set the result to the error message
        elif cipher == 'Vigenere':  # check if the cipher is Vigenere
            if action == 'Encrypt':  # check if the action is Encrypt
                result = vigenere_encrypt(text, key) # call the vigenere_encrypt function
                if not key:  # Check if the key is not provided
                    result = 'No key provided for Vigenere encryption. Please enter a key.'
                    # call the vigenere_encrypt function
            elif action == 'Decrypt':  # check if the action is Decrypt
                if key:  # check if the key is provided
                    result = vigenere_decrypt(text, key)  # call the vigenere_decrypt function with the key
                else:
                    result = vigenere_decrypt(text)  # call the vigenere_decrypt function without the ke
                    self.result_display.setPlainText("No key provided. Decryption results have been saved to decrypt_nokey.txt  ")
                result #set the result to the error message
    
        self.result_display.setPlainText(result) #set the result to the result display
# shows the window, and starts the application's event loop.
if __name__ == '__main__': #check if the script is being run directly
    app = QApplication(sys.argv) #create an instance of QApplication
    ex = CipherApp() # Create an instance of our class
    ex.show() # Show the form
    sys.exit(app.exec_()) # Start the application
    
