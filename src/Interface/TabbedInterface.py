import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tabbed Interface")
root.geometry("400x300")


tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Tab 1")
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both")


# Create a Label
ttk.Label(tab1, text="This is a Label On Tab 1").grid(column=0, row=0)
ttk.Label(tab2, text="This is a Label On Tab 2").grid(column=0, row=0)

root.mainloop()