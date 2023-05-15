"""
Leetcode problem:
5. https://leetcode.com/problems/longest-palindromic-substring/
647. https://leetcode.com/problems/palindromic-substrings/

Time complexity: O(N^2). A nested traversal is needed.
Auxiliary Space: O(N^2). A matrix of size N*N is needed to store the table.
"""


def printStr(string, start, end):
    print("Longest substring = ", string[start : end + 1])


def longestPalindromeSubstring(string):
    ln = len(string)
    palindrome = []
    palindrome_count = 0
    """
    length of string = 9
    """

    table = [[0 for i in range(ln)] for i in range(ln)]
    print(table)
    """
    table =>
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """

    """
    CASE 1: 
        string[i][i] (i.e substring of length one), will always be true as a substring of unit length is always palindromic.
    """

    print("\nIteration for length = 1")
    i = 0
    maxLength = 1
    while i < ln:
        table[i][i] = 1
        # store the palindrome string
        palindrome.append(string[i : i + 1])
        palindrome_count += 1
        start = i
        i += 1
    print(table)
    print(palindrome)

    """ 
    All substrings of length 1 are palindromes
    Iteration times (9) => 00,11,22,33,44,55,66,77,88

    [[1, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 1, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 1, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 1, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 1, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 1, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 1, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 1, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    
    Palindrome =>
    ['c', 'c', 'f', 'b', 'a', 'b', 'a', 'b', 'd']

    """

    """
    CASE 2: 
        string[i:i+1] (i.e substring of length two), will be true only if string[i] and string[i+1] are equal.
    """
    print("\nIteration for length = 2")
    i = 0
    while i < ln - 1:
        if string[i] == string[i + 1]:
            table[i][i + 1] = 1
            start = i
            maxLength = 2
            palindrome.append(string[i : i + 2])
            palindrome_count += 1
        i += 1
    print(table)
    print(palindrome)

    """
    For substrings of length 2 if both are same then it is palindrome
    Iteration times (8) => 01,12,23,34,45,56,67,78

    [[1, 1, 0, 0, 0, 0, 0, 0, 0], 
     [0, 1, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 1, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 1, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 1, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 1, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 1, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 1, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 1]]

    Palindrome =>
    ['c', 'c', 'f', 'b', 'a', 'b', 'a', 'b', 'd', 'cc']

    """

    """
    Check for substring of length str_len where str_len > 2
    str_len is length of substring (3 to 9)

    CASE 3:
    1. Start from index 0 and check for substring of length str_len (formula => end = init + str_len - 1)
        Example: 
            str_len = 3, init = 0, end = 0 + 3 - 1 = 2
            str_len = 4, init = 0, end = 0 + 4 - 1 = 3
    2. If string[init] == string[end] and table[init + 1][end - 1] == 1 then table[init][end] = 1
        Example:
            string[0] == string[2] and table[0 + 1][2 - 1] == 1 then table[0][2] = 1
            string[0] == string[3] and table[0 + 1][3 - 1] == 1 then table[0][3] = 1
    3. If table[init][end] == 1 then store the palindrome string and update the maxLength
        Example:
            table[0][2] == 1 then palindrome.append(string[0 : 2 + 1]) and maxLength = str_len
            table[0][3] == 1 then palindrome.append(string[0 : 3 + 1]) and maxLength = str_len
    4. Increment init by 1
    5. Repeat the steps 1 to 4 till init < ln - str_len + 1
    6. Increment str_len by 1
    7. Repeat the steps 1 to 6 till str_len <= ln
    """

    str_len = 3
    while str_len <= ln:
        print(f"\nIteration for length = {str_len}")
        init = 0
        while init < ln - str_len + 1:
            end = init + str_len - 1
            if string[init] == string[end] and table[init + 1][end - 1] == 1:
                table[init][end] = 1
                palindrome.append(string[init : end + 1])
                palindrome_count += 1
                if str_len > maxLength:
                    start = init
                    maxLength = str_len
            init += 1
        print(table)
        print(palindrome)
        str_len += 1

    """
    Iteration for length = 3
    Iteration times (7) => 012,123,234,345,456,567,678
    [[1, 1, 0, 0, 0, 0, 0, 0, 0], 
     [0, 1, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 1, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 1, 0, 1, 0, 0, 0], 
     [0, 0, 0, 0, 1, 0, 1, 0, 0], 
     [0, 0, 0, 0, 0, 1, 0, 1, 0], 
     [0, 0, 0, 0, 0, 0, 1, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 1, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    ['c', 'c', 'f', 'b', 'a', 'b', 'a', 'b', 'd', 'cc', 'bab', 'aba', 'bab']

    Iteration for length = 4
    [[1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    ['c', 'c', 'f', 'b', 'a', 'b', 'a', 'b', 'd', 'cc', 'bab', 'aba', 'bab']

    Iteration for length = 5
    [[1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    ['c', 'c', 'f', 'b', 'a', 'b', 'a', 'b', 'd', 'cc', 'bab', 'aba', 'bab', 'babab']

    Iteration for length = 6
    [[1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    ['c', 'c', 'f', 'b', 'a', 'b', 'a', 'b', 'd', 'cc', 'bab', 'aba', 'bab', 'babab']

    Iteration for length = 7
    [[1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    ['c', 'c', 'f', 'b', 'a', 'b', 'a', 'b', 'd', 'cc', 'bab', 'aba', 'bab', 'babab']

    Iteration for length = 8
    [[1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    ['c', 'c', 'f', 'b', 'a', 'b', 'a', 'b', 'd', 'cc', 'bab', 'aba', 'bab', 'babab']

    Iteration for length = 9
    [[1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    """

    printStr(string, start, start + maxLength - 1)

    """
    Longest substring =  babab
    Max length =  5
    """
    return maxLength, palindrome_count


if __name__ == "__main__":
    string = "ccfbababd"
    print("Maximum length, palindrome count = ", longestPalindromeSubstring(string))
