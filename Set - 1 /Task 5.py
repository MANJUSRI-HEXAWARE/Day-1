
def greedy_change(amount, denominations):
    denominations = sorted(denominations, reverse=True)
    result = []

    for coin in denominations:
        count = amount // coin

        if count > 0:
            result.extend([coin] * count)
            amount = amount % coin

    if amount != 0:
        return None

    return result


def dp_change(amount, denominations):
    dp = [float("inf")] * (amount + 1)
    chosen = [0] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in denominations:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                chosen[i] = coin

    if dp[amount] == float("inf"):
        return None, None, dp

    result = []
    current = amount

    while current > 0:
        coin = chosen[current]
        result.append(coin)
        current -= coin

    return dp[amount], result, dp


def main():
    print("=" * 65)
    print("TASK 5 - REFUND CALCULATION")
    print("GREEDY ALGORITHM AND DYNAMIC PROGRAMMING")
    print("=" * 65)

    print("\nPART A - GREEDY ALGORITHM")
    print("-" * 65)

    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    amount = 1873

    result = greedy_change(amount, denominations)

    print("Refund Amount:", amount)
    print("Available Denominations:", denominations)

    print("\nSelected Notes / Coins:")

    for coin in result:
        print("Rs.", coin)

    print("\nTotal Notes / Coins:", len(result))
    print("Total Value:", sum(result))

    print("\n" + "=" * 65)
    print("PART B - CASE WHERE GREEDY FAILS")
    print("=" * 65)

    test_denominations = [1, 3, 4]
    test_amount = 6

    greedy_result = greedy_change(test_amount, test_denominations)

    print("Refund Amount:", test_amount)
    print("Denominations:", test_denominations)
    print("\nGreedy Result:", greedy_result)
    print("Greedy Coin Count:", len(greedy_result))

    print("\n" + "=" * 65)
    print("PART C - DYNAMIC PROGRAMMING")
    print("=" * 65)

    minimum_count, dp_result, dp = dp_change(
        test_amount, test_denominations
    )

    print("Refund Amount:", test_amount)
    print("Denominations:", test_denominations)

    print("\nDP TABLE")
    print("-" * 65)
    print(f"{'Amount':<15}{'Minimum Coins':<20}")
    print("-" * 65)

    for i in range(test_amount + 1):
        print(f"{i:<15}{dp[i]:<20}")

    print("-" * 65)

    print("\nOptimal Coin Combination:", dp_result)
    print("Minimum Number of Coins:", minimum_count)

    print("\n" + "=" * 65)
    print("GREEDY VS DYNAMIC PROGRAMMING")
    print("=" * 65)

    print(f"{'Algorithm':<25}{'Coin Count':<15}{'Combination'}")
    print("-" * 65)

    print(f"{'Greedy':<25}{len(greedy_result):<15}{greedy_result}")
    print(f"{'Dynamic Programming':<25}{minimum_count:<15}{dp_result}")
    print("-" * 65)
    print("\nTASK 5 EXECUTION COMPLETED")


if __name__ == "__main__":
    main()
