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
                last = stack[-1]
                if stack and last in brackets and brackets[last] == char:
                    stack.pop()
        print(stack)
        if not stack:
            return True
        else:
            return False
    
def main():
    s = Solution()

    #print('Enter expression: ')
    #statement = input()
    expression = 'test() 123[]'
    print(s.is_balanced(expression))

main()