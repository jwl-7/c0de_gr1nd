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

        }
};

int main(void) {
    Solution s;

    return 0;
}