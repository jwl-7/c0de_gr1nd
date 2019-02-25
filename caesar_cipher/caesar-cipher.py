#====================================================================
#=                          CAESAR CIPHER                           =                    
#====================================================================

class Cipher:
    def check_frequency(self, string):
        char_freq = {}

        for char in string:
            freq = char_freq.keys()
            if char in freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
        char_freq = sorted(char_freq.items(), key = lambda x: x[1], reverse = True)

        return char_freq[:4]
    
    def decrypt(self, string, key):
        decrypted = ''
        key =- key

        for char in string:
            num = ord(char)
            num += key

            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
            decrypted += chr(num)

        return decrypted

    def display(self):
        #ciphertext = str.upper(input('Enter ciphertext: '))
        ciphertext = str.upper('OTWEWNGWCBPQABIZVQAPMLJGZWTTQVOBQUMAPMIDGZCABEQVBMZLZIXMLAXZQVOQVLMMXAVWEIVLLIZSNZWABJQZLWNLMTQOPBVIUMLGWCBPAEQNBTGTMNBBPMVMABITIAKWCTLVBBQUMQBEPQTMQBEIAQVUGBZCAB')
        top_letters = self.check_frequency(ciphertext)

        p_keys = []

        print('Top Four Letters')
        print('-------------------')
        for item in top_letters:
            print(item[0], ' : ', item[1])

            num = ord(item[0]) - 65
            a = (num - 4) % 26
            b = (4 - num) % 26
            num = min(a, b)
            p_keys.append(num)

        print('\nPossible Shift Keys: ' + str(p_keys))
        print('\nPossible Translations')
        print('-----------------------')

        for key in p_keys:
            p_msg = self.decrypt(ciphertext, key)
            print(key)
            print(p_msg + '\n')

def main():
    c = Cipher()
    c.display()

if __name__ == "__main__":
    main()