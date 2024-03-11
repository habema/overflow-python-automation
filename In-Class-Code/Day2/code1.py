import tkinter as tk

window = tk.Tk()
window.title('My First GUI')
window.geometry('400x300')

def on_click():
    name = entry_1.get()
    label_1.config(text = f'Hello {name}!')

label_1 = tk.Label(
    window,
    text = 'Hello World',
    font = ('Courier', 20, 'bold'),
    foreground = '#691dcc'
)

entry_1 = tk.Entry(
    window,
)

button_1 = tk.Button(
    window,
    text = 'Submit',
    command = on_click
)

label_1.pack()
entry_1.pack()
button_1.pack()

window.mainloop()