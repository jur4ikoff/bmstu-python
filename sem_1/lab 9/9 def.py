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


def trap(height: list[int]) -> int:  # 'эфек'
    n = len(height)
    res = 0
    left = [0] * n
    cur_max = height[0]
    left[0] = height[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], height[i])

    right = [0] * n
    right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], height[i])

    for i in range(n):
        res += (min(left[i], right[i]) - height[i])
    return res


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
