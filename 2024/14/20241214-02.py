from PIL import Image, ImageDraw, ImageFont
import re
import sys

# X, Y = 11, 7
X, Y = 101, 103

CENTER_X = (X + 1) // 2 - 1
CENTER_Y = (Y + 1) // 2 - 1

STEPS = 10000


robots = []
quadrants = [0] * 4

try:
    font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Courier New Bold.ttf", size=20
    )  # Replace with a valid monospace .ttf font (e.g., Courier)
except IOError:
    print("Monospace font not found, using default font.")
    font = ImageFont.load_default()  # Default font may not be monospace!

with open(sys.argv[1], "r") as file:
    for line in file:
        robot = {}
        for t in re.findall(r"(p|v)=(-?\d+),(-?\d+)", line):
            robot[t[0]] = (int(t[1]), int(t[2]))
        robots.append(robot)

for i in range(STEPS):
    grid = [[0] * Y for _ in range(X)]
    lines = []

    for r in robots:
        px, py = r["p"]
        dx, dy = r["v"]
        px += dx
        px %= X
        py += dy
        py %= Y
        r["p"] = px, py
        grid[px][py] = 1

    for j in range(len(grid)):
        line = "".join("#" if grid[j][k] == 1 else " " for k in range(len(grid[j])))
        lines.append(line)

    # Create a blank image with white background
    width, height = 1300, 2500  # Dimensions of the image
    image = Image.new("RGB", (width, height), "white")

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Define text position and line spacing
    x, y = 10, 10  # Starting position
    line_spacing = 5  # Space between lines

    # Write each line to the image
    for line in lines:
        # Draw the text
        draw.text((x, y), line, fill="black", font=font)

        # Calculate text height using font.getbbox()
        text_width, text_height = font.getbbox(line)[
            2:
        ]  # Get width and height of the text
        y += text_height + line_spacing  # Move down for the next line

    # Save the image to a PNG file
    image.save(f"{i}.png")

    print(f"Text has been written to {i}.png")
