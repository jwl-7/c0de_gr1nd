#====================================================================
#=                          CAESAR CIPHER                           =                    
#====================================================================

# Problem: Write a program that decrypts ciphertext that has been encrypted
#          using the Caesar Cipher. Find the plaintext and the shift key.

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
        ciphertext = str.upper('OTWEWNGWCBPQABIZVQAPMLJGZWTTQVOBQUMAPMIDGZCAB')
        top_letters = self.check_frequency(ciphertext)

        p_keys = []

        print('Top Four Letters')
        print('-----------------')
        for item in top_letters:
            print(str.upper(item[0]), ' : ', item[1])

            num = ord(item[0])
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
            print(ord(item[0]))


            
        
        print(self.decrypt(ciphertext, 8))

def main():
    s = Solution()
    s.display()

if __name__ == "__main__":
    main()