```python
class Note:
    def __init__(self, noteName, noteContent, noteColor, noteFolder):
        self.noteName = noteName
        self.noteContent = noteContent
        self.noteColor = noteColor
        self.noteFolder = noteFolder

class Folder:
    def __init__(self, folderName, folderColor, notes):
        self.folderName = folderName
        self.folderColor = folderColor
        self.notes = notes

noteList = []

def createNote(noteName, noteContent, noteColor, noteFolder):
    newNote = Note(noteName, noteContent, noteColor, noteFolder)
    noteList.append(newNote)

def editNote(noteName, newContent):
    for note in noteList:
        if note.noteName == noteName:
            note.noteContent = newContent
            break

def deleteNote(noteName):
    for note in noteList:
        if note.noteName == noteName:
            noteList.remove(note)
            break

def reorderNotes(noteName1, noteName2):
    index1, index2 = None, None
    for i, note in enumerate(noteList):
        if note.noteName == noteName1:
            index1 = i
        elif note.noteName == noteName2:
            index2 = i
    if index1 is not None and index2 is not None:
        noteList[index1], noteList[index2] = noteList[index2], noteList[index1]
```