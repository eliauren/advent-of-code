#!/usr/bin/env python
INPUT_FILE_PATH = 'input.txt'
DIGIT_LETTERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def main():
    file = open(INPUT_FILE_PATH, 'r')
    lines = file.readlines()

    total = 0

    for line in lines:
        digits = []
        for i, d in enumerate(line):
            if d.isdigit():
                digits.append(d)

            for n, val in enumerate(DIGIT_LETTERS):
                if line[i:].startswith(val):
                    digits.append(str(n + 1))

        total += int(str(digits[0]+digits[-1]))
        print(digits)
    print(total)


if __name__ == '__main__':
    main()
