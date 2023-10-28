```python
class Note:
    def __init__(self, noteName, noteContent, noteColor, noteFolder):
        self.noteName = noteName
        self.noteContent = noteContent
        self.noteColor = noteColor
        self.noteFolder = noteFolder

class NoteCanvas:
    def __init__(self):
        self.noteList = []

    def create_or_append_note(self, noteName, noteContent, noteColor="white", noteFolder="default"):
        for note in self.noteList:
            if note.noteName == noteName:
                note.noteContent += "\n" + noteContent
                return
        new_note = Note(noteName, noteContent, noteColor, noteFolder)
        self.noteList.append(new_note)

    def get_note_content(self, noteName):
        for note in self.noteList:
            if note.noteName == noteName:
                return note.noteContent
        return None

    def delete_note(self, noteName):
        for note in self.noteList:
            if note.noteName == noteName:
                self.noteList.remove(note)
                return True
        return False
```