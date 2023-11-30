#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_arguments = len(argv) - 1
    arg_list = argv[1:]

    print("{} argument{}{}"
          .format(num_arguments, 's'
                  if num_arguments != 1 else '', ''
                  if num_arguments == 0 else ':'))

    for i in range(1, num_arguments):
        print("{:d}: {}".format(i, argv[i]))
