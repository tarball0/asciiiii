from PIL import Image
import pytesseract
import tabulate


def split_into_n(s, n):
    words = s.split(" ")
    total_words = len(words)
    base_size = total_words // n
    remainder = total_words % n
    parts = []
    start = 0
    for i in range(n):
        size = base_size + (1 if i < remainder else 0)
        parts.append(" ".join(words[start:start + size]))
        start += size
    return parts


def len_of_parts(inlist):
    checklines = [line.split() for line in inlist if line.strip()]
    total = sum(len(inner) for inner in checklines)
    return int(total/len(checklines))


def printtable(imgname='table3.jpg'):
    instring = pytesseract.image_to_string(Image.open(imgname))
    lines = instring.strip().split("\n")
    lengt = len_of_parts(lines)
    header = split_into_n(lines[0], lengt)
    data = [split_into_n(line, lengt) for line in lines[1:]]
    ascii_table = tabulate.tabulate(data, headers=header, tablefmt="grid")
    print(ascii_table)


if __name__ == "__main__":
    printtable()
