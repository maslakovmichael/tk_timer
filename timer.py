import tkinter as tk
from datetime import datetime

BD = 3
times = 0
after_id = ''

def time_count():
    global times, after_id
    after_id = root.after(1000, time_count)
    f_times = datetime.fromtimestamp(times).strftime('%M:%S')
    lab_screen.configure(text = f_times)
    times += 1


def start_func():
    btn_start.grid_forget()
    btn_stop.grid(row=1, column=0, columnspan=2, sticky='we')
    time_count()

def stop_func():
    btn_stop.grid_forget()
    btn_clear.grid(row=1, column=0, sticky='we')
    btn_continue.grid(row=1, column=1, sticky='we')
    root.after_cancel(after_id)

def reset_func():
    global times
    times = 0
    lab_screen.configure(text='00:00')
    btn_clear.grid_forget()
    btn_continue.grid_forget()
    btn_start.grid(row=1, column=0, columnspan=2, sticky='we')

def continue_func():
    btn_clear.grid_forget()
    btn_continue.grid_forget()
    btn_stop.grid(row=1, column=0, columnspan=2, sticky='we')
    time_count()


root = tk.Tk()
root.title('Секундомер')
root.resizable(False, False)

lab_screen = tk.Label(root, text='00:00', font=('Arial', 100), width=5)
btn_start = tk.Button(root, text='Start', bd=BD, font=('Arial', 30), command=start_func)
btn_stop = tk.Button(root, text='Stop', bd=BD, font=('Arial', 30), command=stop_func)
btn_clear = tk.Button(root, text='Reset', bd=BD, font=('Arial', 30), command=reset_func)
btn_continue = tk.Button(root, text='Continue', bd=BD, font=('Arial', 30), command=continue_func)

lab_screen.grid(row=0, column=0, columnspan=2, sticky='we')
btn_start.grid(row=1, column=0, columnspan=2, sticky='we')

root.mainloop()