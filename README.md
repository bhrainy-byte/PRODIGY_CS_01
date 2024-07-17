# Caesar Cipher

This project implements the Caesar Cipher, a classic encryption technique used to secure messages. The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet. This simple yet effective method was named after Julius Caesar, who used it to communicate with his officials.


#Features
Encryption: Encode messages by shifting letters by a specified number of positions.
Decryption: Decode messages by reversing the shift applied during encryption.
Custom Shift Value: User can specify the number of positions to shift the letters.
Support for Upper and Lower Case Letters: Handles both uppercase and lowercase letters while keeping non-alphabetic characters unchanged.
Interactive Command-Line Interface: User-friendly CLI for easy interaction.


#Run the Program on Linux/MacOS
*python3 caesar.py

#Run the Program on Windows
Open Command Prompt.
Navigate to the project directory

*cd path\to\caesar



#Run the program
*python caesar.py


#Usage
Once the program is running, you will be prompted to choose between encryption and decryption, and to input the message and your key stream (shift value). The program will then display the transformed message

Enter 'e' for encryption or 'd' for decryption: e
Enter your message: Hello, World!
Enter the shift value: 3
Encrypted message: Khoor, Zruog!


#Implementation Details

#Language: Python
#Algorithm: The Caesar Cipher shifts each letter in the plaintext by a fixed number of positions determined by the shift value or a key. The shift wraps around the end of the English alphabet.
#Modular Arithmetic: Utilizes modular arithmetic to handle wrap-around cases for the end of the alphabet.

