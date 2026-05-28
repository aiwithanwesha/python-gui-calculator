from tkinter import *

root = Tk()
calculation_history = []
history_visible = False
root.title("CALCULATOR BY ANWESHA")
root.resizable(False, False)

# --- Color Palette ---
BG_COLOR = "#121318"        
BTN_NUM = "#2a2a2f"          
BTN_OPERATOR = "#3a444c"    
BTN_AC = "#00a3e0"          
BTN_EQUAL = "#e8def8"       
TEXT_LIGHT = "#ffffff"      
TEXT_DARK = "#1d192b"       
TEXT_AC = "#000000"         

root.configure(bg=BG_COLOR)

def show(value):
    current = e1.get()
    e1.delete(0, END)
    e1.insert(0, str(current) + str(value))

def clear():
    e1.delete(0, END)

def clear_c():
    current = e1.get()
    e1.delete(0, END)
    e1.insert(0, current[:-1])

def calculate():
    try:
        raw_expression = e1.get()
        expression = raw_expression.replace("×", "*").replace("÷", "/").replace("^", "**").replace("%", "/100")

        result = eval(expression)

        history_entry = f"{raw_expression} = {result}"
        calculation_history.append(history_entry)
        update_history_display()

        e1.delete(0, END)
        e1.insert(0, result)

    except Exception:
        e1.delete(0, END)
        e1.insert(0, "Error")

def update_history_display():
    if not calculation_history:
        history_text.config(text="No history yet!")
    else:
        history_text.config(text="\n".join(reversed(calculation_history[-5:])))

def toggle_history():
    global history_visible
    if history_visible:
        history_frame.grid_remove()
        line_frame.grid_remove()  
        history_visible = False
    else:
        update_history_display()
        history_frame.grid(row=1, column=0, columnspan=5, padx=10, pady=5, sticky="ew")
        line_frame.grid(row=2, column=0, columnspan=5, padx=20, pady=(0, 10), sticky="ew")
        history_visible = True

# --- 🕒 History Toggle Button ---
history_btn = Button(root, text="History", bg=BG_COLOR, fg=BTN_AC, font=('Arial', 10, 'bold'), relief=FLAT, bd=0, command=toggle_history)
history_btn.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=(10, 0))

# --- Row 1 ---
history_frame = Frame(root, bg="#1a1b20", bd=0) 
history_text = Label(history_frame, text="No history yet!", font=('Arial', 11), bg="#1a1b20", fg="#8b949e", justify=RIGHT, anchor="e")
history_text.pack(fill=X, padx=15, pady=8)

line_frame = Frame(root, bg="#ffffff", height=1)

# Display Screen 
e1 = Entry(root, width=21, font=('Arial', 20), bg=BG_COLOR, fg=TEXT_LIGHT, bd=0, justify=RIGHT, insertbackground="white")
e1.grid(row=3, column=0, columnspan=5, padx=20, pady=10)

# Row 4 
mybutton = Button(root, width=17, height=3, text="AC", bg=BTN_AC, fg=TEXT_AC, font=('Arial', 10, 'bold'), relief=FLAT, command=clear)
mybutton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="^", bg=BTN_OPERATOR, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("^"))
mybutton.grid(row=4, column=2, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="÷", bg=BTN_OPERATOR, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("÷"))
mybutton.grid(row=4, column=3, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="%", bg=BTN_OPERATOR, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("%"))
mybutton.grid(row=4, column=4, padx=5, pady=5)

# Row 5 
mybutton = Button(root, width=7, height=3, text="7", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("7"))
mybutton.grid(row=5, column=0, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="8", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("8"))
mybutton.grid(row=5, column=1, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="9", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("9"))
mybutton.grid(row=5, column=2, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="×", bg=BTN_OPERATOR, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("×"))
mybutton.grid(row=5, column=3, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="(", bg=BTN_OPERATOR, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("("))
mybutton.grid(row=5, column=4, padx=5, pady=5)

# Row 6 
mybutton = Button(root, width=7, height=3, text="4", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("4"))
mybutton.grid(row=6, column=0, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="5", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("5"))
mybutton.grid(row=6, column=1, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="6", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("6"))
mybutton.grid(row=6, column=2, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="−", bg=BTN_OPERATOR, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("-"))
mybutton.grid(row=6, column=3, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text=")", bg=BTN_OPERATOR, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show(")"))
mybutton.grid(row=6, column=4, padx=5, pady=5)

# Row 7 
mybutton = Button(root, width=7, height=3, text="1", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("1"))
mybutton.grid(row=7, column=0, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="2", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("2"))
mybutton.grid(row=7, column=1, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="3", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("3"))
mybutton.grid(row=7, column=2, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="+", bg=BTN_OPERATOR, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("+"))
mybutton.grid(row=7, column=3, padx=5, pady=5)
mybutton = Button(root, width=7, height=7, text="=", bg=BTN_EQUAL, fg=TEXT_DARK, font=('Arial', 10, 'bold'), relief=FLAT, command=calculate)
mybutton.grid(row=7, column=4, rowspan=2, padx=5, pady=5)

# Row 8 
mybutton = Button(root, width=17, height=3, text="0", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("0"))
mybutton.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text=".", bg=BTN_NUM, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=lambda: show("."))
mybutton.grid(row=8, column=2, padx=5, pady=5)
mybutton = Button(root, width=7, height=3, text="⌫", bg=BTN_OPERATOR, fg=TEXT_LIGHT, font=('Arial', 10, 'bold'), relief=FLAT, command=clear_c)
mybutton.grid(row=8, column=3, padx=5, pady=5)

footer_lbl = Label(root, text="© Created by Anwesha Santra | Code. Compute. Correct. | May 28, 2026", font=('Arial', 8, 'bold'), fg="#6c757d", bg=BG_COLOR)
footer_lbl.grid(row=9, column=0, columnspan=5, pady=(15, 8))

root.mainloop()











