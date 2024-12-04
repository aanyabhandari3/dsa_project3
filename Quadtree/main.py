"""main.py: DSA Project 3 - Implementation testing."""

__author__ = "Preston Hemmy"
__version__ = "3.0"

from point import Point
from bounding_box import BoundingBox
from quadtree import Quadtree

# Temp function (TESTING)
def print_tree(node, level=0):
        indent = "  " * level
        if node.is_leaf():
            print(f"{indent}Leaf: ")
            for p in node.points:
                new_indent = indent + " "
                print(f"{new_indent}({p.x}, {p.y}) ")

        else:
            print(f"{indent}Node: ({node.bbox.x}, {node.bbox.y}, {node.bbox.width}, {node.bbox.height})")
            print_tree(node.nw, level + 1)
            print_tree(node.ne, level + 1)
            print_tree(node.sw, level + 1)
            print_tree(node.se, level + 1)

def main():
    bounds = BoundingBox(0, 0, 128, 128)
    tree = Quadtree(bounds)

    points = [
        Point(40, 40),
        Point(120, 100),
        Point(105, 20),
        Point(20, 60),
        Point(80, 90),
        Point(50, 10),
        Point(100, 80),
        Point(30, 30),
        Point(5,30),
    ]

    # test insert
    for point in points:
        tree.insert(point)

    print("Quadtree structure:")
    print_tree(tree.root)

    # test search
    search_point = Point(20, 60)
    found_point = tree.search(search_point)
    print(f"\nSearch for point ({search_point.x}, {search_point.y})")
    if found_point:
        print("Point found!")
    else:
        print("Point not found.")

    # test delete  
    print(f"\nDeleting point ({search_point.x}, {search_point.y})")
    tree.delete(search_point)
    print("\nUpdated Quadtree structure:")
    print_tree(tree.root)

    # test search after delete
    found_point = tree.search(search_point)
    print(f"\nSearch again for point ({search_point.x}, {search_point.y})")
    if found_point:
        print("Point found!")
    else:  
        print("Point not found.")

if __name__ == "__main__":
    main()