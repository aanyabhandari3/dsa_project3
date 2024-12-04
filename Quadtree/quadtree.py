"""quadtree.py: DSA Project 3 - Quadtree class."""

__author__ = "Preston Hemmy"
__version__ = "2.0"

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
    @return point is found o.w. None
    """
    def search(self, point):
        # check bounds
        if not self.root.bbox.contains(point):
            return None
    
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

        # check if found
        if point in node.points:
            return point
        
        return None

    """
    Delete given x-y coordinate from quadtree
    @param point: x-y coordinate point
    @return bool indicating successful removal from quadtree
    """
    def delete(self,point):
        # check bounds
        if not self.root.bbox.contains(point):
            return False
    
        # traversal
        node = self.root
        parent = None
        while not node.is_leaf():
            parent = node                       # track parent
            if node.nw.bbox.contains(point):
                node = node.nw
            elif node.ne.bbox.contains(point):
                node = node.ne
            elif node.sw.bbox.contains(point):
                node = node.sw
            else:
                node = node.se

        # check if found
        if point in node.points:
            node.points.remove(point)

            # if parent contains less leaf nodes than capacity, then merge leaf nodes
            while parent is not None:
                if len(parent.nw.points) + len(parent.ne.points) + len(parent.sw.points) + len(parent.se.points) <= parent.capacity:
                    parent.points = parent.nw.points | parent.ne.points | parent.sw.points | parent.se.points
                    parent.nw = parent.ne = parent.sw = parent.se = self.flyweight
                    parent.divided = False
                    node = parent
                    parent = None
                else:
                    break

            return True

        return False