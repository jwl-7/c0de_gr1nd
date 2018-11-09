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
    def is_balanced(self, expression):
        opening = tuple('[({')
        closing = tuple('])}')
        brackets = dict(zip(opening, closing))
        stack = []

        for char in expression:
            if char in opening:
                stack.append(char)
            elif not stack and char in closing:
                return False     
            elif stack:
                peek = stack[-1]
                if char in closing and char == brackets[peek]:
                    stack.pop()
        return not stack
    
def main():
    s = Solution()
    print('Enter expression:')
    expression = input()
    print(s.is_balanced(expression))

main()