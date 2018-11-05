#=====================
#= Balanced Brackets =
#=====================

# Problem: Given an expression string, determine whether or not
#          each sequence of '[](){}' is balanced.
# Runtime: O(n)

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

    #print('Enter expression: ')
    #expression = input()
    #print(s.is_balanced(expression))
    print(s.is_balanced('(([])){[()][]}'))
    print(s.is_balanced('())[]{}'))
    print(s.is_balanced('[(])'))

main()