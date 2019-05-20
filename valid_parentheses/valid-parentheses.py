"""Valid Parenthesis

Time Complexity: O(n)
Space Complexity: O(n)
"""

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