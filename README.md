# Data Visualization Application

An interactive Python application for mathematical data visualization that allows users to input X and Y coordinates and create various types of graphs.

## Features

- **Interactive Input Methods**: Multiple ways to input data points
  - Single point entry
  - Multiple points (comma-separated values)
  - Mathematical function plotting with predefined functions
  
- **Plot Types**:
  - Scatter plots
  - Line plots  
  - Bar charts
  - Combined scatter and line plots

- **Mathematical Functions**:
  - Linear functions (y = mx + b)
  - Quadratic functions (y = ax² + bx + c)
  - Trigonometric functions (y = a×sin(bx + c))
  - Exponential functions (y = a×e^(bx))
  - Custom mathematical expressions

- **Additional Features**:
  - Data statistics display
  - Correlation analysis
  - Plot customization
  - Save plots as PNG files
  - Input validation and error handling

## Requirements

```bash
pip install matplotlib numpy pandas
```

## Usage

### Running the Interactive Application

```bash
python3 data_visualizer.py
```

The application will guide you through:

1. **Choose Input Method**:
   - `1`: Single point (enter one X,Y coordinate pair)
   - `2`: Multiple points (enter comma-separated X and Y values)
   - `3`: Function values (generate points from mathematical functions)

2. **Select Plot Type**:
   - `1`: Scatter Plot
   - `2`: Line Plot
   - `3`: Bar Chart
   - `4`: Combined Scatter and Line Plot

3. **View Results**: The application displays:
   - Your visualization
   - Data statistics (range, mean, correlation)
   - Option to save the plot

### Example Usage

#### Simple Points
```
Choose input method (1/2/3): 2
Enter X values: 1,2,3,4,5
Enter Y values: 2,4,6,8,10
Choose plot type (1-4): 1
```

#### Mathematical Function
```
Choose input method (1/2/3): 3
Choose function type (1-5): 1
Enter X minimum value: -5
Enter X maximum value: 5
Enter number of points: 50
Enter slope (m): 2
Enter y-intercept (b): 1
Choose plot type (1-4): 2
```

## Testing

Run the test suite to verify functionality:

```bash
python3 test_visualizer.py
```

This will:
- Test core plotting functionality
- Validate different plot types
- Generate sample visualizations
- Create demonstration plots

## Sample Output

The application generates plots with:
- Customized titles and labels
- Grid lines for better readability
- Data point annotations (for small datasets)
- Professional styling
- High-resolution output

## File Structure

```
├── data_visualizer.py      # Main application
├── test_visualizer.py      # Test suite
├── README.md              # This documentation
├── test_plot_*.png        # Generated test plots
└── feature_demonstration.png  # Feature showcase
```

## Mathematical Functions Supported

1. **Linear**: `y = mx + b`
2. **Quadratic**: `y = ax² + bx + c`
3. **Sine Wave**: `y = a×sin(bx + c)`
4. **Exponential**: `y = a×e^(bx)`
5. **Custom**: Any Python expression using `x` variable

## Error Handling

The application includes robust error handling for:
- Invalid numeric input
- Mismatched X,Y array lengths
- Invalid mathematical expressions
- File save errors
- User interruption (Ctrl+C)

## Contributing

This application was designed for educational purposes and mathematical visualization. Feel free to extend it with additional features such as:
- 3D plotting capabilities
- More mathematical functions
- Data import from files
- Interactive plot manipulation
- Statistical analysis tools

## License

Open source - feel free to modify and distribute.