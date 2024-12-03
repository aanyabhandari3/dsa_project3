"""main_window.py: DSA Project 3 - GUI main window file."""

__author__ = "Preston Hemmy"
__version__ = "1.0"

import tkinter as tk
from GUI.data_filters import DataFilters
from GUI.map_view import MapView

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bird Migration Spation Indexing")
        self.geometry("800x600")

        self.data_filters = DataFilters(self, on_filter_change=self.handle_filter_change)
        self.map_view = MapView(self)
        self.search_entry = None

        self.create_widgets()

    """
    Creates wireframe window visual
    @param void
    @return void
    """
    def create_widgets(self):
        # map view
        map_frame = tk.Frame(self, bg="white", width=600, height=400)
        map_frame.pack(pady=20)
        self.map_view.pack(in_=map_frame)

        # filters
        filter_frame = tk.Frame(self)
        filter_frame.pack(pady=10)
        filter_label = tk.Label(filter_frame, text="Data Filters")
        filter_label.pack()
        self.data_filters.pack(pady=10)

        # search bar
        search_frame = tk.Frame(self)
        search_frame.pack(pady=10)
        search_label = tk.Label(search_frame, text="Search:")
        search_label.pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side=tk.LEFT)
        search_button = tk.Button(search_frame, text="Search", command=self.handle_search)
        search_button.pack(side=tk.LEFT)

    """
    Handles user search button interaction
    @param void
    @return void
    """
    def handle_search(self):
        query = self.search_entry.get()
        selected_species = self.data_filters.get_selected_species()
        selected_locations = self.data_filters.get_selected_locations()
        
        if query or selected_species or selected_locations:
            filtered_data = self.filter_data(query=query, species=selected_species, locations=selected_locations)
            self.map_view.update_data_points(filtered_data)

    """
    Handles user filter "Apply Filters" button interaction
    @param void
    @return void
    """
    def handle_filter_change(self):
        selected_species = self.data_filters.get_selected_species()
        selected_locations = self.data_filters.get_selected_locations()
        filtered_data = self.filter_data(species=selected_species, locations=selected_locations)
        self.map_view.update_data_points(filtered_data)

    """
    Filter data based on user specified criteria (switch Quadtree to B-Tree implementation and vice versa)
    @param query "keyword/phrase" to filter
    @param species to filter
    @param locations to filter
    @return list of filtered data
    """
    def filter_data(self, query=None, species=None, locations=None):
        # TODO. Implement the actual filtering logic based on the selected indexing method (quadtree or B-tree)
        # For now, return dummy data
        filtered_data = []
        # Placeholder code for demonstration purposes
        if query:
            filtered_data.append(f"Filtered by query: {query}")
        if species:
            filtered_data.append(f"Filtered by species: {species}")
        if locations:
            filtered_data.append(f"Filtered by locations: {locations}")
        return filtered_data
