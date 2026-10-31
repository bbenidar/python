
import sys



def main() -> None:
    """takes a single string argument and displays the sums of its upper-case characters, lower-case characters, punctuation characters, digits, and spaces."""
    try:
        print (main.__doc__)
        len_arg = len(sys.argv)

        if len_arg > 2:
            raise AssertionError("more than one argument is provided")
        __str = ""
        if len_arg == 2:
            __str = sys.argv[1]
        if  __str == "":
            print("What is the text to count?")
            __str = sys.stdin.readline()
        """Print the text length and counts for five character categories."""
        up = 0
        lw = 0
        p_mark = 0
        sp = 0
        nu = 0
        pn = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        for c in __str:
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
        print(f"The text contains {len(__str)} characters:")
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