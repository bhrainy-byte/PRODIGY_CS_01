import string

# ANSI color codes
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


class CaesarCipher:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.alphabet_upper = string.ascii_uppercase

    def _create_cipher_map(self, key, mode):
        if mode == 'decrypt':
            key = -key

        shifted_alphabet = self.alphabet[key:] + self.alphabet[:key]
        shifted_alphabet_upper = self.alphabet_upper[key:] + self.alphabet_upper[:key]

        cipher_map = str.maketrans(
            self.alphabet + self.alphabet_upper,
            shifted_alphabet + shifted_alphabet_upper
        )
        return cipher_map

    def encrypt(self, plaintext, shift):
        cipher_map = self._create_cipher_map(shift, 'encrypt')
        return plaintext.translate(cipher_map)

    def decrypt(self, ciphertext, shift):
        cipher_map = self._create_cipher_map(shift, 'decrypt')
        return ciphertext.translate(cipher_map)


def get_shift_value():
    while True:
        try:
            shift = int(input("Enter the key value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 1 and 25. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 25.")


def main():
    cipher = CaesarCipher()

    while True:
        mode = input(
            f"Enter {GREEN}'e'{RESET} {BLUE}for{RESET} {RED}encrypt{RESET}, {GREEN}'d'{RESET} {BLUE}for{RESET} {RED}decrypt{RESET}, or 'q' to quit: ").lower()

        if mode == 'q':
            print("Goodbye!")
            break

        if mode not in ['e', 'd']:
            print("Invalid mode. Please try again.")
            continue

        text = input("Enter the message: ")
        shift = get_shift_value()

        if mode == 'e':
            result = cipher.encrypt(text, shift)
            print(f"{RED}Encrypted{RESET} message: {YELLOW}{result}{RESET}")
        else:
            result = cipher.decrypt(text, shift)
            print(f"{RED}Decrypted{RESET} message: {YELLOW}{result}{RESET}")


if __name__ == "__main__":
    main()
