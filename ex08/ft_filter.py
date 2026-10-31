def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        function = bool

    for item in iterable:
        if function(item):
            yield item


def main() -> None:
    """Quick test of ft_filter."""
    print(list(ft_filter(lambda x: x % 2 == 0, range(10))))


if __name__ == "__main__":
    main()
