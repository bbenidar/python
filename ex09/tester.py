"""Demonstrate count_in_list from the installed ft_package."""

import sys


def main() -> None:
    """Run the exercise examples and report failures."""
    try:
        from ft_package import count_in_list

        print(count_in_list(["toto", "tata", "toto"], "toto"))
        print(count_in_list(["toto", "tata", "toto"], "tutu"))
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as error:
        print(f"{type(error).__name__}: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
