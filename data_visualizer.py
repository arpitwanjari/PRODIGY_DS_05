#!/usr/bin/env python3
"""
Interactive Data Visualization Application

This application allows users to input X and Y coordinates and visualize them
in various plot types including scatter plots, line plots, and bar charts.

Author: Data Visualization App
"""

import matplotlib.pyplot as plt
import numpy as np
import sys
from typing import List, Tuple, Optional


class DataVisualizer:
    """A class for creating interactive data visualizations."""
    
    def __init__(self):
        """Initialize the DataVisualizer."""
        self.x_data = []
        self.y_data = []
        plt.style.use('default')
    
    def get_user_input(self) -> Tuple[List[float], List[float]]:
        """
        Get X and Y coordinates from user input.
        
        Returns:
            Tuple of lists containing X and Y coordinates
        """
        print("\n=== Interactive Data Visualization Application ===")
        print("Enter your data points to create a visualization.")
        print("You can enter multiple X,Y coordinate pairs.")
        print("\nInput Methods:")
        print("1. Single point: Enter X value, then Y value")
        print("2. Multiple points: Enter comma-separated values for X, then for Y")
        print("3. Function values: Enter X range, then corresponding Y values")
        
        while True:
            try:
                input_method = input("\nChoose input method (1/2/3): ").strip()
                
                if input_method == "1":
                    return self._get_single_point()
                elif input_method == "2":
                    return self._get_multiple_points()
                elif input_method == "3":
                    return self._get_function_values()
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                sys.exit(0)
            except Exception as e:
                print(f"Error: {e}")
                print("Please try again.")
    
    def _get_single_point(self) -> Tuple[List[float], List[float]]:
        """Get a single X,Y coordinate pair."""
        x_val = float(input("Enter X coordinate: "))
        y_val = float(input("Enter Y coordinate: "))
        return [x_val], [y_val]
    
    def _get_multiple_points(self) -> Tuple[List[float], List[float]]:
        """Get multiple X,Y coordinate pairs."""
        print("\nEnter comma-separated values (e.g., 1,2,3,4,5)")
        
        x_input = input("Enter X values: ").strip()
        y_input = input("Enter Y values: ").strip()
        
        x_values = [float(x.strip()) for x in x_input.split(',')]
        y_values = [float(y.strip()) for y in y_input.split(',')]
        
        if len(x_values) != len(y_values):
            raise ValueError("Number of X and Y values must be equal")
        
        return x_values, y_values
    
    def _get_function_values(self) -> Tuple[List[float], List[float]]:
        """Get X range and calculate Y values based on user function."""
        print("\nAvailable functions:")
        print("1. Linear (y = mx + b)")
        print("2. Quadratic (y = ax² + bx + c)")
        print("3. Sine wave (y = a*sin(bx + c))")
        print("4. Exponential (y = a*e^(bx))")
        print("5. Custom expression")
        
        func_choice = input("Choose function type (1-5): ").strip()
        
        # Get X range
        x_min = float(input("Enter X minimum value: "))
        x_max = float(input("Enter X maximum value: "))
        num_points = int(input("Enter number of points (default 50): ") or "50")
        
        x_values = np.linspace(x_min, x_max, num_points).tolist()
        
        if func_choice == "1":
            m = float(input("Enter slope (m): "))
            b = float(input("Enter y-intercept (b): "))
            y_values = [m * x + b for x in x_values]
        
        elif func_choice == "2":
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            y_values = [a * x**2 + b * x + c for x in x_values]
        
        elif func_choice == "3":
            a = float(input("Enter amplitude (a): "))
            b = float(input("Enter frequency (b): "))
            c = float(input("Enter phase shift (c): "))
            y_values = [a * np.sin(b * x + c) for x in x_values]
        
        elif func_choice == "4":
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter exponent coefficient b: "))
            y_values = [a * np.exp(b * x) for x in x_values]
        
        elif func_choice == "5":
            print("Enter a Python expression using 'x' as variable (e.g., x**2 + 2*x + 1)")
            expression = input("Enter expression: ").strip()
            try:
                y_values = [eval(expression, {"x": x, "np": np}) for x in x_values]
            except Exception as e:
                raise ValueError(f"Invalid expression: {e}")
        
        else:
            raise ValueError("Invalid function choice")
        
        return x_values, y_values
    
    def choose_plot_type(self) -> str:
        """
        Let user choose the type of plot to create.
        
        Returns:
            String representing the plot type
        """
        print("\n=== Choose Plot Type ===")
        print("1. Scatter Plot")
        print("2. Line Plot")
        print("3. Bar Chart")
        print("4. Both Scatter and Line")
        
        while True:
            try:
                choice = input("Enter your choice (1-4): ").strip()
                if choice in ["1", "2", "3", "4"]:
                    return choice
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                sys.exit(0)
    
    def create_plot(self, x_data: List[float], y_data: List[float], plot_type: str):
        """
        Create and display the plot.
        
        Args:
            x_data: List of X coordinates
            y_data: List of Y coordinates
            plot_type: Type of plot to create
        """
        plt.figure(figsize=(10, 6))
        
        # Set up the plot based on user choice
        if plot_type == "1":  # Scatter plot
            plt.scatter(x_data, y_data, c='blue', alpha=0.7, s=50)
            plt.title("Scatter Plot of X vs Y Data")
        
        elif plot_type == "2":  # Line plot
            plt.plot(x_data, y_data, 'b-', linewidth=2, marker='o', markersize=4)
            plt.title("Line Plot of X vs Y Data")
        
        elif plot_type == "3":  # Bar chart
            plt.bar(range(len(x_data)), y_data, alpha=0.7, color='skyblue')
            plt.xticks(range(len(x_data)), [f'{x:.2f}' for x in x_data], rotation=45)
            plt.title("Bar Chart of Y Data")
        
        elif plot_type == "4":  # Both scatter and line
            plt.scatter(x_data, y_data, c='red', alpha=0.7, s=50, label='Data Points')
            plt.plot(x_data, y_data, 'b-', linewidth=1, alpha=0.7, label='Line Connection')
            plt.legend()
            plt.title("Combined Scatter and Line Plot")
        
        # Customize the plot
        plt.xlabel("X Values")
        plt.ylabel("Y Values")
        plt.grid(True, alpha=0.3)
        
        # Add data point annotations for small datasets
        if len(x_data) <= 10:
            for i, (x, y) in enumerate(zip(x_data, y_data)):
                plt.annotate(f'({x:.2f}, {y:.2f})', 
                           (x, y), 
                           xytext=(5, 5), 
                           textcoords='offset points',
                           fontsize=8,
                           alpha=0.7)
        
        plt.tight_layout()
        
        # Display statistics
        self._display_statistics(x_data, y_data)
        
        # Show the plot
        print("\nDisplaying your visualization...")
        plt.show()
    
    def _display_statistics(self, x_data: List[float], y_data: List[float]):
        """Display basic statistics about the data."""
        print("\n=== Data Statistics ===")
        print(f"Number of data points: {len(x_data)}")
        print(f"X range: {min(x_data):.2f} to {max(x_data):.2f}")
        print(f"Y range: {min(y_data):.2f} to {max(y_data):.2f}")
        print(f"X mean: {np.mean(x_data):.2f}")
        print(f"Y mean: {np.mean(y_data):.2f}")
        
        if len(x_data) > 1:
            correlation = np.corrcoef(x_data, y_data)[0, 1]
            print(f"Correlation coefficient: {correlation:.3f}")
    
    def save_plot(self):
        """Ask user if they want to save the plot."""
        save_choice = input("\nDo you want to save the plot? (y/n): ").strip().lower()
        if save_choice == 'y':
            filename = input("Enter filename (without extension): ").strip()
            if not filename:
                filename = "data_visualization"
            plt.savefig(f"{filename}.png", dpi=300, bbox_inches='tight')
            print(f"Plot saved as {filename}.png")
    
    def run(self):
        """Main method to run the data visualization application."""
        try:
            # Get data from user
            x_data, y_data = self.get_user_input()
            
            # Choose plot type
            plot_type = self.choose_plot_type()
            
            # Create and display plot
            self.create_plot(x_data, y_data, plot_type)
            
            # Ask if user wants to save
            self.save_plot()
            
            # Ask if user wants to create another plot
            another = input("\nDo you want to create another visualization? (y/n): ").strip().lower()
            if another == 'y':
                self.run()
            else:
                print("Thank you for using the Data Visualization Application!")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")


def main():
    """Main function to run the application."""
    try:
        visualizer = DataVisualizer()
        visualizer.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()