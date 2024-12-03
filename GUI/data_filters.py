"""data_filters.py: DSA Project 3 - Data filter and search functionality."""

__author__ = "Preston Hemmy"
__version__ = "1.0"

import tkinter as tk

class DataFilters(tk.Frame):
    def __init__(self, parent, on_filter_change):
        super().__init__(parent)
        self.on_filter_change = on_filter_change

        self.species_var = tk.StringVar()
        self.location_var = tk.StringVar()

        filter_frame = tk.Frame(self)
        filter_frame.pack(side=tk.TOP, padx=10, pady=10)

        species_label = tk.Label(self, text="Species:")
        species_label.pack(side=tk.LEFT)
        species_entry = tk.Entry(self, textvariable=self.species_var)
        species_entry.pack(side=tk.LEFT)

        location_label = tk.Label(self, text="Location:")
        location_label.pack(side=tk.LEFT)
        location_entry = tk.Entry(self, textvariable=self.location_var)
        location_entry.pack(side=tk.LEFT)

        apply_button = tk.Button(self, text="Apply Filters", command=self.apply_filters)
        apply_button.pack(side=tk.LEFT)

    def apply_filters(self):
        self.on_filter_change()

    def get_selected_species(self):
        return self.species_var.get()
    
    def get_selected_locations(self):
        return self.location_var.get()