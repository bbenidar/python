"""A sample test package with a list occurrence counter."""


def count_in_list(items: list, value: object) -> int:
    """Return the number of elements in items that compare equal to value."""
    count = 0
    for item in items:
        if item == value:
            count += 1
    return count
