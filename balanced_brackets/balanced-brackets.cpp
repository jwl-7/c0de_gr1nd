//=====================
//= Balanced Brackets =
//=====================

// Problem: Given an expression string, determine whether or not
//          each sequence of '[](){}' is balanced.
// Runtime: O(n)

#include <iostream>
#include <stack>
#include <string>

class Solution {
    public: 
        bool is_pair(char opening, char closing) {
            if (opening == '[' && closing == ']')
                return true;
            else if (opening == '(' && closing == ')')
                return true;
            else if (opening == '{' && closing == '}')
                return true;
            else
                return false;
        }

        bool is_balanced(std::string expression) {
            std::string str = expression;

            for (int i = 0; i < str.length(); i++) {
                
            }
        }
};

int main(void) {
    //Solution s;
    std::string test1 = "()[]{}";    // true
    std::string test2 = "{([])}";    // true
    std::string test3 = "()[";       // false

    return 0;
}