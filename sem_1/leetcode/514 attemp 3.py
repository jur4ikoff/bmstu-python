import collections


def findRotateSteps(ring: str, key: str) -> int:
    char_pos = collections.defaultdict(set)
    for i, c in enumerate(ring):
        char_pos[c].add(i)

    def minstep(fromm, to):
        if fromm == to:
            return 0
        min_steps = min(abs(fromm - to), abs(len(ring) - abs(fromm - to)))
        return min_steps

    dp = [0] * len(ring)
    for p in char_pos[key[0]]:
        dp[p] = minstep(0, p)

    prev_char = key[0]
    for c in key[1:]:
        for next_pos in char_pos[c]:
            dp[next_pos] = min(dp[prev_pos] + minstep(prev_pos, next_pos) for prev_pos in char_pos[prev_char])
        prev_char = c

    return min(dp[p] for p in char_pos[prev_char]) + len(key)


print(findRotateSteps('godding', 'gdn'))
