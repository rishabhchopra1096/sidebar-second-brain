```python
import tkinter as tk
from tkinter import ttk
from sidebar import Sidebar
from note_canvas import NoteCanvas
from text_input import TextInput

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sidebar Notes App")
        self.sidebar = Sidebar(self.root)
        self.note_canvas = NoteCanvas(self.root)
        self.text_input = TextInput(self.root)
        self.theme = tk.StringVar(value="light")

    def toggle_theme(self):
        if self.theme.get() == "light":
            self.theme.set("dark")
        else:
            self.theme.set("light")
        self.root.configure(bg=self.theme.get())

    def create_theme_toggle(self):
        theme_toggle = ttk.Checkbutton(
            self.root,
            text="Toggle Theme",
            variable=self.theme,
            command=self.toggle_theme
        )
        theme_toggle.pack()

    def run(self):
        self.create_theme_toggle()
        self.root.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
```