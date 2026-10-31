def ft_filter(function, iterable):
    (
        "Return an iterator yielding those items of iterable for which\n"
        "function(item) is true.  If function is None, return the items that\n"
        "are true."
    )
    if function is None:
        function = bool

    for item in iterable:
        if function(item):
            yield item


def main() -> None:
    """Provide the required entry point for this importable module."""
    pass


if __name__ == "__main__":
    main()
