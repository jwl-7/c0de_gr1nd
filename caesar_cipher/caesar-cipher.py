#====================================================================
#=                          CAESAR CIPHER                           =                    
#====================================================================

class Cipher:
    def check_frequency(self, msg):
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
    
    def decrypt(self, msg, key):
        """Shifts each letter in the ciphertext n positions to the right."""

        decrypted = ''
        key =- key

        for char in msg:
            num = ord(char)
            num += key

            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
            decrypted += chr(num)

        return decrypted

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


    def display(self):
        """Runs the Caesar cipher decryption / frequency analysis."""

        ciphertext = str.upper(input('Enter ciphertext: '))
        top_letters = self.check_frequency(ciphertext)
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

def main():
    c = Cipher()
    c.display()

if __name__ == "__main__":
    main()