def text_stats(text):
    text = text

    letters = {}
    for x in text:
        if x not in letters.keys():
            letters[x] = 1

        else:
            letters[x] = letters[x] + 1

    print("Betűk gyakorisága: ", letters)

    # __________________

    print("Fordítva: ", text[::-1])

    # __________________

    words = text.split(' ')
    print("Listába rendezve szavanként: ", words)


def unit_converter(num, unit):
    num = num
    unit = unit

    if unit == "cm":
        print(float(num)/2.54, "inch")

    elif unit == "inch":
        print(float(num)*2.54, "cm")

    else:
        print("Not Correct Unit!")


if __name__ == "__main__":
    menu = input("Type 1 for Text Statistics, or 2 for Unit Converter: ")

    if menu == "1":
        print("Adjon meg egy mondatot:")
        text = input()

        text_stats(text)

    elif menu == "2":
        print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
        num = input()
        unit = input()

        unit_converter(num, unit)

    else:
        print("That Was Not An Option!")
