def findRotateSteps(ring: str, key: str) -> int:
    dict = {}

    def dp(i, j):
        if (i, j) in dict:
            return dict[(i, j)]
        if j == len(key):
            return 0
        ans = float('inf')
        for k in range(len(ring)):
            if ring[k] == key[j]:
                steps = min(abs(k - i), len(ring) - abs(k - i))
                ans = min(ans, steps + dp(k, j + 1))
        dict[(i, j)] = ans
        return ans

    return dp(0, 0) + len(key)