import time


def main() -> None:
    seconds = time.time()
    print(
        f"Seconds since January 1, 1970: {seconds:,.4f} or "
        f"{seconds:.2e} in scientific notation"
    )
    print(time.strftime("%b %d %Y", time.localtime(seconds)))


if __name__ == "__main__":
    main()
