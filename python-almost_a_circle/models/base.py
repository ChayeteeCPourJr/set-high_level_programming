
#!/usr/bin/python3
"""Defines the Base class."""

import json
import csv

class Base:
    """Manage the id attribute for all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle."""
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
            objects = [shape for shape, _ in shapes]
            cx = (
                min(obj.x for obj in objects)
                + max(obj.x + obj.width for obj in objects)
            ) / 2
            cy = (
                min(obj.y for obj in objects)
                + max(obj.y + obj.height for obj in objects)
            ) / 2

        warm = [
            ("#c0392b", "#f5b7b1"),
            ("#d35400", "#fad7a0"),
            ("#b7950b", "#f9e79f"),
        ]
        cool = [
            ("#1f618d", "#aed6f1"),
            ("#117a65", "#a3e4d7"),
            ("#6c3483", "#d7bde2"),
        ]
        counts = {True: 0, False: 0}

        for shape, is_rectangle in shapes:
            palette = warm if is_rectangle else cool
            outline, fill = palette[
                counts[is_rectangle] % len(palette)
            ]
            counts[is_rectangle] += 1

            turtle.penup()
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


    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of objects to a file."""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dictionaries = cls.from_json_string(json_string)

        return [cls.create(**dictionary)
                for dictionary in list_dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save objects to a CSV file."""
        filename = cls.__name__ + ".csv"

        if list_objs is None:
            list_objs = []

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([
                        obj.id, obj.width, obj.height, obj.x, obj.y
                    ])
                elif cls.__name__ == "Square":
                    writer.writerow([
                        obj.id, obj.size, obj.x, obj.y
                    ])

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file."""
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                if cls.__name__ == "Rectangle":
                    return [
                        cls.create(
                            id=int(row[0]),
                            width=int(row[1]),
                            height=int(row[2]),
                            x=int(row[3]),
                            y=int(row[4])
                        )
                        for row in reader
                    ]

                elif cls.__name__ == "Square":
                    return [
                        cls.create(
                            id=int(row[0]),
                            size=int(row[1]),
                            x=int(row[2]),
                            y=int(row[3])
                        )
                        for row in reader
                    ]

                return []
        except FileNotFoundError:
            return []
