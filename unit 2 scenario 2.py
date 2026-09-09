# Fibonacci Using Memoization
# Top-Down Dynamic Programming

# Dictionary to store previously calculated values
memo = {}

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Check if value is already calculated
    if n in memo:
        return memo[n]

    # Calculate and store the value
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]


# Accept N
N = int(input("Enter the number of Fibonacci numbers: "))

# Generate first N Fibonacci numbers
sequence = []

for i in range(N):
    sequence.append(fibonacci(i))

# Display the sequence
print("Fibonacci sequence:")
print(sequence)