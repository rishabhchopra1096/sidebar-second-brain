```python
import os
import json
import icloud
from note_management import noteList

syncStatus = False

def sync_notes():
    global syncStatus
    if not syncStatus:
        try:
            icloud.login(os.getenv('ICLOUD_USERNAME'), os.getenv('ICLOUD_PASSWORD'))
            syncStatus = True
        except Exception as e:
            print(f"Error logging into iCloud: {e}")
            return

    try:
        icloud.put('notes_backup.json', json.dumps(noteList))
        print("Notes successfully synced to iCloud.")
    except Exception as e:
        print(f"Error syncing notes to iCloud: {e}")

def load_notes():
    global syncStatus
    if not syncStatus:
        try:
            icloud.login(os.getenv('ICLOUD_USERNAME'), os.getenv('ICLOUD_PASSWORD'))
            syncStatus = True
        except Exception as e:
            print(f"Error logging into iCloud: {e}")
            return

    try:
        noteList = json.loads(icloud.get('notes_backup.json'))
        print("Notes successfully loaded from iCloud.")
    except Exception as e:
        print(f"Error loading notes from iCloud: {e}")

def backup_notes():
    try:
        with open('notes_backup.json', 'w') as f:
            json.dump(noteList, f)
        print("Notes successfully backed up locally.")
    except Exception as e:
        print(f"Error backing up notes locally: {e}")
```