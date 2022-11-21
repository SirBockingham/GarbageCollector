def beolvas():
    playlist = []

    with open("playlist.csv", "r") as file:
        sorok = file.readlines()

        for i in range(1, len(sorok)):
            if sorok[i].strip():
                sor = sorok[i].split(';')

                zene = {
                    "eloado": sor[0],
                    "cim": sor[1],
                    "mufaj": sor[2],
                    "hossz": int(sor[3])
                }
                playlist.append(zene)
    return playlist


def teljes_hossz(playlist):
    hossz = 0

    for i in playlist:
        hossz += i["hossz"]

    with open("02_hossz.txt", "w") as f:
        f.write(str(int(hossz/60)) + ":" + str(hossz%60))


def leghosszabb_rockzene(playlist):
    for i in playlist:
        if i["mufaj"] == "rock":
            leghosszabb = i
            break

    for i in playlist:
        if i["mufaj"] == "rock":
            if i["hossz"] == leghosszabb["hossz"]:
                continue
            elif i["hossz"] > leghosszabb["hossz"]:
                leghosszabb = i

    with open("03_leghosszabb_rock.txt", "w") as f:
        f.write(leghosszabb["cim"])


def leggyakoribb_mufaj(playlist):
    mufajok = []
    leggyakoribb = ""
    gyakorisag = 0

    for i in playlist:
        if i["mufaj"] not in mufajok:
            mufajok.append(i["mufaj"])

    for i in mufajok:
        count = 0
        for x in playlist:
            if x["mufaj"] == i:
                count += 1

        if count > gyakorisag:
            leggyakoribb = i

    with open("04_kedvenc_mufaj.txt", "w") as f:
        f.write(leggyakoribb.upper())

if __name__ == "__main__":
    playlist = beolvas()
    teljes_hossz(playlist)
    leghosszabb_rockzene(playlist)
    leggyakoribb_mufaj(playlist)
