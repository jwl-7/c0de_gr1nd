/////////////////////
//    Fizz Buzz    //
/////////////////////

// This program prints each number from 1 to 100 on a new line.
// For each multiple of 3, it prints "Fizz" instead of the number.
// For each multiple of 5, it prints "Buzz" instead of the number.
// For numbers which are multiples of both 3 and 5, it prints "FizzBuzz" instead of the number.

#include <iostream>

void fizzy() {
    for (int i = 1; i <= 100; i++) {
        if (i % 15 == 0) std::cout << "FizzBuzz\n";
        else if (i % 3 == 0) std::cout << "Fizz\n";
        else if (i % 5 == 0) std::cout << "Buzz\n";
        else std::cout << i << "\n";
    }    
}

int main(void) {
    fizzy();
}