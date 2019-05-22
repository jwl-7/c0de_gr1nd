"""Rejection Sampling Algorithm

 Time Complexity: O(log(b - a + 1))
Space Complexity: O(1)
"""

import random

class Solution:
    def zero_one_random(self):
        return random.randrange(2)

    def uniform_random(self, lower_bound, upper_bound):
        number_of_outcomes = upper_bound - lower_bound + 1
        while True:
            result, i = 0, 0
            while (1 << i) < number_of_outcomes:
                # zero_one_random() is the provided random number generator.
                result = (result << 1) | self.zero_one_random()
                i += 1
            if result < number_of_outcomes:
                break
        return result + lower_bound
    
def main():
    s = Solution()
    test_cases = [
        (1, 6),
        (0, 3),
        (1, 10)
        ]
    for num in test_cases:
        for i in range(3):
            random_num = s.uniform_random(num[0], num[1])
            print(f'[{num[0]},{num[1]}] -> {random_num}')

if __name__ == '__main__':
    main()