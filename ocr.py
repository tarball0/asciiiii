from PIL import Image
import pytesseract


def read(filename="table1.jpg"):
    string = pytesseract.image_to_string(Image.open(filename))
    print(string)


if __name__ == "__main__":
    read()
