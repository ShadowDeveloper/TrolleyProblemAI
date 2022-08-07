class Human:
    def __init__(self, gender, age, type):
        self.gender = gender
        self.age = age
        self.type = type

    def format(self):
        return f"A(n) {self.age} year old {self.gender} {self.type}"