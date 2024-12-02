"""quadtree.py: DSA Project 3 - Quadtree class."""

__author__ = "Preston Hemmy"
__version__ = "1.0"

from node import Node, Flyweight

class Quadtree:
    def __init__(self, bbox):
        self.root = Node(bbox)
        self.flyweight = Flyweight()

    """
    Insert given x-y coordinate into tree
    @param point: x-y coordinate point
    @return void
    """
    def insert(self, point):
        # check bounds
        if not self.root.bbox.contains(point):
            return False
    
        # traversal
        node = self.root
        while not node.is_leaf():
            if node.nw.bbox.contains(point):
                node = node.nw
            elif node.ne.bbox.contains(point):
                node = node.ne
            elif node.sw.bbox.contains(point):
                node = node.sw
            else:
                node = node.se
        
        # if not full, then add Point data
        if len(node.points) < node.capacity:
            node.points.add(point)
            return True
        
        # redistribute previously stored points
        node.subdivide()
        for pt in node.points:
            if node.nw.bbox.contains(pt):
                node.nw.insert(pt)
            elif node.ne.bbox.contains(pt):
                node.ne.insert(pt)
            elif node.sw.bbox.contains(pt):
                node.sw.insert(pt)
            else:
                node.se.insert(pt)

        node.points.clear()

        # insert the new point
        if node.nw.bbox.contains(point):
            node.nw.insert(point)
        elif node.ne.bbox.contains(point):
            node.ne.insert(point)
        elif node.sw.bbox.contains(point):
            node.sw.insert(point)
        else:
            node.se.insert(point)

        return True

    """
    Search for given x-y coordinate in tree
    @param point: x-y coordinate point
    @return void (returns <...> if point not found)
    """
    def search(self, point):
        # Todo

        pass

    """
    Delete given x-y coordinate from tree
    @param point: x-y coordinate point
    @return void (returns <...> if point not found)
    """
    def delete(self,point):
        # Todo

        pass