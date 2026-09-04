import time

def fib_recursive(n):
    if n <= 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_memo(n, cache=None):
    if cache is None:
        cache = {0: 0, 1: 1}

    if n in cache:
        return cache[n]

    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    return cache[n]

def fib_dp(n):
    if n <= 1:
        return n

    a = 0      
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b

def fib_fast_doubling(n):

    def helper(n):
        if n == 0:
            return 0, 1

        a, b = helper(n // 2)

        c = a * (2 * b - a)
        d = a * a + b * b

        if n % 2 == 0:
            return c, d
        else:
            return d, c + d

    return helper(n)[0]

if __name__ == "__main__":

    n = 10

    recursive_result = fib_recursive(n)
    memo_result = fib_memo(n)
    dp_result = fib_dp(n)
    fast_result = fib_fast_doubling(n)

    print("Fibonacci number at n =", n)
    print("Recursive:", recursive_result)
    print("Memoization:", memo_result)
    print("Dynamic Programming:", dp_result)
    print("Fast Doubling:", fast_result)

    if recursive_result == memo_result == dp_result == fast_result:
        print("\nAll four methods give the same answer.")
    else:
        print("\nThe methods produced different answers.")

    print("\nFirst 15 Fibonacci numbers:")

    for i in range(15):
        print(fib_dp(i), end=" ")

    print()


    n = 28

    start = time.perf_counter()
    result_recursive = fib_recursive(n)
    end = time.perf_counter()

    recursive_time = end - start


    start = time.perf_counter()
    result_dp = fib_dp(n)
    end = time.perf_counter()

    dp_time = end - start


    print("\nTiming comparison for F(28):")
    print("Recursive result:", result_recursive)
    print("Recursive time:", recursive_time, "seconds")

    print("DP result:", result_dp)
    print("DP time:", dp_time, "seconds")


    n = 100

    print("\nF(100) using DP:")
    print(fib_dp(n))

    print("\nF(100) using Fast Doubling:")
    print(fib_fast_doubling(n))