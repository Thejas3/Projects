def handle_exceptions():
    try:
        # TypeError
        x = 5 + "10"
    except TypeError as e:
        print("TypeError occurred:", e)

    try:
        # ValueError
        num = int("hello")
    except ValueError as e:
        print("ValueError occurred:", e)

    try:
        # KeyError
        my_dict = {"a": 1, "b": 2}
        value = my_dict["c"]
    except KeyError as e:
        print("KeyError occurred:", e)

    try:
        # AttributeError
        class MyClass:
            def __init__(self):
                self.x = 5

        obj = MyClass()
        print(obj.y)
    except AttributeError as e:
        print("AttributeError occurred:", e)

    try:
        # RecursionError
        def infinite_recursion():
            return infinite_recursion()

        infinite_recursion()
    except RecursionError as e:
        print("RecursionError occurred:", e)


if __name__ == "__main__":
    handle_exceptions()
