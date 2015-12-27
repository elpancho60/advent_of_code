#!/usr/bin/env python3


def main():
    inputs = get_input_file()
    total = 0
    for line in inputs:
        total += difference(line.rstrip("\n"))

    print(total)


def difference(line):
    # print("{0}:{1}\t{2}:{3}".format(
    #    line, len(line), eval(line), len(eval(line))))
    return len(line) - len(eval(line))


def get_input_file():
    with open('./day_8_input.txt', 'r') as f:
        read_data = f.readlines()

    f.closed
    return read_data

main()
