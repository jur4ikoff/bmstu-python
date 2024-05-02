import math


def validate(data: str, width, height, mode):
    output = []
    try:
        data = list(map(float, data.split(' ')))

        if mode == 0 and len(data) != 2:
            return -1, 1
        elif mode == 1 and len(data) != 3:
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


def find_distance(x1, y1, x2, y2):
    res = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return round(res, 2)


def find_max(circle, point):
    try:
        x, y = point[0][0], point[0][1]
    except Exception as e:
        print("Введите точку")
        return
    min_circle = []
    minn = 10 ** 9
    for i in range(len(circle)):
        center_x, center_y, radius = circle[i][0], circle[i][1], circle[i][2]
        dist = find_distance(center_x, center_y, x, y)
        print(dist)

        if dist < radius:
            true_dist = radius - dist
        else:
            true_dist = dist - radius

        if true_dist < minn:
            minn = true_dist
            min_circle = [center_x, center_y, radius]

    return  min_circle
