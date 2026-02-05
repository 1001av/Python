class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks   # notice the underscore, it's a "hidden" variable

    @property
    def grade(self):
        # grade is calculated based on marks
        if self._marks >= 90:
            return "A"
        elif self._marks >= 75:
            return "B"
        else:
            return "C"

# Using the class
s = Student("Akhil", 85)

print(s.name)      # normal attribute
print(s.grade)     # looks like an attribute, but actually calls the method
