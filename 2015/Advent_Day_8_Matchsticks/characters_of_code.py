#!/usr/bin/env python3
import re


def main():
    inputs = get_input_file()
    total = 0
    partb_total = 0
    for line in inputs:
        line = line.rstrip("\n")
        total += difference(line)
        partb_total += encode_all_the_things(line)

    print("part a:{0}\npart b:{1}".format(total, partb_total))


def difference(line):
    # print("{0}:{1}\t{2}:{3}".format(
    #    line, len(line), eval(line), len(eval(line))))
    return len(line) - len(eval(line))


def encode_all_the_things(line):
    # line = line.startswith(
    # encoded_line = "\"" + re.escape(line) + "\""
    # print("{0} -- {1}".format(line,encoded_line ))
    return len("\"" + re.escape(line) + "\"") - len(line)


def get_input_file():
    with open('./day_8_input.txt', 'r') as f:
        read_data = f.readlines()

    f.closed
    return read_data

main()
