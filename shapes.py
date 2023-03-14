from canvas import Canvas


class Rectangle:
    def __init__(self, x: int, y: int, height: int, width: int, color: list[int, int, int]):
        """Creates a rectangle on the provided canvas with a specified height, width, and color,
        starting at the point specified and drawing down and to the right.

        :param int x: Vertical starting position (top -> bottom)
        :param int y: Horizontal starting position (left -> right)
        :param height: Vertical height down from starting x
        :param width: Horizontal width right from starting y
        :param color: Fill color of shape e.g. [255, 255, 255]
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas: Canvas):
        """Draws the rectangle onto the canvas.

        :param Canvas canvas: Background image/canvas to be drawn on
        :return str:
        """
        canvas.data[self.x: self.x + self.height,
                    self.y: self.y + self.width] = self.color
        return f"The rectangle at {self.x}, {self.y} has been added."


class Square:
    def __init__(self, x: int, y: int, side: int, color: list[int, int, int]):
        """Creates a square on the provided canvas with a specified side length and color,
        starting at the point specified and drawing down and to the right.

        :param int x: Vertical starting position (top -> bottom)
        :param int y: Horizontal starting position (left -> right)
        :param int side: Vertical and horizontal distance starting from x and y
        :param list[int, int, int] color: Fill color of shape (e.g. [255, 255, 255])
        """
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas: Canvas):
        """Draws the square onto the canvas.

        :param canvas: Background image/canvas to be drawn on
        :return str:
        """
        canvas.data[self.x: self.x + self.side,
        self.y: self.y + self.side] = self.color
        return f"The square at {self.x}, {self.y} has been added."
