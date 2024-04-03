import PIL.Image as Image
import numpy
import os
import numpy as np


# encrypting and decrypting


def encrypt(text, file):
    img = Image.open(file)
    widht, height = img.size[0], img.size[1]
    arr = np.array(img)
    bit_texts = [bin(i)[2:].zfill(8) for i in text.encode() + b'\x00']

    flag = False
    cur_byte, cur_bit = 0, 0
    for i in range(widht):
        if flag:
            break
        for j in range(height):
            if flag:
                break
            for k in range(3):

                if cur_bit > 7:
                    cur_byte += 1
                    cur_bit = 0
                if cur_byte >= len(bit_texts):
                    flag = True
                    break

                bit = bit_texts[cur_byte][cur_bit]
                cur_bit += 1
                if bit == '0':
                    arr[i, j, k] &= 254
                else:
                    arr[i, j, k] |= 1

    new_image = Image.fromarray(arr)
    new_image.save("encode_image.bmp")
    return os.path.abspath("encode_image.bmp")


def decrypt(file):
    img = Image.open(file)
    widht, height = img.size[0], img.size[1]
    new_bytes = b""
    arr = numpy.array(img)
    byte = 0
    cur_bit = 0
    flag = False
    for i in range(widht):
        if flag:
            break
        for j in range(height):
            if flag:
                break
            for k in range(3):
                if cur_bit == 8:
                    if byte == 0:
                        flag = True
                        break
                    cur_bit = 0
                    new_bytes += int(byte).to_bytes(1, "little")
                    byte = 0

                byte <<= 1
                byte += arr[i, j, k] & 1
                cur_bit += 1

    return new_bytes.decode()
