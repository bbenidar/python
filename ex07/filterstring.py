import sys


def main() -> None:
    """a program accepts two arguments: a string (S) and an integer (N).
    and output a list of words from S that have a length greater than N"""
    try:
        len_arg = len(sys.argv)
        if len_arg != 3:
            raise AssertionError("the arguments are bad")

        try:
            min_l = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        if not all(c.isalnum() or c == " " for c in sys.argv[1]):
            raise AssertionError("the arguments are bad")

        lst = [word for word in sys.argv[1].split(" ") if word]

        result = list(filter(lambda word: len(word) > min_l, lst))
        print(result)

    except KeyboardInterrupt:
        return
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
