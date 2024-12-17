def minimum_money():
    import sys
    input = sys.stdin.read
    from heapq import heappush, heappop
    MAX_WEIGHT = 10000

    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1

    results = []

    for _ in range(T):
        E = int(data[idx])
        F = int(data[idx + 1])
        idx += 2

        W_target = F - E
        N = int(data[idx])
        idx += 1

        coins = []
        for _ in range(N):
            P = int(data[idx])
            W = int(data[idx + 1])
            coins.append((P, W))
            idx += 2

        dp = [float('inf')] * (W_target + 1)
        dp[0] = 0

        pq = [(0, 0)]

        while pq:
            value, weight = heappop(pq)

            if weight == W_target:
                break

            for coin_value, coin_weight in coins:
                next_weight = weight + coin_weight
                next_value = value + coin_value

                if next_weight <= W_target and dp[next_weight] > next_value:
                    dp[next_weight] = next_value
                    heappush(pq, (next_value, next_weight))

        results.append(dp[W_target] if dp[W_target] != float('inf') else -1)

    for result in results:
        print(result)

        
minimum_money()