#!/usr/bin/env python3
import itertools


def main():
    travels = {}
    trips = set()
    shortest_trip = None
    longest_trip = None
    trip_entries = get_input_file('day_9_input.txt')
    for t in trip_entries:
        start, _, end, _, distance = t.split(" ")
        travels[(start, end)] = int(distance)
        travels[(end, start)] = int(distance)
        trips.update([start, end])

    for t in itertools.permutations(trips):
        stops = list(t)
        trip_distance = sum(travels[(stops[i], stops[i+1])]
                            for i in range(len(stops)-1))

        if not shortest_trip:
            shortest_trip = trip_distance

        if not longest_trip:
            longest_trip = trip_distance

        if trip_distance < shortest_trip:
            shortest_trip = trip_distance

        if trip_distance > longest_trip:
            longest_trip = trip_distance

    print("Shortest trip {0}".format(shortest_trip))
    print("Longest trip {0}".format(longest_trip))


def get_input_file(input_file):
    with open(input_file, 'r') as f:
        read_data = f.readlines()

    f.closed

    return read_data

main()
