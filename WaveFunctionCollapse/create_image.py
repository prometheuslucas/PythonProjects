from PIL import Image, ImageDraw
import os


RES = 18
TILES = "tiles"
PATH = f"./{TILES}/res_{RES}/"

def create_image(colors, resolution, name):
    if resolution % 3 != 0:
        raise ValueError("Resolution must be a multiple of three.")

    if not os.path.exists(PATH):
        os.makedirs(PATH)

    img = Image.new('RGB', (resolution, resolution))
    draw = ImageDraw.Draw(img)

    square_size = resolution // 3
    color_map = {'B': (0, 0, 0), 'G': (0, 255, 0)}

    # Draw squares
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # middle square is always green
                color = 'G'
            elif i == 0:  # top row
                color = colors[3][j]
            elif i == 2:  # bottom row
                color = colors[1][j]
            elif j == 0:  # left column
                color = colors[2][i]
            else:  # right column
                color = colors[0][i]
            draw.rectangle((j*square_size, i*square_size, (j+1)*square_size, (i+1)*square_size), color_map[color])

    img.save(f"{PATH}{name}.png")


PATH_METADATA = f"./metadata.txt"
metadata = []
with open(PATH_METADATA, "r") as file:
    file = file.readlines()
    for line in file:
        line = line.strip().split("\t")
        if line[5] == "0":
            metaEntry = {
                "ID": line[0],
                "SOCKETS": [line[1], line[2], line[3], line[4]],
                "FIXED": False,
                "ROTATION": 0
            }
            create_image(metaEntry["SOCKETS"], RES, metaEntry["ID"])
        else:
            print("Fixed tile found, skipping...")
