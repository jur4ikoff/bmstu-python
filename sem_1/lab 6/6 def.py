height = list(map(int, input().split()))
n = len(height)
res = 0
l, r = 0, n - 1
while l < r:
    area = (min(height[l], height[r]) * (r - l))
    res = max(res, area)

    if height[l] <= height[r]:
        l += 1
    else:
        r -= 1

print(res)