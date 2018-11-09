//====================================================================
//=                            FIZZ BUZZ                             =                    
//====================================================================

// Problem: Write a program that outputs the string representation of numbers from 1 to n.
//          For each multiple of 3, print 'Fizz' instead of the number. 
//          For each multiple of 5, print 'Buzz' instead of the number. 
//          For numbers which are multiples of both 3 and 5, print 'FizzBuzz' instead of the number.
//
//  Time Complexity: O(n)
// Space Complexity: O(n)

#include <iostream>

class Solution {
    public:
        void fizzy() {
            for (int i = 1; i <= 100; i++) {
                if (i % 15 == 0) std::cout << "FizzBuzz\n";
                else if (i % 3 == 0) std::cout << "Fizz\n";
                else if (i % 5 == 0) std::cout << "Buzz\n";
                else std::cout << i << "\n";
            }    
        }
};

int main() {
    Solution s;
    s.fizzy();
}