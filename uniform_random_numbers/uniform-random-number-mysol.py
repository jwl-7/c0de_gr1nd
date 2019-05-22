"""[FILL IN] Algorithm

Time Complexity: [FILL IN]
"""

import random

class Solution:
    def zero_one_random(self):
        return random.randrange(2)

    def uniform_random(self, lower_bound, upper_bound):
        # TODO - you fill in here.
        return 0
    
def main():
    s = Solution()
    test_cases = [
        (1, 6),
        (1, 6),
        (1, 6),
        (0, 3),
        (0, 3),
        (0, 3),
        (1, 10),
        (1, 10),
        (1, 10)
        ]
    for num in test_cases:
        random_num = s.uniform_random(num[0], num[1])
        print(f'[{num[0]},{num[1]}] -> {random_num}')

if __name__ == '__main__':
    main()