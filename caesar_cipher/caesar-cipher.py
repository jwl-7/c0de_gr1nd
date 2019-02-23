#====================================================================
#=                          CAESAR CIPHER                           =                    
#====================================================================

# Problem: Write a program that decrypts ciphertext that has been encrypted
#          using the Caesar Cipher. Find the plaintext and the shift key.
import enchant

class Solution:
    def check_frequency(self, string):
        alphabet = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        alphabet_nums = []
        char_freq = {}

        for char in string:
            keys = char_freq.keys()

            if char in keys:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        sorted_char_freq = sorted(char_freq.items(), key = lambda x: x[1], reverse = True)

        return sorted_char_freq[:4]

    def cipher_key(self, string):
        sdalphabet = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  
    def detect_word(self):
        d = enchant.Dict('en_US')

    def decrypt(self):
        ciphertext = input('Enter ciphertext: ')
        top_letters = self.check_frequency(ciphertext)

        print('Top Four Letters')
        print('-----------------')
        for item in top_letters:
            print(item[0], ' : ', item[1])

def main():
    s = Solution()
    s.decrypt()

if __name__ == "__main__":
    main()