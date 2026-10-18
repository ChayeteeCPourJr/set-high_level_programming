import shutil

PATH = "models/rectangle.py"
shutil.copy(PATH, PATH + ".bak")
text = open(PATH).read()

old = '''    def display(self):
        """Print the Rectangle using the # character."""
        for _ in range(self.height):
            print("#" * self.width)
'''
new = '''    def display(self):
        """Print the Rectangle using the # character, honoring x and y."""
        print("\\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
'''
if text.count(old) != 1:
    raise SystemExit("display() not found in the expected form - "
                     "nothing changed")
open(PATH, "w").write(text.replace(old, new))
print("display() updated")
