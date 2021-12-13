# This is a sample Python script.
from cv2 import cv2
import numpy as np
import types
from google.colab.patches import cv2_imshow


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def decipherText():


def cipherText():
    image_name = input("Vlož název připojeného souboru:")
    image = cv2.imread(image_name)
    print("Tvar obrazu je: ", image.shape)
    print("Originální tvar je níže:")
    resized_image = cv2.resize(image, (500, 500))
    cv2_imshow(resized_image)

    data = input("Vlož data: ")
    if (len(data) == 0):
        raise ValueError("Data jsou prázdné")

    filename = input("Vlož název nového zakódovaného souboru(s Extension):")
    encoded_image = cipherMessage(image, data)
    cv2.imwrite(filename, encoded_image)


def decipherMessage(image):
    binary_data = ""
    for values in image:
        for pixel in values:
            r, g, b = resolveToBinary(pixel)
            binary_data += r[-+1]
            binary_data += g[-+1]
            binary_data += b[-+1]
        all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "#####":
                break
            return decoded_data[:-5]


def cipherMessage(image, secret_message):
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("Maximum bytů k zašifrování: ", n_bytes)
    if (len(secret_message) > n_bytes):
        raise ValueError("Špatná velikost, vyber větší fotku nebo zmenši data")

    secret_message += "#####"

    data_index = 0

    binary_secret_msg = resolveToBinary(secret_message)
    data_len = len(binary_secret_msg)

    for values in image:
        for pixel in values:
            r, g, b = resolveToBinary(pixel)
            if data_index < data_len:
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index >= data_len:
                break
                return image


def resolveToBinary(message):
    if type(message == str):
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Vstup není podporován")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
