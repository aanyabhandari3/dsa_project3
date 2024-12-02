"""node.py: DSA Project 3 - Quadtree node class, where nodes can be either empty, storing data, or storing a quadtree."""

__author__ = "Preston Hemmy"
__version__ = "1.0"

from bounding_box import BoundingBox

class Node:
    def __init__(self, bbox, capacity=4):       # Note: default capacity negotiable
        self.bbox = bbox
        self.capacity = capacity
        self.points = set()
        self.divided = False
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None

    def is_leaf(self):
        return not self.divided
    
    """
    Divides current node (now parent) into four new nodes (nw, ne, sw, se children)
    @param void
    @return void
    """
    def subdivide(self):
         quadrants = self.bbox.subdivide()
         self.nw = Node(quadrants[0], self.capacity)
         self.ne = Node(quadrants[1], self.capacity)
         self.sw = Node(quadrants[2], self.capacity)
         self.se = Node(quadrants[3], self.capacity)
         self.divided = True

    """
    Inserts point data into node, subdividing when current node is at max capacity
    @param point: x-y Point pair
    @return bool: successful insertion
    """
    def insert(self, point):
        if not self.bbox.contains(point):
            return False
        
        # if current node is not at capacity then add point
        if len(self.points) < self.capacity:
            self.points.add(point)
            return True
        
        if not self.divided:
            self.subdivide()
        
        # recursively check children
        if self.nw.insert(point):
             return True
        if self.ne.insert(point):
             return True
        if self.sw.insert(point):
             return True
        if self.se.insert(point):
             return True
        
        return False

# Flyweight class inherits Node class (used for any empty node)
class Flyweight(Node):
        def __init__(self):
            super().__init__(None)