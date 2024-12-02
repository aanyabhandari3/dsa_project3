"""point.py: DSA Project 3 - Quadtree coordinate system."""

__author__ = "Preston Hemmy"
__version__ = "1.0"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

        return False

    def __hash__(self):
        return hash((self.x, self.y))