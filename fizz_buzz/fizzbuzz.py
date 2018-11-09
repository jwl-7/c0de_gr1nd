#====================================================================
#=                            FIZZ BUZZ                             =                    
#====================================================================

# Problem: Write a program that outputs the string representation of numbers from 1 to n. 
#          For each multiple of 3, print 'Fizz' instead of the number. 
#          For each multiple of 5, print 'Buzz' instead of the number. 
#          For numbers which are multiples of both 3 and 5, print 'FizzBuzz' instead of the number.
#
#  Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def fizzy(self):
        for i in range(1, 101):
            if i % 15 == 0: print('FizzBuzz')
            elif i % 3 == 0: print('Fizz')
            elif i % 5 == 0: print('Buzz')
            else: print(i)

def main():
    s = Solution()
    s.fizzy()

if __name__ == "__main__":
    main()