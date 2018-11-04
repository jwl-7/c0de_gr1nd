#=====================
#= Balanced Brackets =
#=====================

class Solution:
    def balanced_brackets(self, expression):
        opening = tuple('[({')
        closing = tuple('])}')
        brackets = dict(zip(opening, closing))
        stack = []

        for char in expression:
            if char in opening:
                stack.append(char)
            elif stack and char in closing:
                stack.pop()
        print(stack)
        if not stack:
            print('> BALANCED')
        else:
            print('> NOT BALANCED')
    
def main():
    sol = Solution()
    print('Enter expression: ')
    statement = input()
    sol.balanced_brackets(statement)

main()

#