#====================================================================
#=                        Valid Parentheses                         =
#====================================================================

# Problem: Given a string containing just the characters 
#          '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#          An input string is valid if:
#              Open brackets must be closed by the same type of brackets.
#              Open brackets must be closed in the correct order.
#
#          Note that an empty string is also considered valid.
#
#  Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def is_balanced(self, string):
        open = tuple('[({')
        close = tuple('])}')
        brackets = dict(zip(open, close))
        stack = []

        for char in string:
            if char in open:
                stack.append(char)
            elif not stack and char in close:
                return False     
            elif stack:
                peek = stack[-1]
                if char in close and char == brackets[peek]:
                    stack.pop()
        return not stack
    
def main():
    s = Solution()
    string = input('Enter string: ')
    print(s.is_balanced(string))

if __name__ == "__main__":
    main()