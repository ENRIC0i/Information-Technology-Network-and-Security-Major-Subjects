# Programmed by: Abenes, Enrico O.
# Program Date: November 8, 2023
# Program Title: Add/Delete Widget

import tkinter as GUI


# --- Model ---

note_list = []


# --- Controller ---

def add_func():
    new_text_widget = GUI.Text(root, height=10, width=30)
    new_text_widget.pack()
    note_list.append(new_text_widget)

def delete_func():
    if note_list:
        last_text_widget = note_list.pop()
        last_text_widget.pack_forget()


# --- View ---

root = GUI.Tk()
root.title("Note")

add_button = GUI.Button(root, text="Add New Button", command=add_func)
add_button.pack()

delete_button = GUI.Button(root, text="Delete Last Note", command=delete_func)
delete_button.pack()

root.mainloop()