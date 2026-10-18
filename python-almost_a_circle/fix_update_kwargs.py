import shutil

PATH = "models/rectangle.py"
shutil.copy(PATH, PATH + ".bak")
text = open(PATH).read()

old = '''    def update(self, *args):
        """Assign each positional argument to an attribute, in order.

        Args:
            *args (ints): New attribute values, in this order:
                - 1st argument is the id attribute
                - 2nd argument is the width attribute
                - 3rd argument is the height attribute
                - 4th argument is the x attribute
                - 5th argument is the y attribute
        """
        attributes = ["id", "width", "height", "x", "y"]
        for attribute, value in zip(attributes, args):
            setattr(self, attribute, value)
'''
new = '''    def update(self, *args, **kwargs):
        """Assign new values to the attributes of the Rectangle.

        If args is not empty, kwargs is skipped.

        Args:
            *args (ints): New attribute values, in this order:
                - 1st argument is the id attribute
                - 2nd argument is the width attribute
                - 3rd argument is the height attribute
                - 4th argument is the x attribute
                - 5th argument is the y attribute
            **kwargs (dict): New key/value pairs of attributes, in any
                order. Keys that are not attributes are ignored.
        """
        attributes = ("id", "width", "height", "x", "y")
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
'''
if text.count(old) != 1:
    raise SystemExit("update(self, *args) not found in the expected form - "
                     "nothing changed")
open(PATH, "w").write(text.replace(old, new))
print("update() updated")
