import os
import webbrowser
from canvas import Canvas
from shapes import Rectangle, Square


def form_color():
    """Ask for user color inputs and form into an RGB Python list."""
    red = int(input("[COLOR SELECT] Choose the red RGB value (0-255): "))
    blue = int(input("[COLOR SELECT] Choose the blue RGB value (0-255): "))
    green = int(input("[COLOR SELECT] Choose the green RGB value (0-255): "))
    return [red, blue, green]


def select_position():
    """Ask for user position inputs and returns an x, y tuple."""
    x_pos = int(input("[POSITION] Choose the vertical starting position (from top): "))
    y_pos = int(input("[POSITION] Choose the horizontal starting position (from left): "))
    return x_pos, y_pos


print("Welcome to the Math Draw Interface!")
print("-----------------------------------")

# Get canvas dimensions and background color from user
width = int(input("[CANVAS DIMENSIONS] Choose a positive integer for background width: "))
height = int(input("[CANVAS DIMENSIONS] Choose a positive integer for background height: "))
color = form_color()
canvas = Canvas(width, height, color)

# Main event loop for drawing shapes
while True:
    shape_type = input('[SHAPE SELECT] Choose to draw a "square" or "rectangle": ')
    # Draw rectangle
    if shape_type.lower() == "rectangle":
        x, y = select_position()
        height = int(input("[DIMENSIONS] Choose the vertical height (going downward): "))
        width = int(input("[DIMENSIONS] Choose the horizontal width (going right): "))
        color = form_color()
        print(f"[DRAWING] Drawing a {color} rectangle with dimensions ({x}, {y}) ; ({x + height}, {y + width}).")
        Rectangle(x, y, height, width, color).draw(canvas)
    # Draw square
    elif shape_type.lower() == "square":
        x, y = select_position()
        side = int(input("[DIMENSIONS] Choose the square side length (going down, right): "))
        color = form_color()
        print(f"[DRAWING] Drawing a {color} square with dimensions ({x}, {y}) ; ({x + side}, {y + side}).")
        Square(x, y, side, color).draw(canvas)
    # Error handling
    else:
        print("[ERROR] Sorry, you either misspelled or entered an invalid shape. Please try again.")
        continue
    # Continue drawing or save file
    draw_more = input('[CONTINUE] Draw more shapes? ("yes" or "no"): ')
    if (draw_more.lower() == "no") or (draw_more.lower() == "n"):
        file_name = input("[SAVE] What would you like to name your photo?: ")
        os.chdir("images")
        canvas.make(f"{file_name}.png")
        break

print("Thanks for drawing with me! See you later!")
