import string

def dismember(line):
    new_line = ""
    mgh = ["a","A","á","Á","e","E","é","É","i","I","í","Í","o","O","ó","Ó","ö","Ö","ő","Ő","u","U","ú","Ú","ü","Ü","ű","Ű"]

    for x in line:
        if x not in string.punctuation and x not in mgh:
            new_line += x

    return new_line

if __name__ == "__main__":
    new_lines = []

    with open("be.txt","r", encoding="utf8") as f:
        line = f.readline()

        while line:
            if line.strip():
                line = dismember(line)
                new_lines.append(line)
            line = f.readline()


    with open("ki.txt","w") as f:
        for i in range(0,len(new_lines),3):
             f.write(str(new_lines[i]))