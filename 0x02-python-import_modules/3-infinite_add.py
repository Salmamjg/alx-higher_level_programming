#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    # Skip the script name, convert arguments to integers, and sum them
    result = sum(int(arg) for arg in argv[1:])

    # Print the result
    print(result)
