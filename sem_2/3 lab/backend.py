import PIL.Image as Image
import numpy
import os
import numpy as np


def save_image(arr):
    """Сохранение изображения"""
    new_image = Image.fromarray(arr)
    new_image.save("encode_image.bmp")
    return os.path.abspath("encode_image.bmp")


def bit_encrypt(cur_bit, cur_byte, bit_texts, arr, i, j, k):
    bit = bit_texts[cur_byte][cur_bit]
    cur_bit += 1
    if bit == '0':
        arr[i, j, k] &= 254
    else:
        arr[i, j, k] |= 1

    return arr, cur_bit


def bit_decrypt(byte, arr, cur_bit, i, j, k):
    byte <<= 1
    byte += arr[i, j, k] & 1
    cur_bit += 1

    return byte, cur_bit


def encrypt(text, file):
    """Шифрование текста"""
    img = Image.open(file)
    width, height = img.size[0], img.size[1]
    arr = np.array(img)
    bit_texts = [bin(i)[2:].zfill(8) for i in text.encode() + b'\x00']

    flag = False
    cur_byte, cur_bit = 0, 0
    for i in range(width):
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
                arr, cur_bit = bit_encrypt(cur_bit, cur_byte, bit_texts, arr, i, j, k)

    path = save_image(arr)
    return path


def decrypt(path: str) -> str:
    """Дешифровка"""
    img = Image.open(path)
    width, height = img.size[0], img.size[1]
    new_bytes = b""
    arr = numpy.array(img)
    byte = 0
    cur_bit = 0
    flag = False
    for i in range(width):
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

                byte, cur_bit = bit_decrypt(byte, arr, cur_bit, i, j, k)

    return new_bytes.decode()
