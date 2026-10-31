import sys


def main() -> None:
    """encode one string argument as morse code"""
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    try:
        len_arg = len(sys.argv)
        if len_arg != 2:
            raise AssertionError("the arguments are bad")

        __result = []

        for c in sys.argv[1]:
            c = c.upper()
            if c not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
            __result.append(NESTED_MORSE[c])
        print(" ".join(__result))
    except Exception as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
