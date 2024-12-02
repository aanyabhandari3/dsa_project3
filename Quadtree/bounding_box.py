"""bounding_box.py: DSA Project 3 - Quadtree 2D bounding box for x-y pairs."""

__author__ = "Preston Hemmy"
__version__ = "1.0"

from point import Point

class BoundingBox:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    """
    Determine if given point is in the bounding box
    @param point: x-y Point point
    @return bool: point is/is not within bounds
    """
    def contains(self, point):
        return (
            self.x <= point.x < self.x + self.width
            and self.y <= point.y < self.y + self.height
        )
    
    """
    Determine if given given bouding box overlaps with another bounding box
    @param other: BoundingBox to compare to
    @return bool: overlap exists
    """
    def intersects(self, other):
        return (
            other.x < self.x + self.width
            or other.x + other.width > self.x
            or other.y < self.y + self.height
            or other.y + other.height > self.y
        )

    """
    Divides the 2D space along its horizontal and vertical midpoints, respectively
    @param void
    @return list: four new bounding boxes from subdivision
    """
    def subdivide(self):
        half_width = self.width // 2
        half_height = self.height // 2

        return [
            BoundingBox(self.x, self.y, half_width, half_height),
            BoundingBox(self.x + half_width, self.y, half_width, half_height),
            BoundingBox(self.x, self.y + half_height, half_width, half_height),
            BoundingBox(self.x + half_width, self.y + half_height, half_width, half_height)
        ]