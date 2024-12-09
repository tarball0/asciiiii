from PIL import Image


# map pixel sum range to char and return
def getchar(pixel_sum):
    ranges = [
        (0, 0, "#"),
        (1, 100, "X"),
        (100, 200, "%"),
        (200, 300, "&"),
        (300, 400, "*"),
        (400, 500, "+"),
        (500, 600, "/"),
        (600, 700, "("),
        (700, 750, "'"),
        (750, float("inf"), " "),
    ]
    for start, end, char in ranges:
        if start <= pixel_sum < end:
            return char

    return " "


def converter(image, scale=4, save=False):
    img = Image.open(image)
    w, h = img.size
    w //= scale
    h //= scale

    pix = img.resize((w, h))

    grid = []
    for i in range(h):
        grid.append(["X"] * w)

    pix = pix.load()
    for y in range(h):
        for x in range(w):
            pixsum = sum(pix[x, y])
            grid[y][x] = getchar(pixsum)

    if save:
        art = open("output/output.txt", "w")
        for row in grid:
            art.write("".join(row) + "\n")
        art.close()
    else:
        for row in grid:
            print("".join(row))


if __name__ == "__main__":
    converter("test-images/fahimvillageboi.jpg", save=True)
