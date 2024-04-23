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
            k = round(dy / dx, 2)
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
    status, k = max_k(lines)
    is_line = False
    if status:
        k = str(k)
    else:
        return is_line, 0, 0, 0, 0

    print(k)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            try:
                cur_k = round(dy / dx, 2)
            except ZeroDivisionError:
                cur_k = "inf"
            if k == str(cur_k):
                is_line = True
                return is_line, points[i][0], points[i][1], points[j][0], points[j][1]

    return is_line, 0, 0, 0, 0


'''
points = [[130, 130], [128, 287], [126, 289], [125, 292], [124, 297], [124, 304], [126, 313], [134, 328],
          [147, 343],
          [162, 355], [179, 363], [197, 368], [214, 370], [230, 370], [246, 370], [262, 369], [280, 365], [299, 359],
          [315, 351], [331, 342], [349, 329], [367, 317], [385, 302], [402, 287], [417, 272], [429, 260], [441, 248],
          [453, 236], [465, 226], [476, 217], [486, 210], [495, 201], [503, 191], [510, 181], [515, 171], [520, 164],
          [522, 157], [522, 154], [522, 151], [519, 148], [508, 144], [491, 140], [468, 136], [444, 136], [417, 136],
          [389, 140], [365, 143], [345, 148], [330, 330], [315, 156], [305, 158], [298, 160], [293, 162], [289, 163],
          [286, 163], [200, 200]]

arr = [[200.0, 200.0, 100.0, 100.0], [100.0, 100.0, 10.0, 500.0], [10.0, 500.0, 500.0, 10.0], [500.0, 10.0, 0.0, 0.0],
       [0.0, 0.0, 500.0, 500.0], [500.0, 500.0, 500.0, 10.0], [100, 100, 200, 200]]
print(find_max_line(points, arr))
'''
