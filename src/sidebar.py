```python
import tkinter as tk

# Global variable to track the status of the sidebar
sidebarStatus = False

def toggleSidebar():
    global sidebarStatus
    if sidebarStatus:
        sidebar.pack_forget()
        sidebarStatus = False
    else:
        sidebar.pack(side="left", fill="y")
        sidebarStatus = True

def createSidebar(root):
    global sidebar
    sidebar = tk.Frame(root, width=200, bg='white', relief='sunken', borderwidth=2)
    sidebar.pack(side="left", fill="y")

    toggleButton = tk.Button(sidebar, text="Toggle Sidebar", command=toggleSidebar)
    toggleButton.pack()

def moveSidebar(position):
    global sidebar
    sidebar.pack_forget()
    sidebar.pack(side=position, fill="y")

root = tk.Tk()
createSidebar(root)
root.mainloop()
```