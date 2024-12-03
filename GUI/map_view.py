"""map_view.py: DSA Project 3 - Map view implementation."""

__author__ = "Preston Hemmy"
__version__ = "1.0"

import tkintermapview
import tkinter as tk

class MapView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.map_widget = tkintermapview.TkinterMapView(self, width=600, height=400, corner_radius=0)
        self.map_widget.set_position(37.7749, -122.4194)
        self.map_widget.set_zoom(4)
        self.map_widget.pack()

    def create_map(self):
        self.map = folium.Map(location=[37.7749, -122.4194], zoom_start=4)

    """
    Update map to display data points of form (latitude, longitude, species)
    @param data_points: already filtered
    @return void
    """
    def update_data_points(self, data_points):
        self.map_widget.delete_all_marker()
        for point in data_points:
            # Assuming data_points is a list of tuples (latitude, longitude, species)
            self.map_widget.set_marker(point[0], point[1], text=point[2])