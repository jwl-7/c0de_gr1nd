/////////////////////
//    Fizz Buzz    //
/////////////////////

// This program prints each number from 1 to 100 on a new line.
// For each multiple of 3, it prints "Fizz" instead of the number.
// For each multiple of 5, it prints "Buzz" instead of the number.
// For numbers which are multiples of both 3 and 5, it prints "FizzBuzz" instead of the number.

#include <iostream>

int main(void) {
    int i;
    for (i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0)
            printf("FizzBuzz\n");
        else if (i % 3 == 0)
            printf("Fizz\n");
        else if (i % 5 == 0)
            printf("Buzz\n");
        else
            printf("%d\n", i);
    }

    return 0;
}