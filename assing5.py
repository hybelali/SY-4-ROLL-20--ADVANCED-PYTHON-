def lcs_tabulation(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create DP table (Tabulation)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the LCS by backtracking
    i = m
    j = n
    ans = []

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            ans.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    ans.reverse()

    return "".join(ans), dp[m][n]


# Main Program
first = input("Enter first string: ")
second = input("Enter second string: ")

lcs, length = lcs_tabulation(first, second)

print("\nLongest Common Subsequence:", lcs)
print("Length of LCS:", length)



