import tkinter as tk
from datetime import datetime

BD = 3                        # размер границы
times = 0                     # переменная times - счетчик секунд
after_id = ''                 # after_id --- переменная метода after() обьекта root - определяет задержку в 1000ms
                              # и рекурсионно запускает функцию time_count(), которая делает задержку и добавляет счетчик times

def time_count():
    global times, after_id
    after_id = root.after(1000, time_count)
    f_times = datetime.fromtimestamp(times).strftime('%M:%S') # форматирование количества секунд times в читаемую форму
    lab_screen.configure(text = f_times)   # установка нового значения в переменную text лейбла lab_screen
    times += 1                          # счетчик секунд


def start_func():
    btn_start.grid_forget()   # остановка выполнения кнопки старт
    btn_stop.grid(row=1, column=0, columnspan=2, sticky='we') # отображение кнопки стоп
    time_count()     # запуск рекурсивной функции time_count() для отсчета секунд

def stop_func():
    btn_stop.grid_forget()    # остановка отображения кнопки стоп
    btn_reset.grid(row=1, column=0, sticky='we')  # отображение кнопки сброса
    btn_continue.grid(row=1, column=1, sticky='we') # отображения кнопки продолжения отсчета
    root.after_cancel(after_id) # прикращение выполнения метода after

def reset_func():
    global times
    times = 0
    lab_screen.configure(text='00:00') # установка нулевого значения в lab_screen
    btn_reset.grid_forget()            # остановка отображения кнопки сброс
    btn_continue.grid_forget()         # остановка отображения кнопки продолжить
    btn_start.grid(row=1, column=0, columnspan=2, sticky='we') # отображение кнопки старт

def continue_func():
    btn_reset.grid_forget()    # остановка отображения кнопки сброс
    btn_continue.grid_forget() # остановка отображения кнопки продолжить
    btn_stop.grid(row=1, column=0, columnspan=2, sticky='we')  # отображение кнопки стоп
    time_count()               # запуск рекурсивной функции time_count() для отсчета секунд


root = tk.Tk()
root.title('Секундомер')
root.resizable(False, False)

lab_screen = tk.Label(root, text='00:00', font=('Arial', 100), width=5)
btn_start = tk.Button(root, text='Start', bd=BD, font=('Arial', 30), command=start_func)
btn_stop = tk.Button(root, text='Stop', bd=BD, font=('Arial', 30), command=stop_func)
btn_reset = tk.Button(root, text='Reset', bd=BD, font=('Arial', 30), command=reset_func)
btn_continue = tk.Button(root, text='Continue', bd=BD, font=('Arial', 30), command=continue_func)

lab_screen.grid(row=0, column=0, columnspan=2, sticky='we')
btn_start.grid(row=1, column=0, columnspan=2, sticky='we')

root.mainloop()