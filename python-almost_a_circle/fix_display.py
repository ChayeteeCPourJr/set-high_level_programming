import shutil

PATH = "models/rectangle.py"
shutil.copy(PATH, PATH + ".bak")
lines = open(PATH).read().split("\n")

# Find the (last) display method and cut everything from there to the end.
starts = [i for i, line in enumerate(lines)
          if line.strip() == "def display(self):"]
if not starts:
    raise SystemExit("def display(self): not found - nothing changed")
text = "\n".join(lines[:starts[-1]]).rstrip("\n") + "\n"

text += '''
    def display(self):
        """Print the Rectangle using the # character."""
        for _ in range(self.height):
            print("#" * self.width)
'''
open(PATH, "w").write(text)
print("display() rewritten")
