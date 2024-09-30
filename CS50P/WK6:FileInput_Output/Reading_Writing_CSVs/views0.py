import numpy as np
from PIL import Image


def main(): ...


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


if __name__ == "__main__":
    main()
