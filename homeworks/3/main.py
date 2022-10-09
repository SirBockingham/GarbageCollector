def divide(a, b):
    try:
        print(int(a)/int(b))

    except ZeroDivisionError:
        print("Division by zero not allowed")

    print("Out of try except blocks")


if __name__ == "__main__":
    while True:
        a = input("Enter 'a' value: ")
        b = input("Enter 'b' value: ")

        divide(a, b)
