if __name__ == "__main__":
    table_size = int(input("Enter the size of the table: "))
    layout = "{:>3}{:>6}" + ("{:>4}" * (table_size-1))
    numbers = list(range(1,table_size+1))

    print(layout.format('', *numbers))
    print("  :------" + ("----" * (table_size-1)))

    for num in numbers:
        row = [str(num) + ":"]
        for multiplier in numbers:
            row.append(num*multiplier)
        print(layout.format(*row))





