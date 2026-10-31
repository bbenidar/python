import sys

try:
    len_arg = len(sys.argv)

    if len_arg > 2:
        raise AssertionError("more than one argument is provided")
    if len_arg == 2:
        try:
            num = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    
except AssertionError as error:
    print(f"AssertionError: {error}")