import customtkinter
from customtkinter import *
from PIL import Image
from calc import _Logic as Calc
import math

# Set cosmetic features
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("graphics/themes/sky.json")

# Set properties
app = CTk()
app.title("Calculator")
app.geometry("400x600")
app.resizable(False, False)

calc = Calc()  # Make an instance

upper_frame = CTkFrame(app)
upper_frame.pack(fill="x", padx=10, pady=10)

try: # Try to display the image, otherwise have a contingency
    image_logo = CTkImage(
        light_image=Image.open("graphics/images/logo.png"),
        dark_image=Image.open("graphics/images/logo.png"),
        size=(40, 40)
    )

    label_logo = CTkLabel(upper_frame, image=image_logo, text="")
    label_logo.pack(pady=(0, 5))
except Exception:
    label_logo = CTkLabel(upper_frame, text="no logo")
    label_logo.pack(pady=(0, 5))

result_label = CTkLabel(upper_frame, text="", font=("Arial", 18), anchor="e")
result_label.pack(fill="x")

# Entry field, for taking inputs
entry = CTkEntry(app, font=("Arial", 16), height=40)
entry.pack(fill="x", padx=10, pady=(0, 5))

bottom_top = CTkFrame(app)
bottom_top.pack(fill="x", padx=10, pady=5)

# Delete everything
clear_btn = CTkButton(bottom_top, text="C", width=120,
                     command=lambda: entry.delete(0, END))
clear_btn.pack(side="left", padx=3)

# Delete, in a traditional backspace manner
backspace = CTkButton(bottom_top, text="←", width=120,
                        command=lambda: entry.delete(len(entry.get())-1, END) if entry.get() else None)
backspace.pack(side="left", padx=3)

calculate_btn = CTkButton(bottom_top, text="=", width=120)
calculate_btn.pack(side="left", padx=3)

arith_frame = CTkFrame(app)
arith_frame.pack(fill="x", padx=10, pady=5)

operators = [("+", "add"), ("-", "minus"), ("*", "mul"), ("/", "div")]
for operator, _ in operators:
    CTkButton(arith_frame, text=operator, width=70, command=lambda o=operator: entry.insert(END, o)).pack(side="left", padx=5, expand=True)

CTkFrame(app, height=5).pack(fill="x")

# Ability to utilize buttons for adding numbers instead of using keyboard input
row1 = CTkFrame(app)
row1.pack(fill="x", padx=10, pady=3)
for num in ["5", "6", "7", "8", "9"]:
    CTkButton(row1, text=num, width=50, command=lambda n=num: entry.insert(END, n)).pack(side="left", padx=2)
CTkButton(row1, text="(", width=50, command=lambda: entry.insert(END, "(")).pack(side="left", padx=2)
CTkButton(row1, text=")", width=50, command=lambda: entry.insert(END, ")")).pack(side="left", padx=2)

# Ability to utilize buttons for adding numbers instead of using keyboard input
row2 = CTkFrame(app)
row2.pack(fill="x", padx=10, pady=3)
for num in ["0", "1", "2", "3", "4"]:
    CTkButton(row2, text=num, width=50, command=lambda n=num: entry.insert(END, n)).pack(side="left", padx=2)
CTkButton(row2, text=".", width=50, command=lambda: entry.insert(END, ".")).pack(side="left", padx=2)
CTkButton(row2, text="π", width=50, command=lambda: entry.insert(END, str(math.pi))).pack(side="left", padx=2)

CTkFrame(app, height=10).pack(fill="x")

# Creating a frame collection of power and root functions
sp_frame = CTkFrame(app)
sp_frame.pack(fill="x", padx=10, pady=3)

sq_btn = CTkButton(sp_frame, text="x²", width=180, command=lambda: entry.insert(END, "sq("))
sq_btn.grid(row=0, column=0, padx=5, pady=3)

pow_btn = CTkButton(sp_frame, text="xʸ", width=180, command=lambda: entry.insert(END, "pow("))
pow_btn.grid(row=0, column=1, padx=5, pady=3)

sqrt_btn = CTkButton(sp_frame, text="√x", width=180, command=lambda: entry.insert(END, "sqrt("))
sqrt_btn.grid(row=1, column=0, padx=5, pady=3)

root_btn = CTkButton(sp_frame, text="ʸ√x", width=180, command=lambda: entry.insert(END, "root("))
root_btn.grid(row=1, column=1, padx=5, pady=3)

CTkFrame(app, height=10).pack(fill="x")

# Trigonomtry functions, tradition 12
trig_frame = CTkFrame(app)
trig_frame.pack(fill="x", padx=10, pady=3)

trig_btns = [
    ("sin", "sin("), ("cos", "cos("), ("tan", "tan("),
    ("csc", "csc("), ("sec", "sec("), ("cot", "cot("),
    ("asin", "asin("), ("acos", "acos("), ("atan", "atan("),
    ("acsc", "acsc("), ("asec", "asec("), ("acot", "acot(")
]

for trig_btn, (txt, cmd) in enumerate(trig_btns):
    CTkButton(trig_frame, text=txt, width=120, command=lambda c=cmd: entry.insert(END, c)).grid(row=trig_btn//3, column=trig_btn%3, padx=3, pady=3)

CTkFrame(app, height=10).pack(fill="x")

# The last frame dedicated to extra functions for the calculator
extra_frame = CTkFrame(app)
extra_frame.pack(fill="x", padx=10, pady=3)

abs_btn = CTkButton(extra_frame, text="abs", width=90, command=lambda: entry.insert(END, "abs("))
abs_btn.pack(side="left", padx=3)

fact_btn = CTkButton(extra_frame, text="n!", width=90, command=lambda: entry.insert(END, "fact("))
fact_btn.pack(side="left", padx=3)

# log base 10
log_btn = CTkButton(extra_frame, text="log", width=90, command=lambda: entry.insert(END, "log(, 10)"))
log_btn.pack(side="left", padx=3)

# ln (natural log)
ln_btn = CTkButton(extra_frame, text="ln", width=90, command=lambda: entry.insert(END, 'log(, "e")'))
ln_btn.pack(side="left", padx=3)

# Evalute the input to process to functions
def evaluate():
    expression = entry.get().strip()
    try:
        local_env = {
            "add": calc.add,
            "minus": calc.minus,
            "mul": calc.multiply,
            "div": calc.divide,
            "abs": calc.abs,
            "fact": calc.factorial,
            "sq": calc.square,
            "pow": calc.power,
            "sqrt": calc.square_root,
            "root": calc.root,
            "sin": calc.sin,
            "cos": calc.cos,
            "tan": calc.tan,
            "csc": calc.csc,
            "sec": calc.sec,
            "cot": calc.cot,
            "asin": calc.arcsin,
            "acos": calc.arccos,
            "atan": calc.arctan,
            "acsc": calc.arccsc,
            "asec": calc.arcsec,
            "acot": calc.arccot,
            "log": calc.log,
            "pi": math.pi,
        }

        result = eval(expression, {"__builtins__": {}}, local_env) # To ensure safe processing
        result_label.configure(text = str(result)) # Update result widget
    except Exception as e: # Otherwise, do the following
        result_label.configure(text = f"Error: {e}") # Update result widget

calculate_btn.configure(command = evaluate)

# Making the function to start the program
def start():
    app.mainloop()
