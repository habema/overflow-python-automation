import os
import shutil
import tkinter as tk
from tkinter import filedialog


window = tk.Tk()
window.title('My First GUI')
window.geometry('600x300')

def organize():
    root = folder_path.get()
    print(root)
    try:
        files = os.listdir(root)
    except FileNotFoundError:
        label_2.config(text = 'Please enter a valid directory')
        return


    for f in files:
        if '.' not in f:
            continue

        ext = f.split('.')[-1]
        # ext = os.path.splitext(f)[1].replace('.', '')
        
        # if os.path.exists(os.path.join(root, ext)):
        #     shutil.move(os.path.join(root, f), os.path.join(root, ext, f) )
        # else:
        #     os.mkdir(os.path.join(root, ext))
        #     shutil.move(os.path.join(root, f), os.path.join(root, ext, f) )

        if not os.path.exists(os.path.join(root, ext)):
            os.mkdir(os.path.join(root, ext))
        shutil.move(os.path.join(root, f), os.path.join(root, ext, f) )

    label_2.config(text = 'Success!')



label_1 = tk.Label(
    window,
    text = 'Welcome to the directory organizer',
    font = ('Courier', 20, 'bold'),
    foreground = '#691dcc'
)

label_2 = tk.Label(
    window,
    text = 'Please enter a directory',
    font = ('Courier', 15),
    foreground = '#691dcc'
)

# entry_1 = tk.Entry(
#     window,
#     width = 80
# )

button_1 = tk.Button(
    window,
    text = 'Submit',
    command = organize
)

def browse_button():
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


folder_path = tk.StringVar()
button2 = tk.Button(text="Browse", command=browse_button)

label_1.pack(pady=10)
label_2.pack(pady=5)
# entry_1.pack(pady=5)
button2.pack()
button_1.pack(pady=5)

window.mainloop()