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
                print("push char: " + char)
                print("brackets[char] = " + brackets[char])
                match = brackets[char]
                stack.append(char)
                peek = stack[-1]
            elif not stack and char in closing:
                return False
            if stack and peek in brackets and brackets[peek] == char:
                    print("peek = " + peek)
                    print("brackets[peek] " + brackets[peek])
                    stack.pop()
        return False
    
def main():
    s = Solution()

    #print('Enter expression: ')
    #statement = input()
    expression = 'test() 123[]'
    print(s.is_balanced(expression))

main()