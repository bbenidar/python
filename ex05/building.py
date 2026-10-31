import sys


def main() -> None:
    """Count upper, lower, punctuation, space and digit characters
    in the given string."""
    try:
        len_arg = len(sys.argv)

        if len_arg > 2:
            raise AssertionError("more than one argument is provided")
        text = ""
        if len_arg == 2:
            text = sys.argv[1]
        if text == "":
            print("What is the text to count?")
            text = sys.stdin.readline()
        up = 0
        lw = 0
        p_mark = 0
        sp = 0
        nu = 0
        pn = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        for c in text:
            if c.isupper():
                up += 1
            elif c.islower():
                lw += 1
            elif c in pn:
                p_mark += 1
            elif c.isdigit():
                nu += 1
            elif c.isspace():
                sp += 1
        print(f"The text contains {len(text)} characters:")
        print(f"{up} upper letters")
        print(f"{lw} lower letters")
        print(f"{p_mark} punctuation marks")
        print(f"{sp} spaces")
        print(f"{nu} digits")
    except KeyboardInterrupt:
        return
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
