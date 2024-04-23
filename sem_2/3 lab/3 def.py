from PIL import Image, ImageDraw
import numpy as np


def draw_black_lines(x, y, arr, width, height):
    while y > 0 and x < width - 1:
        x += 1
        y -= 1
        arr[x, y] = [0, 0, 0]
    # for i in range(width):
    # for j in range(height):

    return arr


path = "for def.bmp"
img = Image.open(path)
draw = ImageDraw.Draw(img)
width, height = img.size[0], img.size[1]
print(width, height)
arr = np.array(img)
koef = max(width, height) / min(width, height)
for x in range(0, max(width, height), 50):
    draw.line((0, x, x * int(koef), 0), fill='red', width=1)
    # arr = draw_black_lines(0, x - 1, arr, width, height)

new_image = Image.fromarray(arr)
new_image.show()
