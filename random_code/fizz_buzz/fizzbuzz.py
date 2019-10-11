class Solution:
    def fizzy(self, n):
        list = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                list.append('FizzBuzz')
            elif i % 3 == 0:
                list.append('Fizz')
            elif i % 5 == 0:
                list.append('Buzz')
            else:
                list.append(str(i))
        return '\n'.join(list)


def main():
    s = Solution()
    print(s.fizzy(100))


if __name__ == '__main__':
    main()
