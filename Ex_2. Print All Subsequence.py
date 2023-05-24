def printAllSubsequence(string):
    if len(string) == 0:
        return [""]
    smallOutput = printAllSubsequence(string[1:])
    result = [""] * 2*len(smallOutput)

    k = 0
    for i in range(len(smallOutput)):
        result[k] = smallOutput[i]
        k += 1
    for i in range(len(smallOutput)):
        result[k] = string[0]+smallOutput[i]
        k += 1
    return result


print(printAllSubsequence("abcd"))

"""
['', 'd', 'c', 'cd', 'b', 'bd', 'bc', 'bcd', 'a', 'ad', 'ac', 'acd', 'ab', 'abd', 'abc', 'abcd']
"""
