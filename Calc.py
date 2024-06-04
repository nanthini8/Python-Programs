import tkinter as tk

def add_entry(value):
    current_val=entry_op.get()
    entry_op.delete(0,tk.END)
    entry_op.insert(0,current_val+str(value))

def clear_entry():
    entry_op.delete(0,tk.END)
    
def calculate():
    try:
        exp=entry_op.get()
        res=eval(exp)
        entry_res.delete(0,tk.END)
        entry_res.insert(0,res)

    except Exception as e:
        entry_res.delete(0,tk.END)
        entry_res.insert(0,'Error')


window=tk.Tk()
window.title('Simple Calculator')
                         
entry_op = tk.Entry(window, font=('Arial', 20))  
entry_op.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky='we')

button_style = {'font': ('Arial', 14), 'width': 5, 'height': 2}

# Buttons for digits
for i in range(10):
    tk.Button(window, text=str(i), command=lambda i=i: add_entry(i), **button_style).grid(row=(i//3)+1, column=(i%3), padx=5, pady=5)

# Operator buttons
op_buttons = ['+', '-', '*', '/']
for i, op in enumerate(op_buttons):
    tk.Button(window, text=op, command=lambda op=op: add_entry(op), **button_style).grid(row=i+1, column=4, padx=5, pady=5, sticky='ew')

# Clear button
tk.Button(window, text='Clear', command=clear_entry, **button_style).grid(row=4, column=1, padx=5, pady=5, sticky='ew')

# Calculate button
tk.Button(window, text='=', command=calculate, **button_style).grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky='ew')

entry_res=tk.Entry(window, font=('Arial', 20))
entry_res.grid(row=5,column=0,columnspan=6, padx=10, pady=10, sticky='we')  #NE-North east

window.mainloop()
