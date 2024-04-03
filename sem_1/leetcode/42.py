# 42. Trapping Rain Water

def trap_not_efec(self, height: list[int]) -> int:  # неэфек
    n = len(height)
    res = 0
    for i in range(1, n - 1):
        max_left = height[i]
        for j in range(i):
            max_left = max(max_left, height[j])

        max_right = height[i]
        for j in range(i, n):
            max_right = max(max_right, height[j])

        res += min(max_left, max_right) - height[i]

    return res


def trap(height: list[int]) -> int:  # эфек
    n = len(height)
    res = 0
    right = []
    left = []
    for i in range(0, n):
        left_el = max(height[:i + 1])
        left.append(left_el)

    for i in range(0, n):
        right_el = max(height[i:])
        right.append(right_el)

    for i in range(n):
        res += (min(left[i], right[i]) - height[i])

    return res


print(trap([4, 2, 0, 3, 2, 5]))
