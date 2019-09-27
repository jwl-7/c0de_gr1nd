from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    keypad = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ',
    }
    mnemonics = ['']
    for num in phone_number:
        letters = keypad.get(num, num)
        mnemonics = [x+letter for x in mnemonics for letter in letters]
    return mnemonics


def phone_mnemonic_recursive(phone_number):
    keypad = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ',
    }
    
    def build_mnemonic(num):
        if num == len(phone_number):
            mnemonics.append(''.join(curr))
        else:
            letters = keypad.get(phone_number[num], phone_number[num])
            for letter in letters:
                curr[num] = letter
                build_mnemonic(num + 1)

    mnemonics = []
    curr = [0] * len(phone_number)
    build_mnemonic(0)
    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic_recursive,
            comparator=test_utils.unordered_compare))
