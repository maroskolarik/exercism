import random, string


class Robot:
    names = set()

    def __init__(self):
        self.name = self.generate_name()

    def reset(self):
        self.name = self.generate_name()

    def generate_name(self):
        while True:
            name = ''.join(random.choices(string.ascii_uppercase, k=2)) + \
                   ''.join(random.choices(string.digits, k=3))
            if name not in Robot.names:
                Robot.names.add(name)
                return name

