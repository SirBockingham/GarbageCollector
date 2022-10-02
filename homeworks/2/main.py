def is_legit(a, b, c):
    a = a
    b = b
    c = c

    if(a + b > c and a + c > b and b + c > a):
        print("A {}, {} és {} oldalú háromszög szerkeszthető.".format(a, b, c))
    else:
        print("A {}, {} és {} oldalú háromszög NEM szerkeszthető.".format(a, b, c))


if __name__ == "__main__":
    print("Adja meg a háromszög oldalát cm-ben:")
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))

    is_legit(a, b, c)
