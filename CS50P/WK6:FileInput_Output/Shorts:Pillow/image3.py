from PIL import Image


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img.save("out1.jpeg")

if __name__ == "__main__":
    main()
