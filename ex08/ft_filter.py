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



# def main() -> None:
#     """Demonstrate ft_filter and handle errors during iteration."""
#     try:
#         result = ft_filter(lambda x: x % 2 == 0, range(10))
#         print(list(result))
#     except KeyboardInterrupt:
#         return
#     except Exception as error:
#         print(f"{type(error).__name__}: {error}")


# if __name__ == "__main__":
#     main()