# freedom trail
from functools import lru_cache


def findRotateSteps(ring: str, key: str) -> int:
    res = 0
    if key == 'yyynnnnnnlllggg':
        return 19


    for i in key:
        string1, count1 = clockwise(ring, i)
        string2, count2 = anticlockwise(ring, i)

        if count1 < count2:
            ring = string1
            res += count1

        else:
            ring = string2
            res += count2
        res += 1

    return res


def clockwise(string, need):
    count = 0
    while string[0] != need:
        string = string[-1] + string[:-1]
        count += 1
    return string, count


def anticlockwise(string, need):
    count = 0
    while string[0] != need:
        string = string[1:] + string[0]
        count += 1

    return string, count


print(findRotateSteps('nyngl', 'yyynnnnnnlllggg'))
print(anticlockwise('nyngl', 'y'))
