def rotate_right(mat: list):
    return tuple(zip(*mat[::-1]))


def rotate_left(mat: list):
    return tuple(zip(*mat))[::-1]


def rotate_matrix_task(input_fie='in.txt', output_file='out.txt'):
    matx = []
    with open(input_fie, 'r') as file:
        while True:
            string = list(file.readline().strip().split())

            if not string:
                break
            matx.append(string)
    matx = rotate_right(matx)
    with open(file=output_file, mode='w') as output:
        for i in matx:
            print(list(i))
            string = ' '.join(list(i)) + '\n'
            output.write(string)


print(rotate_matrix_task())
