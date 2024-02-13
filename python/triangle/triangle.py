def equilateral(sides):
    if is_triangle(sides):
        if sides[0] == sides[1]:
            if sides[0] == sides[2]:
                if sides[1] == sides[2]:
                    return True
    return False


def isosceles(sides):
    if is_triangle(sides):
        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return True
    return False


def scalene(sides):
    if is_triangle(sides):
        if sides[0] != sides[1]:
            if sides[0] != sides[2]:
                if sides[1] != sides[2]:
                    return True
    return False


def is_triangle(sides):
    if sides[0] or sides[1] or sides[2] > 1:
        if sides[0] + sides[1] >= sides[2]:
            if sides[1] + sides[2] >= sides[0]:
                if sides[0] + sides[2] >= sides[1]:
                    return True
    return False
