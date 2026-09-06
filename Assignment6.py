def knapsack_top_down(weights, values, n, capacity, memo):

    if n == 0 or capacity == 0:
        return 0

    if memo[n][capacity] != -1:
        return memo[n][capacity]

    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity,
            memo
        )

    else:
        include = values[n - 1] + knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity - weights[n - 1],
            memo
        )

        exclude = knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity,
            memo
        )

        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]

def knapsack_bottom_up(weights, values, n, capacity):

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]

                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    return dp

def find_selected_items(dp, weights, values, n, capacity):

    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected.append(i)

            w = w - weights[i - 1]

    selected.reverse()

    return selected

n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):

    print("\nItem", i + 1)

    weight = int(input("Enter weight: "))
    value = int(input("Enter value: "))

    weights.append(weight)
    values.append(value)


capacity = int(input("\nEnter knapsack capacity: "))

memo = [[-1] * (capacity + 1) for _ in range(n + 1)]

top_down_result = knapsack_top_down(
    weights,
    values,
    n,
    capacity,
    memo
)

print("\n----- TOP-DOWN APPROACH -----")
print("Maximum Value =", top_down_result)

dp = knapsack_bottom_up(
    weights,
    values,
    n,
    capacity
)

bottom_up_result = dp[n][capacity]

print("\n----- BOTTOM-UP APPROACH -----")
print("Maximum Value =", bottom_up_result)

selected = find_selected_items(
    dp,
    weights,
    values,
    n,
    capacity
)

print("\nSelected Items:")

total_weight = 0
total_value = 0

for item in selected:

    print(
        "Item", item,
        "- Weight:", weights[item - 1],
        "Value:", values[item - 1]
    )

    total_weight += weights[item - 1]
    total_value += values[item - 1]


print("\nTotal Weight =", total_weight)
print("Total Value =", total_value)