"""main.py: DSA Project 3 - Implementation testing."""

__author__ = "Preston Hemmy"
__version__ = "3.0"

from GUI.main_window import MainWindow

def main():
    window = MainWindow()
    window.mainloop()

if __name__ == "__main__":
    main()











# QUAD TREE TESTING
# from point import Point
# from bounding_box import BoundingBox
# from quadtree import Quadtree

# # Temp function (TESTING)
# def print_tree(node, level=0):
#         indent = "  " * level
#         if node.is_leaf():
#             print(f"{indent}Leaf: ")
#             for p in node.points:
#                 new_indent = indent + " "
#                 print(f"{new_indent}({p.x}, {p.y}) ")

#         else:
#             print(f"{indent}Node: ({node.bbox.x}, {node.bbox.y}, {node.bbox.width}, {node.bbox.height})")
#             print_tree(node.nw, level + 1)
#             print_tree(node.ne, level + 1)
#             print_tree(node.sw, level + 1)
#             print_tree(node.se, level + 1)

# def main():
#     bounds = BoundingBox(0, 0, 128, 128)
#     tree = Quadtree(bounds)

#     points = [
#         Point(40, 40),
#         Point(120, 100),
#         Point(105, 20),
#         Point(20, 60),
#         Point(80, 90),
#         Point(50, 10),
#         Point(100, 80),
#         Point(30, 30),
#         Point(5,30),
#     ]

#     for point in points:
#         tree.insert(point)

#     print("Quadtree structure:")
#     print_tree(tree.root)

# if __name__ == "__main__":
#     main()