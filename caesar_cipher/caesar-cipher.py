#====================================================================
#=                          CAESAR CIPHER                           =                    
#====================================================================

# Problem: Write a program that decrypts ciphertext that has been encrypted
#          using the Caesar Cipher. Find the plaintext and the shift key.
import enchant

class Solution:
    def cipher_key(self, string):
        alphabet = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        alphabet_numbers = []
        char_frequency = {}

        for char in string:
            keys = char_frequency.keys()

            if char in keys:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

        
    def detect_word(self):
        d = enchant.Dict('en_US')

    def decrypt(self):
        ciphertext = input('Enter ciphertext: ')

def main():
    s = Solution()

if __name__ == "__main__":
    main()