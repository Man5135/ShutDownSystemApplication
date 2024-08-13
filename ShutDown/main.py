import tkinter as tk
import os

def shutdown_pc():
    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())
    total_seconds = hours * 3600 + minutes * 60 + seconds
    os.system(f'shutdown /s /t {total_seconds}')

# Создаем графический интерфейс
root = tk.Tk(className="ShutDown")
root.configure(bg ='black')
root.geometry("300x200")

label = tk.Label(root, text="Insert the time to shut down:")
label.pack()

hours_label = tk.Label(root, text="Hours:")
hours_label.pack()
hours_entry = tk.Entry(root)
hours_entry.pack()

minutes_label = tk.Label(root, text="Minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()

seconds_label = tk.Label(root, text="Seconds:")
seconds_label.pack()
seconds_entry = tk.Entry(root)
seconds_entry.pack()

button = tk.Button(root, text="Turn off your PC", command=shutdown_pc)
button.pack()

root.mainloop()