def beolvas():
    playlist = []

    with open("playlist.csv", "r") as f:
        for item in f:
            if item.strip():
                zene = {
                    "eloado": item.split(';')[0],
                    "cim": item.split(';')[1],
                    "mufaj": item.split(';')[2],
                    "hossz": int(item.split(';')[3])
                }

            playlist.append(zene)

    return playlist


def teljes_hossz(playlist):
    teljes = 0

    for i in playlist:
        teljes += i["hossz"]

    with open("02_hossz.txt", "w") as f:
        f.write(str(int(teljes/60)) + ":" + str(teljes%60))


def leghosszabb_rockzene(playlist):
    rock_zenek = []

    for i in playlist:
        if i["mufaj"] == "rock":
            rock_zenek.append(i)

    leghosszabb = rock_zenek[0]

    for i in rock_zenek:
        if i["hossz"] > leghosszabb["hossz"]:
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
            gyakorisag = count

    with open("04_kedvenc_mufaj.txt", "w") as f:
        f.write(leggyakoribb.upper())


def zeneket_csoportosit(playlist):
    eloadok = []

    for i in playlist:
        if i["eloado"] not in eloadok:
            eloadok.append(i["eloado"])

    osszegzes = []

    for i in eloadok:
        hossz = 0
        for x in playlist:
            if x["eloado"] == i:
                hossz += x["hossz"]
        osszegzes.append((i + ": " + str(hossz) + "s\n"))

    osszegzes.sort()

    with open("05_osszegzes.txt", "w") as f:
        for i in osszegzes:
            f.write(i)


def zeneket_listaz(playlist, eloado):
    eloadonev = ""

    if " " in eloado:
        for i in eloado.lower():
            if i != " ":
                eloadonev += i
            else:
                eloadonev += "_"
    else:
        eloadonev = eloado.lower()

    with open(("06_"+eloadonev+"_dalok.txt"),"w") as f:
        is_there = False
        for i in playlist:
            if i["eloado"].lower() == eloado.lower():
                is_there = True
                f.write(i["cim"] + ";" + i["mufaj"] + ";" + str(i["hossz"]) + "\n")

        if is_there == False:
            f.write("Nincs ilyen előadó a lejátszási listában!")




if __name__ == "__main__":
    playlist = beolvas()
    teljes_hossz(playlist)
    leghosszabb_rockzene(playlist)
    leggyakoribb_mufaj(playlist)
    zeneket_csoportosit(playlist)
    zeneket_listaz(playlist, "Gopnik McBlyat")
