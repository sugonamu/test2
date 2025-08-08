# Advanced Calculator Application

A modern, feature-rich calculator application built with Python and Tkinter. This calculator provides both basic arithmetic operations and advanced scientific functions with a clean, professional interface.

## 🚀 Features

### Basic Operations
- **Addition** (+)
- **Subtraction** (-)
- **Multiplication** (×)
- **Division** (÷)
- **Decimal point** support
- **Negative/Positive** number toggle (±)
- **Percentage** calculations (%)

### Scientific Functions
- **Trigonometric Functions**: sin, cos, tan (in degrees)
- **Logarithmic Functions**: log (base 10), ln (natural log)
- **Power Functions**: x² (square), x³ (cube)
- **Square Root** (√)

### User Interface
- **Modern Dark Theme** with color-coded buttons
- **Responsive Design** with proper grid layout
- **Error Handling** with user-friendly error messages
- **Clear Functions**: C (clear all), CE (clear entry)

## 🎨 Interface Design

The calculator features a professional dark theme with color-coded buttons:
- **Red**: Arithmetic operations (+, -, ×, ÷)
- **Green**: Equals button (=)
- **Orange**: Clear functions (C, CE)
- **Purple**: Scientific functions (sin, cos, tan, sqrt, log, ln, square, cube)
- **Gray**: Number buttons and decimal point

## 📋 Requirements

- **Python 3.x**
- **Tkinter** (usually comes with Python installation)
- **No additional packages required!**

## 🛠️ Installation & Usage

### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://python.org).

### Running the Calculator

1. **Navigate** to the project directory
2. **Run** the calculator:
   ```bash
   python calculator.py
   ```

### Alternative: Run from GitHub
```bash
# Clone the repository
git clone https://github.com/sugonamu/test2.git
cd test2

# Run the calculator
python test.py
```

## 🎯 How to Use

### Basic Calculations
1. Enter the first number using the number buttons
2. Press an operation button (+, -, ×, ÷)
3. Enter the second number
4. Press = to see the result

### Scientific Functions
1. Enter a number
2. Press a scientific function button (sin, cos, tan, sqrt, etc.)
3. The result will be displayed immediately

### Special Functions
- **C**: Clears all data and resets the calculator
- **CE**: Clears the current entry only
- **±**: Toggles between positive and negative numbers
- **%**: Converts the current number to percentage (divides by 100)

## ⚠️ Error Handling

The calculator includes comprehensive error handling for:
- **Division by zero**
- **Square root of negative numbers**
- **Logarithm of non-positive numbers**
- **Invalid mathematical operations**

Error messages are displayed in popup dialogs to inform the user of the issue.

## 🏗️ Code Structure

```
calculator.py
├── Calculator Class
│   ├── __init__() - Initialize calculator state
│   ├── create_widgets() - Build the GUI
│   ├── button_click() - Handle button presses
│   ├── calculate() - Basic arithmetic operations
│   └── scientific_calculate() - Scientific functions
└── main() - Application entry point
```

## 🔧 Customization

You can easily customize the calculator by modifying:
- **Colors**: Change the hex color codes in the button configuration
- **Size**: Modify the `geometry()` call in `__init__()`
- **Fonts**: Update the font parameters in button creation
- **Functions**: Add new scientific functions in `scientific_calculate()`

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the error messages displayed by the calculator
2. Ensure you have Python 3.x installed
3. Verify that Tkinter is available in your Python installation

---

**Created by**: Advanced Calculator Team  
**Repository**: [https://github.com/sugonamu/test2](https://github.com/sugonamu/test2)  
**Last Updated**: August 2025