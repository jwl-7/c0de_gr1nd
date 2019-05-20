"""Brute-Force Algorithm

Time Complexity: O(n), where n is the integer width
"""

class Solution:
    def closest(self, x):
        return x
        
def main():
    s = Solution()
    test_cases = [
        92,
        55,
        69,
        74
        ]
    for num in test_cases:
        closest_int = s.closest(num)
        print(f'{num} -> {closest_int}')

if __name__ == '__main__':
    main()