"""main_window.py: DSA Project 3 - GUI main window file."""

__author__ = "Preston Hemmy"
__version__ = "1.0"

import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bird Migration Spation Indexing")
        self.geometry("800x600")

        self.search_entry = None                # search field
        self.performance_comparison = None      # dict
        self.summary_label = None               # summary text

        self.create_widgets()

    def create_widgets(self):
        # search bar
        search_frame = tk.Frame(self)
        search_frame.pack(pady=10)
        search_label = tk.Label(search_frame, text="Number of data points:")
        search_label.pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame, width=10)
        self.search_entry.pack(side=tk.LEFT)
        search_button = tk.Button(search_frame, text="Run Benchmark", command=self.handle_search)
        search_button.pack(side=tk.LEFT)

        # comparison section
        comparison_frame = ttk.LabelFrame(self, text="Performance Comparison")
        comparison_frame.pack(pady=10)

        comparison_table = ttk.Treeview(comparison_frame, columns=("quadtree", "spatial_hashing"), show="headings")
        comparison_table.heading("quadtree", text="Quadtree")
        comparison_table.heading("spatial_hashing", text="Spatial Hashing")
        comparison_table.insert("", "end", values=("", ""), tags=("insert",))
        comparison_table.insert("", "end", values=("", ""), tags=("search",))
        comparison_table.insert("", "end", values=("", ""), tags=("delete",))
        comparison_table.pack()

        self.performance_comparison = comparison_table

        # summary section
        summary_frame = ttk.LabelFrame(self, text="Summary")
        summary_frame.pack(pady=10)

        self.summary_label = tk.Label(summary_frame, text="", justify=tk.LEFT)
        self.summary_label.pack()

    """
    Handles user search button interaction
    @param void
    @return void
    """
    def handle_search(self):
        num_points = self.search_entry.get()
        if num_points.isdigit():
            num_points = int(num_points)
            self.run_benchmark(num_points)
        else:
            print("Invalid input. Please enter a valid number of data points.")

    """
    Calculate and display benchmarks
    @param num_points to run through benchmark test
    @return void
    """
    def run_benchmark(self, num_points):
        # TODO. Implement benchmark logic for quadtree and spatial hashing
        # Update the performance comparison table with the benchmark results
        quadtree_insert_time = 0.5
        spatial_hashing_insert_time = 0.3
        quadtree_search_time = 0.2
        spatial_hashing_search_time = 0.1
        quadtree_delete_time = 0.4
        spatial_hashing_delete_time = 0.2

        self.performance_comparison.item(self.performance_comparison.get_children()[0], values=(quadtree_insert_time, spatial_hashing_insert_time))
        self.performance_comparison.item(self.performance_comparison.get_children()[1], values=(quadtree_search_time, spatial_hashing_search_time))
        self.performance_comparison.item(self.performance_comparison.get_children()[2], values=(quadtree_delete_time, spatial_hashing_delete_time))

        self.update_summary(quadtree_insert_time, spatial_hashing_insert_time,
                            quadtree_search_time, spatial_hashing_search_time,
                            quadtree_delete_time, spatial_hashing_delete_time)
    """
    Display benchmark results summary
    @param quadtree_insert_time, spatial_hashing_insert_time, quadtree_search_time,
            spatial_hashing_search_time, quadtree_delete_time, spatial_hashing_delete_time
    @return void
    """
    def update_summary(self, quadtree_insert_time, spatial_hashing_insert_time,
                       quadtree_search_time, spatial_hashing_search_time,
                       quadtree_delete_time, spatial_hashing_delete_time):
        insert_winner = "Quadtree" if quadtree_insert_time < spatial_hashing_insert_time else "Spatial Hashing"
        search_winner = "Quadtree" if quadtree_search_time < spatial_hashing_search_time else "Spatial Hashing"
        delete_winner = "Quadtree" if quadtree_delete_time < spatial_hashing_delete_time else "Spatial Hashing"

        summary_text = f"Insert: {insert_winner} performs better.\n"
        summary_text += f"Search: {search_winner} performs better.\n"
        summary_text += f"Delete: {delete_winner} performs better."

        self.summary_label.config(text=summary_text)

# to run uncomment:
# def main():
#     window = MainWindow()
#     window.mainloop()

# if __name__ == "__main__":
#     main()