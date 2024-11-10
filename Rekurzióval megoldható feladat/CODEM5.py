def minObjects(n, k, weights):
    memo = {}

    def seged(index, jelenlegi):
        if jelenlegi == 0:
            return 0
        if index >= n or jelenlegi < 0:
            return float('inf')

        if (index, jelenlegi) in memo:
            return memo[(index, jelenlegi)]

        include = float('inf')
        if jelenlegi >= weights[index]:
            include = seged(index + 1, jelenlegi - weights[index]) + 1
        
        exclude = seged(index + 1, jelenlegi)

        result = min(include, exclude)

        memo[(index, jelenlegi)] = result
        return result

    answer = seged(0, k)
    return answer if answer != float('inf') else "impossible"

T = int(input())
results = []
for _ in range(T):
    n, k = map(int, input().split())
    weights = list(map(int, input().split()))
    result = minObjects(n, k, weights)
    results.append(result)

for result in results:
    print(result)
