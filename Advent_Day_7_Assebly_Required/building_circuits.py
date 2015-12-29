#!/usr/bin/env python3

gates = {}


def main():
    instructions = get_input_file()
    break_it_up(instructions)
    gates["b"] = 956  # answer from 1
    print(signal("a"))


def signal(wire):
    if isinstance(wire, int) or wire.isdigit():
        return int(wire)

    ops = wire.split(" ")

    if len(ops) == 1:
        gates[wire] = signal(gates[ops[0]])
        return gates[wire]

    elif len(ops) == 2:
        return ~signal(ops[1])

    elif len(ops) == 3:
        if ops[1] == "AND":
            return signal(ops[0]) & signal(ops[2])
        elif ops[1] == "OR":
            return signal(ops[0]) | signal(ops[2])
        elif ops[1] == "RSHIFT":
            return signal(ops[0]) >> signal(ops[2])
        elif ops[1] == "LSHIFT":
            return signal(ops[0]) << signal(ops[2])


def break_it_up(circuit):
    for instruction in circuit:
        instruction = instruction.strip()
        signal, wire = instruction.split(' -> ')
        gates[wire] = signal


def get_input_file():
    with open('./day_7_input.txt', 'r') as f:
        read_data = f.readlines()

    f.closed
    return read_data

main()
