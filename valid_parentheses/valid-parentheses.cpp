//====================================================================
//=                        Valid Parentheses                         =
//====================================================================

// Problem: Given a string containing just the characters 
//          '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
//
//          An input string is valid if:
//              Open brackets must be closed by the same type of brackets.
//              Open brackets must be closed in the correct order.
//
//          Note that an empty string is also considered valid.
//
//  Time Complexity: O(n)
// Space Complexity: O(n)

#include <iostream>
#include <stack>
#include <string>

class Solution {
    public: 
        bool is_pair(char open, char close) {
            if (open == '[' && close == ']') return true;
            if (open == '(' && close == ')') return true;
            if (open == '{' && close == '}') return true;
            else return false;
        }

        bool is_balanced(std::string str) {
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

int main() {
    Solution s;
    std::string str;

    std::cout << "Enter string: ";
    std::cin >> str;
    std::cout << std::boolalpha << s.is_balanced(str) << '\n';
}