#!/usr/bin/env python3
"""
Demo script showing practical examples of the data visualization application.
This script demonstrates how the visualizer can be used programmatically.
"""

import matplotlib.pyplot as plt
import numpy as np
from data_visualizer import DataVisualizer


def demo_examples():
    """Run practical demonstration examples."""
    print("="*60)
    print("DATA VISUALIZATION APPLICATION - PRACTICAL EXAMPLES")
    print("="*60)
    
    visualizer = DataVisualizer()
    
    # Example 1: Physics - Projectile Motion
    print("\n1. Physics Example: Projectile Motion")
    print("-" * 40)
    
    # Calculate projectile motion: y = x*tan(θ) - (g*x²)/(2*v₀²*cos²(θ))
    g = 9.81  # gravity
    v0 = 20   # initial velocity
    angle = 45 * np.pi / 180  # 45 degrees in radians
    
    x_proj = np.linspace(0, 40, 50)
    y_proj = x_proj * np.tan(angle) - (g * x_proj**2) / (2 * v0**2 * np.cos(angle)**2)
    y_proj = [max(0, y) for y in y_proj]  # Ground level is y=0
    
    plt.figure(figsize=(10, 6))
    visualizer.create_plot(list(x_proj), y_proj, "2")
    plt.title("Projectile Motion (v₀=20 m/s, θ=45°)")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Height (m)")
    plt.savefig("demo_projectile_motion.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Projectile motion plot saved as 'demo_projectile_motion.png'")
    
    # Example 2: Economics - Supply and Demand
    print("\n2. Economics Example: Supply and Demand Curves")
    print("-" * 50)
    
    price = np.linspace(1, 10, 20)
    demand = 100 - 8 * price    # Demand decreases as price increases
    supply = -20 + 6 * price    # Supply increases as price increases
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(demand, price, 'b-', linewidth=2, label='Demand Curve')
    ax.plot(supply, price, 'r-', linewidth=2, label='Supply Curve')
    
    # Find equilibrium point
    equilibrium_idx = np.argmin(np.abs(demand - supply))
    eq_quantity = demand[equilibrium_idx]
    eq_price = price[equilibrium_idx]
    
    ax.scatter([eq_quantity], [eq_price], color='green', s=100, 
               label=f'Equilibrium ({eq_quantity:.1f}, ${eq_price:.1f})', zorder=5)
    
    ax.set_xlabel('Quantity')
    ax.set_ylabel('Price ($)')
    ax.set_title('Supply and Demand Analysis')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.savefig("demo_supply_demand.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Supply and demand plot saved as 'demo_supply_demand.png'")
    
    # Example 3: Statistics - Normal Distribution
    print("\n3. Statistics Example: Normal Distribution")
    print("-" * 45)
    
    x_norm = np.linspace(-4, 4, 100)
    
    # Different normal distributions
    y_norm1 = (1/np.sqrt(2*np.pi)) * np.exp(-0.5 * x_norm**2)  # μ=0, σ=1
    y_norm2 = (1/np.sqrt(2*np.pi*0.5)) * np.exp(-0.5 * (x_norm**2)/0.5)  # μ=0, σ=0.7
    y_norm3 = (1/np.sqrt(2*np.pi*2)) * np.exp(-0.5 * ((x_norm-1)**2)/2)  # μ=1, σ=1.4
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_norm, y_norm1, 'b-', linewidth=2, label='μ=0, σ=1')
    plt.plot(x_norm, y_norm2, 'r-', linewidth=2, label='μ=0, σ=0.7')
    plt.plot(x_norm, y_norm3, 'g-', linewidth=2, label='μ=1, σ=1.4')
    
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.title('Normal Distribution Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("demo_normal_distribution.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Normal distribution plot saved as 'demo_normal_distribution.png'")
    
    # Example 4: Engineering - Signal Processing
    print("\n4. Engineering Example: Signal Processing")
    print("-" * 45)
    
    t = np.linspace(0, 2, 500)
    
    # Create a composite signal
    signal = (np.sin(2*np.pi*5*t) +           # 5 Hz component
              0.5*np.sin(2*np.pi*10*t) +      # 10 Hz component  
              0.3*np.sin(2*np.pi*20*t))       # 20 Hz component
    
    # Add some noise
    noise = 0.2 * np.random.normal(0, 1, len(t))
    noisy_signal = signal + noise
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Clean signal
    ax1.plot(t, signal, 'b-', linewidth=1.5)
    ax1.set_title('Original Signal (5Hz + 10Hz + 20Hz components)')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Amplitude')
    ax1.grid(True, alpha=0.3)
    
    # Noisy signal
    ax2.plot(t, noisy_signal, 'r-', alpha=0.7, linewidth=0.8)
    ax2.plot(t, signal, 'b-', linewidth=1.5, label='Original')
    ax2.set_title('Signal with Noise')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Amplitude')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("demo_signal_processing.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Signal processing plot saved as 'demo_signal_processing.png'")
    
    # Example 5: Biology - Population Growth
    print("\n5. Biology Example: Population Growth Models")
    print("-" * 48)
    
    t_bio = np.linspace(0, 10, 100)
    
    # Exponential growth
    P0 = 100  # Initial population
    r = 0.3   # Growth rate
    exponential = P0 * np.exp(r * t_bio)
    
    # Logistic growth
    K = 1000  # Carrying capacity
    logistic = K / (1 + ((K - P0) / P0) * np.exp(-r * t_bio))
    
    plt.figure(figsize=(10, 6))
    plt.plot(t_bio, exponential, 'r-', linewidth=2, label='Exponential Growth')
    plt.plot(t_bio, logistic, 'b-', linewidth=2, label='Logistic Growth')
    plt.axhline(y=K, color='gray', linestyle='--', alpha=0.7, label='Carrying Capacity')
    
    plt.xlabel('Time (years)')
    plt.ylabel('Population Size')
    plt.title('Population Growth Models Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("demo_population_growth.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Population growth plot saved as 'demo_population_growth.png'")
    
    print("\n" + "="*60)
    print("DEMO SUMMARY")
    print("="*60)
    print("✓ Physics: Projectile motion simulation")
    print("✓ Economics: Supply and demand analysis")
    print("✓ Statistics: Normal distribution comparison")
    print("✓ Engineering: Signal processing visualization")
    print("✓ Biology: Population growth models")
    print("\nAll demo plots have been saved as PNG files.")
    print("These examples show how the data visualizer can be used")
    print("for various mathematical and scientific applications!")


if __name__ == "__main__":
    demo_examples()