class Team:
    def __init__(self, nev, project, role):
        self._nev = nev
        self._project = project
        self._role = role
        self._checked = []

        print("-- Developer létrehozva. --")
        print(self._nev + " a " + self._project + "-en dolgozik " + self._role + " szerepkörben")

    def __eq__(self, other_member):
        return self._project == other_member._project

    @property
    def nev(self):
        return self._nev


    def get_checked(self):
        return self._checked

    def set_checked(self, member):
        self._checked.append(member)



if __name__ == "__main__":
    member1 = Team("Ricsi", "SolArch", "Frontend")
    member2 = Team("Angéla", "ZerTeng", "Tesztelő")
    member3 = Team("Peti", "KefERP", "Backend")
    member4 = Team("Éva", "KefERP", "Frontend")

    memberList = [member1, member2, member3, member4]

    print()

    for i in range(len(memberList)):
        for x in range(len(memberList)):
            if memberList[i].nev == memberList[x].nev:
                continue
            elif memberList[x].nev in memberList[i].get_checked():
                continue
            else:
                if memberList[i] == memberList[x]:
                    print(memberList[i].nev, " és " + memberList[x].nev, " egy projekten dolgoznak.")
                memberList[x].set_checked(memberList[i].nev)
