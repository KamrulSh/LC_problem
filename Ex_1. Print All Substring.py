def printAllSubstrings(string):
    ln = len(string)
    c = 0
    for i in range(1, ln + 1):
        for j in range(ln - i + 1):
            print(string[j: j + i])
            c += 1
    print("Total Substrings: ", c)

    """
    a
    b
    c
    d
    ab
    bc
    cd
    abc
    bcd
    abcd
    Total Substrings:  10
    """


def printAllSubstrings2(string):
    ln = len(string)
    c = 0
    for i in range(ln):
        for j in range(i+1, ln+1):
            print(string[i:j])
            c += 1
    print("Total Substrings: ", c)

    """
    a
    ab
    abc
    abcd
    b
    bc
    bcd
    c
    cd
    d
    Total Substrings:  10
    """


st = "abcd"
printAllSubstrings(st)
printAllSubstrings2(st)
