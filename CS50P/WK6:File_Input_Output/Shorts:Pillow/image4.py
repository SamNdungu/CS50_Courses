from PIL import Image, ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.BLUR)
        img.save("out2.jpeg")

if __name__ == "__main__":
    main()