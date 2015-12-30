#!/usr/bin/env python3


def main():
    input = '1113222113'
    input = '1113222113'
    # my_output = '3113322113'
    # input = '11'  # output 21
    # input = '21'  # ouput 1211
    # input = '1211' # output 111221

    for i in range(40):
        input = loop_it(input)

    print(len(input))


def loop_it(input):
    count = 0
    marker = None
    output = []

    for x in input:
        if not marker:
            marker = x

        if marker != x:
            output.append(str(count))
            output.append(marker)
            marker = x
            count = 1
        else:
            count += 1

    output.append(str(count))
    output.append(marker)

    return(''.join(output))

main()
