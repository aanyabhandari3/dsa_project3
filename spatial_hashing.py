import csv
from collections import defaultdict
import math

class SpatialHash:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.grid = defaultdict(list)

    def hash(self, lat, lon):
        return (
            math.floor(lat / self.cell_size),
            math.floor(lon / self.cell_size)
        )

    def insert(self, lat, lon, data):
        cell = self.hash(lat, lon)
        self.grid[cell].append((lat, lon, data))

    def query(self, lat, lon, radius):
        results = []
        cell = self.hash(lat, lon)
        # Convert radius to cell units
        cell_radius = math.ceil(radius / (self.cell_size * 111))  # Approx. km per degree
        for dx in range(-cell_radius, cell_radius + 1):
            for dy in range(-cell_radius, cell_radius + 1):
                neighbor_cell = (cell[0] + dx, cell[1] + dy)
                for point in self.grid.get(neighbor_cell, []):  # Safely handle missing cells
                    if self.haversine_distance(lat, lon, point[0], point[1]) <= radius:
                        results.append(point)
        return results

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        R = 6371.0  # Earth's radius in kilometers
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c


def load_data_from_csv(filename, spatial_hash):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                lon = float(row['longitude']) 
                lat = float(row['latitude']) 
                spatial_hash.insert(lat, lon, row)
            except (ValueError, KeyError) as e:
                print(f"Skipping invalid row: {row}. Error: {e}")


import matplotlib.pyplot as plt
import time

def incremental_plot(data, chunk_size=1000, delay=0.1):
    fig, ax = plt.subplots()
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        latitudes = [p[0] for p in chunk]
        longitudes = [p[1] for p in chunk]
        ax.scatter(longitudes, latitudes, s=1, alpha=0.5, color='blue')
        plt.pause(delay)
    plt.show()


# Usage
spatial_hash = SpatialHash(cell_size=0.1)  # Adjust cell_size as needed
load_data_from_csv('Bird_Data_Parsed.csv', spatial_hash)

# Query the SpatialHash for a specific location and radius
query_lat, query_lon, query_radius = 45.759891, 7.548206, 5000  # Query at one of the points
results = spatial_hash.query(query_lat, query_lon, query_radius)

# Display the results
print("Query Results:")
for result in results:
    print(result)

# Convert data to list and call the function
data = [p for points in spatial_hash.grid.values() for p in points]
incremental_plot(data, chunk_size=5000)


