def threeSum(nums):
    res = []
    n = len(nums)
    nums = sorted(nums)
    for i in range(n - 2):
        a = nums[i]
        start = i + 1
        end = n - 1
        while (start < end):
            b = nums[start]
            c = nums[end]
            if (a + b + c == 0):
                if [a, b, c] not in (res):
                    res.append([a, b, c])
                start += 1
                end -= 1

            elif (a + b + c > 0):
                end -= 1
            else:
                start += 1

    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
