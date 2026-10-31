def main() -> None:
    """Modify the supplied collections to display the campus greetings."""
    ft_list = ["Hello"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    ft_list.append("World!")
    ft_tuple = ft_tuple[:1] + ("Morocco!",)
    ft_set.remove("tutu!")
    ft_set.add("Khouribga!")
    ft_dict["Hello"] = "1337Khouribga!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()
