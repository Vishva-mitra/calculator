import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc_screen.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc_screen['state'] = tk.NORMAL
    calc_screen.delete(0, tk.END)
    calc_screen.insert(0, value + digit)
    calc_screen['state'] = tk.DISABLED


def clear():
    calc_screen['state'] = tk.NORMAL
    calc_screen.delete(0, tk.END)
    calc_screen.insert(0, '0')
    calc_screen['state'] = tk.DISABLED


def add_operation(operation):
    value = calc_screen.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc_screen.get()
    calc_screen['state'] = tk.NORMAL
    calc_screen.delete(0, tk.END)
    calc_screen.insert(0, value + operation)
    calc_screen['state'] = tk.DISABLED


def calculate():
    value = calc_screen.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc_screen['state'] = tk.NORMAL
    calc_screen.delete(0, tk.END)
    try:
        calc_screen.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showinfo('Внимание!', 'На ноль делить нельзя')
        calc_screen.insert(0, '0')
    finally:
        calc_screen['state'] = tk.DISABLED


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 15), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15, 'bold'), fg='red',
                     command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15, 'bold'), fg='red', command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15, 'bold'), fg='red', command=clear)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '\x7f':
        clear()


win = tk.Tk()
win.title('Калькулятор')
win.geometry('250x280+1000+300')
win.resizable(False, False)
win['bg'] = '#66ff33'
win.bind('<Key>', press_key)

calc_screen = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15, disabledforeground='#000000',
                       disabledbackground='#ffffff')
calc_screen.insert(0, '0')
calc_screen['state'] = tk.DISABLED
calc_screen.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('c').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
