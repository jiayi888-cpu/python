import tkinter as tk
from functools import partial

def create_calculator_window():
    window = tk.Tk()
    window.geometry("300x400")
    window.title("计算器")
    
    display = tk.Label(window, text="", font=("Helvetica", 16), height=2, width=18)
    display.grid(row=0, column=0, columnspan=4, pady=10)
    
    def on_keypress(key):
        if key == "AC":
            display["text"] = ""
        elif key == "←":
            display["text"] = display["text"][:-1]
        elif key == "%":
            try:
                expression = eval(display["text"])
                display["text"] = str(expression / 100)
            except:
                display["text"] = "Error"
        elif key == "=":
            try:
                expression = display["text"]
                expression = expression.replace("÷", "/")
                expression = expression.replace("x", "*")
                result = eval(expression)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                display["text"] = str(result)
            except:
                display["text"] = "Error"
        else:
            if "=" in display["text"]:
                display["text"] = ""
            display["text"] += key
    
    keys = [
        ("AC", on_keypress),
        ("←", on_keypress),
        ("%", on_keypress),
        ("÷", on_keypress),
        ("7", on_keypress),
        ("8", on_keypress),
        ("9", on_keypress),
        ("x", on_keypress),
        ("4", on_keypress),
        ("5", on_keypress),
        ("6", on_keypress),
        ("-", on_keypress),
        ("1", on_keypress),
        ("2", on_keypress),
        ("3", on_keypress),
        ("+", on_keypress),
        ("0", on_keypress),
        (".", on_keypress),
        ("(", on_keypress),
        (")", on_keypress),
        ("=", on_keypress)
    ]
    
    row = 1
    col = 0
    for key, command in keys:
        button = tk.Button(window, text=key, font=("Helvetica", 12), height=2, width=5)
        button.grid(row=row, column=col, padx=5, pady=5)
        button.configure(command=partial(command, key))
        col += 1
        if col > 3:
            col = 0
            row += 1
    
    window.bind("<Key>", lambda event: on_keypress(event.char))
    
    window.mainloop()

if __name__ == "__main__":
    create_calculator_window()
