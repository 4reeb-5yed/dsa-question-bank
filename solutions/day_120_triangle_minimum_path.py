def minimum_total(triangle):
    n = len(triangle)
    dp = [0] * (n + 1)
    for row in reversed(triangle):
        for i in range(len(row)):
            dp[i] = row[i] + min(dp[i], dp[i + 1])
    return dp[0]