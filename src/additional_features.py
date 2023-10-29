```python
import os
import shutil
from PIL import Image

# Global shortcuts
def register_global_shortcuts():
    # This function will register global shortcuts for the app
    # The implementation will depend on the platform and the library used for global shortcuts
    pass

# Exporting notes to images
def export_note_to_image(note):
    # Convert note text to image using PIL library
    note_image = Image.new('RGB', (500, 500), color = (73, 109, 137))
    d = ImageDraw.Draw(note_image)
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
    d.text((10,10), note.noteContent, font=fnt, fill=(255, 255, 0))
    note_image.save(note.noteName + '.png')

# Note and folder URLs
def get_note_url(note):
    # This function will return a URL for the given note
    # The implementation will depend on the way notes are stored and accessed
    pass

def get_folder_url(folder):
    # This function will return a URL for the given folder
    # The implementation will depend on the way folders are stored and accessed
    pass

# Importing text files
def import_text_file(file_path):
    # Check if file exists
    if not os.path.isfile(file_path):
        print("File path {} does not exist. Exiting...".format(file_path))
        sys.exit()

    # Read the file
    with open(file_path, 'r') as file:
        note_content = file.read()

    # Create a new note with the content of the file
    new_note = Note(noteName=os.path.basename(file_path), noteContent=note_content)
    noteList.append(new_note)
```