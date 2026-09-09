# Accept number of items
n = int(input("Enter number of items: "))

# Accept weights and values
weights = []
values = []

print("Enter weights of items:")
for i in range(n):
    weights.append(int(input(f"Weight of item {i + 1}: ")))

print("Enter values of items:")
for i in range(n):
    values.append(int(input(f"Value of item {i + 1}: ")))

# Accept bag capacity
capacity = int(input("Enter bag capacity: "))

# Create DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Fill the DP table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        # If item can fit in the bag
        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )

        # If item cannot fit
        else:
            dp[i][w] = dp[i - 1][w]

# Display maximum obtainable value
print("Maximum obtainable value:", dp[n][capacity])