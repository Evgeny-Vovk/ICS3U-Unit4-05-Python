# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: november 2022
# ICS3U-Unit4-05.py File, learning continue statement in python.


def main():

    # input and variables
    times_to_repeat = input("How many numbers do you want to add: ")
    counter = 0
    add_number = 0
    answer = 0

    # process and output
    print("")
    try:
        times_to_repeat_asint = int(times_to_repeat)
        while counter < times_to_repeat_asint:
            counter += 1
            add_number = int(input("Enter a number to add: "))
            if add_number < 0:
                continue
            answer += add_number
        if times_to_repeat_asint < 0:
            print("Please enter a positive number.")
        else:
            print("Sum of all the positive numbers is {0:,}.".format(answer))
    except ValueError:
        print("invalid input, the input does not fit the requirements.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
