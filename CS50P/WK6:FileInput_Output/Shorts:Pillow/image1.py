from PIL import Image


def main():
    img = Image.open("in.jpeg")
    print(img.size)
    print(img.format)
    img.close()

if __name__ == "__main__":
    main()