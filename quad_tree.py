import pandas as pd
import matplotlib.pyplot as plt

class Point:
    #2D-space
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Rectangle:
    #bounding box
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains(self, point):
        #check if in rectangle
        return (self.x <= point.x < self.x + self.width and
                self.y <= point.y < self.y + self.height)

    def intersects(self, other):
        #check if intersection
        return not (self.x + self.width <= other.x or
                    other.x + other.width <= self.x or
                    self.y + self.height <= other.y or
                    other.y + other.height <= self.y)


class QuadTree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary  # Rectangle defining this node's boundary
        self.capacity = capacity  # Max points before subdivision
        self.points = []          # Points in this node
        self.divided = False      # Whether this node has been subdivided

    def subdivide(self):
        #four-quadrant division
        x, y, w, h = self.boundary.x, self.boundary.y, self.boundary.width, self.boundary.height
        nw = Rectangle(x, y, w / 2, h / 2)
        ne = Rectangle(x + w / 2, y, w / 2, h / 2)
        sw = Rectangle(x, y + h / 2, w / 2, h / 2)
        se = Rectangle(x + w / 2, y + h / 2, w / 2, h / 2)

        self.northwest = QuadTree(nw, self.capacity)
        self.northeast = QuadTree(ne, self.capacity)
        self.southwest = QuadTree(sw, self.capacity)
        self.southeast = QuadTree(se, self.capacity)

        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return False  # Point is out of bounds

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True

        if not self.divided:
            self.subdivide()

        return (self.northwest.insert(point) or
                self.northeast.insert(point) or
                self.southwest.insert(point) or
                self.southeast.insert(point))

    def query(self, range_rect, found=None):
        if found is None:
            found = []

        if not self.boundary.intersects(range_rect):
            return found  # If range does not intersect this node's boundary, skip

        for point in self.points:
            if range_rect.contains(point):
                found.append(point)

        if self.divided:
            self.northwest.query(range_rect, found)
            self.northeast.query(range_rect, found)
            self.southwest.query(range_rect, found)
            self.southeast.query(range_rect, found)

        return found

    def __repr__(self):
        return f"QuadTree(boundary={self.boundary}, points={self.points}, divided={self.divided})"

    def visualize(self, ax=None):
        if ax is None:
            _, ax = plt.subplots(figsize=(12, 8))
        
        # Draw the boundary of the current QuadTree node
        rect = plt.Rectangle((self.boundary.x, self.boundary.y),
                              self.boundary.width, self.boundary.height,
                              edgecolor='blue', fill=False)
        ax.add_patch(rect)

        # Plot the points in the current node
        for point in self.points:
            ax.plot(point.x, point.y, 'ro', markersize=2)

        # Recursively visualize child nodes if divided
        if self.divided:
            self.northwest.visualize(ax)
            self.northeast.visualize(ax)
            self.southwest.visualize(ax)
            self.southeast.visualize(ax)

        return ax

#load data from a CSV file and populate the QuadTree
def load_data_to_quadtree(csv_file, quadtree):
    data = pd.read_csv(csv_file)
    if 'longitude' not in data.columns or 'latitude' not in data.columns:
        raise ValueError("CSV must contain 'longitude' and 'latitude' columns")

    for _, row in data.iterrows():
        point = Point(row['longitude'], row['latitude'])
        quadtree.insert(point)


if __name__ == "__main__":
    boundary = Rectangle(-180, -90, 360, 180)  # Covers the entire world in lat/lon
    qt = QuadTree(boundary, 20)

    csv_file = "Bird_Data_Parsed.csv"
    load_data_to_quadtree(csv_file, qt)

    ax = qt.visualize()
    plt.title("QuadTree Visualization")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

    print("QuadTree structure after loading data:", qt)

    search_area = Rectangle(-50, -25, 50, 50)
    found_points = qt.query(search_area)
    print(f"Points in range {search_area}: {found_points}")

# if __name__ == "__main__":
#     # Define the boundary of the QuadTree
#     boundary = Rectangle(-180, -90, 360, 180)  # Covers the entire world in lat/lon
#     qt = QuadTree(boundary, 4)

#     # Simulate data points instead of loading from a CSV file
#     test_points = [
#         Point(-100, 50), Point(-110, 60), Point(-120, 70), Point(-130, 80),
#         Point(-80, 30), Point(-90, 40), Point(-140, 85), Point(10, 20),
#         Point(30, 40), Point(50, 60), Point(70, 80), Point(90, 100),
#         Point(-50, -40), Point(-40, -30), Point(-30, -20), Point(-20, -10)
#     ]

#     # Insert the test points into the QuadTree
#     for point in test_points:
        # qt.insert(point)

    # Visualize the QuadTree structure
    # ax = qt.visualize()
    # plt.title("QuadTree Visualization with Test Points")
    # plt.xlabel("Longitude")
    # plt.ylabel("Latitude")
    # plt.show()

    # # Display the QuadTree structure
    # print("QuadTree structure after inserting test points:")
    # print(qt)

    # Define a search area and query points within it
    # search_area = Rectangle(-50, -25, 100, 100)
    # found_points = qt.query(search_area)
    # print(f"Points in range {search_area}: {found_points}")

