#====================================================================
#=                          CAESAR CIPHER                           =                    
#====================================================================

# This program allows you to encrypt / decrypt ciphertexts using the Caesar cipher.
# Plaintext is encrypted using shifts to the right.
# Ciphertext is decrypted using either basic frequency analysis or brute force.

class Cipher:
    def prompt(self):
        """Displays information about program and asks user to pick mode."""

        print('Caesar Cipher')
        print('---------------------------------------------------------------')
        print('1 - Encrypt plaintext -> ciphertext')
        print('2 - Decrypt ciphertext -> plaintext using frequency analysis')
        print('3 - Decrypt ciphertext -> plaintext using brute force\n')

        while True:
            try:
                mode = int(input('Pick a mode [1-3]: '))
                if mode < 1 or mode > 3:
                    raise ValueError
                break
            except ValueError:
                print('[ERROR] INVALID INPUT!')

        return mode
    
    def transcipher(self, mode, msg, key):
        """Shifts each letter in the ciphertext n positions to the right."""

        translation = ''

        if mode == 2 or mode == 3:
            key =- key

        for char in msg:
            if char.isalpha():
                num = ord(char)
                num += key

                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

                translation += chr(num)
            else:
                translation += char

        return translation

    def find_frequency(self, msg):
        """Finds the top four most frequently used letters in the ciphertext."""

        char_freq = {}

        for char in msg:
            freq = char_freq.keys()
            if char in freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
        char_freq = sorted(char_freq.items(), key = lambda x: x[1], reverse = True)

        return char_freq[:4]

    def cipher_key(self, msg, top_char):
        """Finds possible cipher keys using most frequently used letters."""

        p_keys = []

        for char in top_char:
            num = ord(char[0]) - 65
            a = (num - 4) % 26
            b = (4 - num) % 26
            num = min(a, b)
            p_keys.append(num)

        return p_keys


    def cipher_run(self):
        """Runs the Caesar cipher decryption / frequency analysis."""

        cipher_mode = self.prompt()

        if cipher_mode == 1:
            ciphertext = str.upper(input('Enter plaintext: '))
        elif cipher_mode == 2:
            ciphertext = str.upper(input('Enter ciphertext: '))
            top_letters = self.find_frequency(ciphertext)
            possible_keys = self.cipher_key(ciphertext, top_letters)

            print('Top Four Letters')
            print('-------------------')
            for item in top_letters:
                print(f'{item[0]} : {item[1]}')

            print(f'\nPossible Shift Keys: {possible_keys}')

            print('\nPossible Translations')
            print('-----------------------')
            for key in possible_keys:
                p_msg = self.decrypt(ciphertext, key)
                print(f'[{key}] {p_msg} \n')
        elif cipher_mode == 3:
            ciphertext = str.upper(input('Enter ciphertext: '))

def main():
    c = Cipher()
    c.cipher_run()

if __name__ == "__main__":
    main()