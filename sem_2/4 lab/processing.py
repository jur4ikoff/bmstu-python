def validate(data: str, width, height, mode):
    output = []
    try:
        data = list(map(float, data.split(' ')))

        if mode == 0 and len(data) != 2:
            return -1, 1
        elif mode == 1 and len(data) != 4:
            return -1, 1

        for i in data:
            if i >= 0 and i <= width and i <= height:
                output.append(i)
            else:
                return -1, 1

        return output, 0
    except Exception as e:
        print(e)
        return -1, 1


def make_array_unique(array):
    unique_arrays = []
    for arr in array:
        if arr not in unique_arrays:
            unique_arrays.append(arr)
    return unique_arrays


def max_k(arr):
    k_arr = {}
    for i in range(len(arr)):
        dy = (arr[i][3] - arr[i][1])
        dx = (arr[i][2] - arr[i][0])
        if dx == 0:
            if "inf" in k_arr.keys():
                k_arr["inf"] += 1
            else:
                k_arr["inf"] = 1
        else:
            k = round(dy / dx, 3)
            if k in k_arr.keys():
                k_arr[k] += 1
            else:
                k_arr[k] = 1
    try:
        k_max = max(k_arr, key=k_arr.get)
    except Exception:
        return False, -1
    return True, k_max


def find_max_line(points, lines):
    k = max_k(lines)
    print(points)
    is_line = False
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            print(i, j)


arr = [[200.0, 200.0, 100.0, 100.0], [100.0, 100.0, 10.0, 500.0], [10.0, 500.0, 500.0, 10.0], [500.0, 10.0, 0.0, 0.0],
       [0.0, 0.0, 500.0, 500.0], [500.0, 500.0, 500.0, 10.0], [100, 100, 200, 200]]
# print(find_max_line(arr))
