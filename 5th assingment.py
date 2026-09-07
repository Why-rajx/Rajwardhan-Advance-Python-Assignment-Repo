def lcs(string1, string2):

    m = len(string1)
    n = len(string2)


    dp = [[0 for j in range(n + 1)]
          for i in range(m + 1)]


    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if string1[i - 1] == string2[j - 1]:

                dp[i][j] = dp[i - 1][j - 1] + 1

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )


    lcs_length = dp[m][n]

    i = m
    j = n
    answer = []

    while i > 0 and j > 0:

        if string1[i - 1] == string2[j - 1]:

            answer.append(string1[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:

            i -= 1

        else:

            j -= 1


    answer.reverse()

    return lcs_length, ''.join(answer)



string1 = input("Enter first string: ")
string2 = input("Enter second sequence: ")

length, subsequence = lcs(string1, string2)

print("\nLongest Common Subsequence:", subsequence)
print("Length of LCS:", length)