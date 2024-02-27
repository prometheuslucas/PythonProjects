from PIL import Image, ImageDraw

def create_image(colors, resolution):
    if resolution % 3 != 0:
        raise ValueError("Resolution must be a multiple of three.")

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
            draw.rectangle([j*square_size, i*square_size, (j+1)*square_size, (i+1)*square_size], color_map[color])

    img.save('output.png')

try:
    create_image(['BGB', 'BGB', 'BGB', 'BGB'], 300)
except ValueError as e:
    print(e)