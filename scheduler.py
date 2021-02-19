import sys

def read(file):
    prefs = {}
    sessions = ['A', 'B', 'C']
    nrows = 0
    with open(file, 'r') as ifile:
        ifile.readline()
        for line in ifile:
            line = line.strip()
            if(line):
                nrows += 1
                row = line.split(",")
                person_prefs = [0, 0, 0]
                i = 0
                for e in row[1:]:
                    e = int(e)
                    if e != 0:
                        person_prefs[3 - e] = sessions[i]
                    i += 1
                prefs[row[0]] = person_prefs
    return prefs, nrows


def main():
    if len(sys.argv) < 1:
        raise Exception("Need arguments: file to read and size of groups.")
        return -1
    file = sys.argv[1]
    groups = {"A": [], "B": [], "C": []}
    prefs, n = read(file)
    k = int(sys.argv[2])
    for person in prefs.keys():
        pref = prefs[person][0]
        if pref != 0:
            groups[pref].append(person)

    current = {k: 1 for k in prefs.keys()}

    # rematching
    for group in groups.values():
        while len(group) > k:
            for person in group:
                next_proposal = current[person]
                next_pref = prefs[person][next_proposal]
                current[person] += 1
                if next_pref == 0:
                    pass
                elif len(groups[next_pref]) < k:
                    groups[next_pref].append(person)
                    group.remove(person)

                if len(group) <= k:
                    break

    print(groups)


main()
