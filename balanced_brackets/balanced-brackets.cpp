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
            if (opening == '[' && closing == ']') return true;
            if (opening == '(' && closing == ')') return true;
            if (opening == '{' && closing == '}') return true;
            else return false;
        }

        bool is_balanced(std::string expression) {
            std::string str = expression;
            std::stack<char> stack;

            for (int i = 0; i < str.length(); i++) {
                if (str[i] == '[' || str[i] == '(' || str[i] == '{') {
                    stack.push(str[i]);
                }
                else if (str[i] == ']' || str[i] == ')' || str[i] == '}') {
                    if (stack.empty()) return false;
                    else if (is_pair(stack.top(), str[i])) stack.pop();
                    else return false;
                }
            }
            
            return stack.empty();
        }
};

int main(void) {
    Solution s;
    std::string expression;

    std::cout << "Enter expression: ";
    std::cin >> expression;
    std::cout << std::boolalpha << s.is_balanced(expression);

    return 0;
}