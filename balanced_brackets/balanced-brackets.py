#=====================
#= Balanced Brackets =
#=====================

# Problem: Given an expression string, determine whether or not
#          each sequence of '[](){}' is balanced.
#
# Time Complexity = 

class Solution:
    def balanced_brackets(self, expression):
        opening = tuple('[({')
        closing = tuple('])}')
        brackets = dict(zip(opening, closing))
        stack = []

        for char in expression:
            if char in opening:
                stack.append(char)
            #elif stack and char in closing:
                #stack.pop()
        print(stack)
        if not stack:
            print('> BALANCED')
        else:
            print('> NOT BALANCED')
    
def main():
    sol = Solution()

    #print('Enter expression: ')
    #statement = input()
    expression = 'test() 123[]}'
    sol.balanced_brackets(expression)

main()