#!/usr/bin/python3
"""Defines a base model class."""


class Base:
    """Represents the base model.

    This Base class manages the id attribute of all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all the Rectangles and Squares.

        The shapes are placed with the same x/y offsets as when they are
        displayed, with the origin at the top-left corner of the drawing.
        Rectangles are drawn in warm colors and squares in cool colors.
        Click the window to close it.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        # Imported here so that a missing tkinter only affects draw().
        import turtle

        shapes = [(r, True) for r in list_rectangles]
        shapes += [(s, False) for s in list_squares]

        screen = turtle.Screen()
        screen.title("Rectangles and Squares")
        screen.bgcolor("#f5f5f0")
        turtle.hideturtle()
        turtle.speed(0)
        turtle.pensize(3)
        turtle.tracer(0)

        if shapes:
            # Center the whole drawing in the window.
            objs = [shape for shape, _ in shapes]
            cx = (min(o.x for o in objs) +
                  max(o.x + o.width for o in objs)) / 2
            cy = (min(o.y for o in objs) +
                  max(o.y + o.height for o in objs)) / 2

        warm = [("#c0392b", "#f5b7b1"), ("#d35400", "#fad7a0"),
                ("#b7950b", "#f9e79f")]
        cool = [("#1f618d", "#aed6f1"), ("#117a65", "#a3e4d7"),
                ("#6c3483", "#d7bde2")]
        counts = {True: 0, False: 0}

        for shape, is_rectangle in shapes:
            palette = warm if is_rectangle else cool
            outline, fill = palette[counts[is_rectangle] % len(palette)]
            counts[is_rectangle] += 1

            turtle.penup()
            # Turtle's y axis points up, the display's y axis points down.
            turtle.goto(shape.x - cx, cy - shape.y)
            turtle.setheading(0)
            turtle.color(outline, fill)
            turtle.pendown()
            turtle.begin_fill()
            for side in (shape.width, shape.height) * 2:
                turtle.forward(side)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()

        turtle.update()
        screen.exitonclick()
