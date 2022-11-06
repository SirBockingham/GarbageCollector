import string

def irasjel_eltavolitas(text):
    irasjel_nelkuli = ""
    for karakter in text:
        if karakter not in string.punctuation and karakter != " ":
            irasjel_nelkuli += karakter
    return irasjel_nelkuli

def ketbetus(text):
    list = ["cs","dzs", "dz", "gy", "ly", "ny", "sz", "ty", "zs"]
    uj_text = ""

    i = 0
    while(i < len(text)-1):
        if text[i]+text[i+1] in list:
            uj_text += text[i+1] + text[i]
            i+=1
        else:
            uj_text += text[i]
        i+=1
    uj_text += text[-1]
    return uj_text


if __name__ == "__main__":
    text = input("Adjon meg egy szöveget: ").lower()
    irasjel_nelkul = irasjel_eltavolitas(text)
    ketbetus_forditva = ketbetus(irasjel_nelkul)

    if irasjel_nelkul == ketbetus_forditva[::-1]:
        print("Ez egy palindróm")
    else:
        print("Ez nem egy palindróm")



