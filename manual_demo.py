#!/usr/bin/env python3
"""
Manual test to demonstrate the interactive functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_visualizer import DataVisualizer
import matplotlib.pyplot as plt

def manual_demo():
    """Manually demonstrate the key functionality."""
    print("Manual demonstration of Data Visualizer functionality:")
    
    visualizer = DataVisualizer()
    
    # Demo 1: Simple scatter plot
    print("\n1. Creating a simple scatter plot...")
    x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_data = [2, 5, 3, 8, 7, 10, 9, 12, 11, 15]
    
    plt.figure(figsize=(8, 6))
    visualizer.create_plot(x_data, y_data, "1")  # Scatter plot
    plt.savefig("manual_demo_scatter.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Scatter plot saved as 'manual_demo_scatter.png'")
    
    # Demo 2: Line plot with mathematical function
    print("\n2. Creating a line plot with mathematical function...")
    import numpy as np
    x_func = list(np.linspace(-2*np.pi, 2*np.pi, 100))
    y_func = [np.sin(x) + 0.5*np.cos(2*x) for x in x_func]
    
    plt.figure(figsize=(10, 6))
    visualizer.create_plot(x_func, y_func, "2")  # Line plot
    plt.savefig("manual_demo_function.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Function plot saved as 'manual_demo_function.png'")
    
    # Demo 3: Combined plot
    print("\n3. Creating a combined scatter and line plot...")
    x_combined = [0, 1, 2, 3, 4, 5]
    y_combined = [0, 1, 4, 9, 16, 25]  # Quadratic function y = x²
    
    plt.figure(figsize=(8, 6))
    visualizer.create_plot(x_combined, y_combined, "4")  # Combined plot
    plt.savefig("manual_demo_combined.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Combined plot saved as 'manual_demo_combined.png'")
    
    print("\nManual demonstration completed successfully!")
    print("The data visualizer can handle various types of mathematical data.")

if __name__ == "__main__":
    manual_demo()