import tkinter as tk
from tkinter import ttk, messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Calculator state
        self.current_number = ""
        self.first_number = 0
        self.operation = ""
        self.should_reset = False
        
        # Create display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="#2C3E50")
        display_frame.pack(fill="x", padx=10, pady=10)
        
        # Display
        display = tk.Entry(display_frame, textvariable=self.display_var, 
                          font=("Arial", 24), justify="right", 
                          bg="#34495E", fg="white", bd=0, relief="flat")
        display.pack(fill="x", padx=5, pady=5)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#2C3E50")
        buttons_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Button configurations
        button_configs = [
            # Row 1 - Scientific functions
            [("sin", "sin"), ("cos", "cos"), ("tan", "tan"), ("√", "sqrt")],
            # Row 2 - More scientific functions
            [("log", "log"), ("ln", "ln"), ("x²", "square"), ("x³", "cube")],
            # Row 3 - Numbers and operations
            [("7", "7"), ("8", "8"), ("9", "9"), ("÷", "divide")],
            # Row 4
            [("4", "4"), ("5", "5"), ("6", "6"), ("×", "multiply")],
            # Row 5
            [("1", "1"), ("2", "2"), ("3", "3"), ("-", "subtract")],
            # Row 6
            [("0", "0"), (".", "decimal"), ("=", "equals"), ("+", "add")],
            # Row 7 - Clear and special functions
            [("C", "clear"), ("CE", "clear_entry"), ("±", "negate"), ("%", "percent")]
        ]
        
        # Create buttons
        for i, row in enumerate(button_configs):
            for j, (text, command) in enumerate(row):
                btn = tk.Button(buttons_frame, text=text, font=("Arial", 14),
                              width=8, height=2, bd=0, relief="flat",
                              command=lambda cmd=command: self.button_click(cmd))
                
                # Color coding
                if command in ["add", "subtract", "multiply", "divide"]:
                    btn.configure(bg="#E74C3C", fg="white", activebackground="#C0392B")
                elif command == "equals":
                    btn.configure(bg="#27AE60", fg="white", activebackground="#229954")
                elif command in ["clear", "clear_entry"]:
                    btn.configure(bg="#F39C12", fg="white", activebackground="#E67E22")
                elif command in ["sin", "cos", "tan", "sqrt", "log", "ln", "square", "cube"]:
                    btn.configure(bg="#9B59B6", fg="white", activebackground="#8E44AD")
                else:
                    btn.configure(bg="#ECF0F1", fg="#2C3E50", activebackground="#BDC3C7")
                
                btn.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
        
        # Configure grid weights
        for i in range(7):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)
    
    def button_click(self, command):
        current = self.display_var.get()
        
        if command in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.should_reset:
                self.current_number = command
                self.should_reset = False
            else:
                self.current_number += command
            self.display_var.set(self.current_number)
            
        elif command == "decimal":
            if "." not in self.current_number:
                self.current_number += "."
                self.display_var.set(self.current_number)
                
        elif command in ["add", "subtract", "multiply", "divide"]:
            if self.current_number:
                self.first_number = float(self.current_number)
                self.operation = command
                self.current_number = ""
                self.should_reset = False
                
        elif command == "equals":
            if self.current_number and self.operation:
                second_number = float(self.current_number)
                result = self.calculate(self.first_number, second_number, self.operation)
                self.display_var.set(str(result))
                self.current_number = str(result)
                self.operation = ""
                self.should_reset = True
                
        elif command == "clear":
            self.current_number = ""
            self.first_number = 0
            self.operation = ""
            self.should_reset = False
            self.display_var.set("0")
            
        elif command == "clear_entry":
            self.current_number = ""
            self.display_var.set("0")
            
        elif command == "negate":
            if self.current_number:
                if self.current_number.startswith("-"):
                    self.current_number = self.current_number[1:]
                else:
                    self.current_number = "-" + self.current_number
                self.display_var.set(self.current_number)
                
        elif command == "percent":
            if self.current_number:
                result = float(self.current_number) / 100
                self.display_var.set(str(result))
                self.current_number = str(result)
                
        elif command in ["sin", "cos", "tan", "sqrt", "log", "ln", "square", "cube"]:
            if self.current_number:
                number = float(self.current_number)
                result = self.scientific_calculate(number, command)
                self.display_var.set(str(result))
                self.current_number = str(result)
                self.should_reset = True
    
    def calculate(self, first, second, operation):
        if operation == "add":
            return first + second
        elif operation == "subtract":
            return first - second
        elif operation == "multiply":
            return first * second
        elif operation == "divide":
            if second == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return 0
            return first / second
    
    def scientific_calculate(self, number, operation):
        try:
            if operation == "sin":
                return math.sin(math.radians(number))
            elif operation == "cos":
                return math.cos(math.radians(number))
            elif operation == "tan":
                return math.tan(math.radians(number))
            elif operation == "sqrt":
                if number < 0:
                    messagebox.showerror("Error", "Cannot calculate square root of negative number!")
                    return 0
                return math.sqrt(number)
            elif operation == "log":
                if number <= 0:
                    messagebox.showerror("Error", "Cannot calculate log of non-positive number!")
                    return 0
                return math.log10(number)
            elif operation == "ln":
                if number <= 0:
                    messagebox.showerror("Error", "Cannot calculate ln of non-positive number!")
                    return 0
                return math.log(number)
            elif operation == "square":
                return number ** 2
            elif operation == "cube":
                return number ** 3
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
            return 0

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()