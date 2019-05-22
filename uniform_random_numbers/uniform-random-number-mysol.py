"""Rejection Sampling Algorithm

 Time Complexity: O(log(b - a + 1))
Space Complexity: O(1)
"""

import random

class Solution:
    def zero_one_random(self):
        return random.randrange(2)

    def uniform_random(self, lower_bound, upper_bound):
        p = upper_bound - lower_bound + 1
        while True:
            x = random.randrange(p)
            y = self.zero_one_random()
            if y < p:
                break
        return x
    
def main():
    s = Solution()
    test_cases = [
        (1, 6),
        (1, 2),
        (0, 10)
        ]
    for num in test_cases:
        for i in range(3):
            random_num = s.uniform_random(num[0], num[1])
            print(f'[{num[0]},{num[1]}] -> {random_num}')

if __name__ == '__main__':
    main()