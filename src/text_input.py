```python
import tkinter as tk
from src.note_canvas import NoteCanvas

class TextInput:
    def __init__(self, root):
        self.root = root
        self.text_input = tk.Text(self.root)
        self.text_input.bind('<Return>', self.handle_return)

    def handle_return(self, event):
        text = self.text_input.get('1.0', 'end-1c')
        if text.startswith('@'):
            note_name = text[1:]
            self.create_or_append_to_note(note_name)
        self.text_input.delete('1.0', 'end')

    def create_or_append_to_note(self, note_name):
        if note_name in NoteCanvas.noteList:
            NoteCanvas.currentNote = NoteCanvas.noteList[note_name]
        else:
            NoteCanvas.currentNote = NoteCanvas.create_note(note_name)
        NoteCanvas.noteList[note_name] = NoteCanvas.currentNote
        NoteCanvas.currentNote.append_text(self.text_input.get('1.0', 'end-1c'))

    def enable_multiline_entry(self):
        self.text_input.config(state='normal')

    def disable_multiline_entry(self):
        self.text_input.config(state='disabled')
```