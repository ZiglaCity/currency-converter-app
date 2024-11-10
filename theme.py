import tkinter as tk
#define a fixed style to be used for all the widgets
label_style = {
    "font": ("Arial", 14, "italic"),
    "bg": "#e6e6e6",
    "fg": "#2b2b2b",
    "padx": 8,
    "pady": 8
}

button_style = {
    "font": ("Comic Sans MS", 12, "bold"),
    "bg": "#BBBBBB",
    "fg": "#333333",
    "bd": 3,
    "relief": "ridge"
}

entry_style = {
    "font": ("Times New Roman", 12),
    "bg": "#ffffff",
    "fg": "#000000",
    "bd": 2,
    "relief": "solid"
}
#DAA520
frame_style = {
    "bg": "#e0e0e0",
    "bd": 2,
    "relief": "sunken"
}
listbox_style = {
    'bg': '#f0f0f0',         # Background color
    'fg': '#333333',         # Text color
    'font': ('Arial', 12),   # Font type and size
    'highlightbackground': '#cccccc',  # Border color when the listbox is not in focus
    'highlightthickness': 1, # Border thickness
    'selectbackground': '#0078d4',  # Background color when an item is selected
    'selectforeground': '#ffffff',  # Text color when an item is selected
    'width': 100,             # Width of the listbox (number of characters)
    'height': 15  # Number of visible lines
}
scrollbar_style = {
    'bg': '#dddddd',         # Background color of the scrollbar
    'troughcolor': '#cccccc',# Color of the trough (the area the slider moves within)
    'width': 15              # Width of the scrollbar
}



#define a funciton which applies the styles to their respective widgets
def apply_styles(widget):
    #Apply styles to all Button, Label, Entry, and Frame widgets
    if isinstance(widget, tk.Button):
        widget.config(**button_style)
    elif isinstance(widget, tk.Label):
        widget.config(**label_style)
    elif isinstance(widget, tk.Entry):
        widget.config(**entry_style)
    elif isinstance(widget, tk.Frame):
        widget.config(**frame_style)
    elif isinstance(widget, tk.Listbox):
        widget.config(**listbox_style)
    elif isinstance(widget, tk.Scrollbar):
        widget.config(**scrollbar_style)

    # Recursively apply styles to all children
    for child in widget.winfo_children():
        apply_styles(child)

