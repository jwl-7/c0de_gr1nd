#====================================================================
#=                          CAESAR CIPHER                           =                    
#====================================================================

# Problem: Write a program that decrypts ciphertext that has been encrypted
#          using the Caesar Cipher. Find the plaintext and the shift key.

import enchant

class Solution:
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

    def check_word(self, string):
        d = enchant.Dict('en_US')
        return d.check(string)

    def decrypt(self):
        #ciphertext = str.upper(input('Enter ciphertext: '))
        ciphertext = str.upper('OTWEWNGWCBPQABIZVQAPMLJGZWTTQVOBQUMAPMIDGZCAB')
        top_letters = self.check_frequency(ciphertext)

        print('Top Four Letters')
        print('-----------------')
        for item in top_letters:
            print(str.upper(item[0]), ' : ', item[1])
        

def main():
    s = Solution()
    s.decrypt()

if __name__ == "__main__":
    main()