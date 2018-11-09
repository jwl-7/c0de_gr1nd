//====================================================================
//=                            FIZZ BUZZ                             =                    
//====================================================================

// Problem: Write a program that outputs the string representation of numbers from 1 to n.
//          For each multiple of 3, print 'Fizz' instead of the number. 
//          For each multiple of 5, print 'Buzz' instead of the number. 
//          For numbers which are multiples of both 3 and 5, print 'FizzBuzz' instead of the number.
//
//  Time Complexity: O(n)
// Space Complexity: O(1)

#include <iostream>
#include <string>
#include <vector>

class Solution {
    public:
        std::vector<std::string> fizzy(int n) {
            std::vector<std::string> result;
            for (int i = 1; i <= n; i++) {
                if (i % 15 == 0) result.push_back("FizzBuzz");
                else if (i % 3 == 0) result.push_back("Fizz");
                else if (i % 5 == 0) result.push_back("Buzz");
                else result.push_back(std::to_string(i));
            }
            return result;    
        }

        void print(std::vector<std::string> const &input) {
            for (int i = 0; i < input.size(); i++) {
                std::cout << input.at(i) << '\n';
            }
        }
};

int main() {
    Solution s;
    s.print(s.fizzy(100));
}