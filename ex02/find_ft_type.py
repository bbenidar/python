from typing import Any


def all_thing_is_obj(object: Any) -> int:
    object_t = type(object)
    if object_t is list:
        print(f"List : {object_t}")
    elif object_t is tuple:
        print(f"Tuple : {object_t}")
    elif object_t is set:
        print(f"Set : {object_t}")
    elif object_t is dict:
        print(f"Dict : {object_t}")
    elif object_t is str:
        print(f"{object} is in the kitchen : {object_t}")
    else:
        print("Type not found")
    return 42
