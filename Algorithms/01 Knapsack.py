def knapsack(values, weights, m):
    n = len(weights)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, m + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    selected = [0] * n
    w = m

    for i in range(n , 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected[i - 1] = 1
            w -= weights[i - 1]

    return dp[n][m], selected


values = [1, 2, 5, 6]
weights = [2, 3, 4, 5]
m = 8

max_profit, selected = knapsack(values, weights, m)
print(f"profit : {max_profit}")
print(f"selected : {selected}")

# maximum profit: 8
# selected array: [0, 1, 0, 1]