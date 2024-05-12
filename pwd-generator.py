import tkinter as tk
import ttkbootstrap as ttk
import random
import string

# Password Generation Function
def password():
    password = []
    len = int(size_var.get())
    for x in range(len):
        if upper_var.get() == 1:
            password += [random.choice(string.ascii_uppercase)]
        if lower_var.get() == 1:    
            password += [random.choice(string.ascii_lowercase)]
        if numbers_var.get() == 1:   
            password += [random.choice(string.digits)]
        if punctuation_var.get() == 1:   
            password += [random.choice(string.punctuation)]
    random.shuffle(password)
    #return ''.join(password[:len])
    output.delete('1.0', 'end')
    output.insert('1.0', ''.join(password[:len]))

# Window
window = ttk.Window()
window.title('Password Generator')
window.geometry('500x325')

# Password Output
output_label = ttk.Label(master = window, text = 'Output', font = ('Arial', '12', 'bold', 'underline'))
output_label.pack(pady = (30, 0))
output = ttk.Text(master = window, height = 1)
output.pack(pady = (5, 20), padx = 20)

# Password Size Selector
size_frame = ttk.Frame(master = window)
size_frame.pack()
size_text = ttk.Label(master = size_frame, text = 'Password Size:')
size_text.pack(side = 'left', padx = (0, 10))
size_var = ttk.StringVar()
size_var.set(8)
size_input = ttk.Spinbox(master = size_frame, from_ = 8, to = 32, width = 3, textvariable = size_var)
size_input.pack(side = 'left', pady = 20)

# Other Options
other_frame = ttk.Frame(master = window)
other_frame.pack()
other_text = ttk.Label(master = other_frame, text = 'Other Options:')
other_text.pack(side = 'left', padx = (0, 10), pady = 20)

upper_var = ttk.IntVar()
upper_var.set(1)
uppercase_check = ttk.Checkbutton(master = other_frame, variable = upper_var, text = 'Uppercase')
uppercase_check.pack()

lower_var = ttk.IntVar()
lower_var.set(1)
lowercase_check = ttk.Checkbutton(master = other_frame, variable = lower_var, text = 'Lowercase')
lowercase_check.pack()

numbers_var = ttk.IntVar()
numbers_var.set(1)
numbers_check = ttk.Checkbutton(master = other_frame, variable = numbers_var, text = 'Numbers')
numbers_check.pack()

punctuation_var = ttk.IntVar()
punctuation_var.set(1)
punctuation_check = ttk.Checkbutton(master = other_frame, variable = punctuation_var, text = 'Punctuation')
punctuation_check.pack()

# Generate Button
generate_button = ttk.Button(master = window, text = 'Generate', command = password)
generate_button.pack(pady = 20)

# Run
window.mainloop()