#####################
#     Fizz Buzz     #
#####################

# This program prints each number from 1 to 100 on a new line.
# For each multiple of 3, it prints 'Fizz' instead of the number.
# For each multiple of 5, it prints 'Buzz' instead of the number.
# For numbers which are multiples of both 3 and 5, it prints 'FizzBuzz' instead of the number.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i% 5 == 0:
        print('Buzz')
    else:
        print(i)