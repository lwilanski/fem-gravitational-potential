import tkinter as tk
from tkinter import messagebox

from solve import solve
from plot import show


class App:
    def __init__(self) -> None:
        self.root = tk.Tk()

        self.root.minsize(600, 300)
        self.root.maxsize(600, 300)

        self.label = tk.Label(self.root, text="Gravitational potential FEM", font=('Arial', 22))
        self.label.pack(padx=10, pady=40)

        self.label = tk.Label(self.root, text="Enter value for n")
        self.label.pack(side='top')

        self.entry = tk.Entry(self.root, justify='center')
        self.entry.pack(side='top')

        self.button = tk.Button(self.root, justify='center', text="confirm", height=1, width=10, command=self.solve)
        self.button.pack(padx=10, pady=47)

        self.root.mainloop()

    def solve(self):
        try:
            n = int(self.entry.get())
            if n <= 2:
                raise Exception("n must be greater than 2")

            x, y = solve(n)
            show(x, y, n)
        except Exception as e:
            messagebox.showwarning(title="Error", message=f"Something went wrong: {e}")

