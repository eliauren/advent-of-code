#!/usr/bin/env python
INPUT_FILE_PATH = 'input.txt'


def main():
    file = open(INPUT_FILE_PATH, 'r')
    lines = file.readlines()

    total = 0

    for line in lines:
        digits = []
        for d in line:
            if d.isdigit():
                digits.append(d)

        total += int(digits[0]+digits[-1])

    print(total)


if __name__ == '__main__':
    main()
