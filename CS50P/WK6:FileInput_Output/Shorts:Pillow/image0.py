from PIL import Image


def main():
    img = Image.open("in.jpeg")
    img.close()


if __name__ == "__main__":
    main()
