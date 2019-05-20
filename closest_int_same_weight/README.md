# Closest Integer with the Same Weight

"Define the weight of a nonnegative integer x to be the number of bits that are set to 1 in its binary representation. For example, since 92 in base-2 equals (1011100)<sub>2</sub>, the weight of 92 is 4." - EPI  
  
Problem:  
Write a program which takes as input a nonnegative integer x and returns a number y which is not equal to x, but has the same weight as x and their difference, |y - x|, is as small as possible. You can assume x is not 0, or all 1s. For example, if x = 6, you should return 5. You can assume the integer fits in 64 bits.  
  
Example:    
```
74 in binary = 1001010
The weight of 74 is 3.

The closest integer would be 73.
73 in binary = 1001001
The weight of 73 is also 3.
```