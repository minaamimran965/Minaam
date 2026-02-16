import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        # Insert task at the end of the listbox
        listbox_tasks.insert(tk.END, task)
        # Clear the entry box for the next task
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        # Get the index of the selected item
        selected_task_index = listbox_tasks.curselection()[0]
        # Delete the item at that index
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    # Remove all items from index 0 to the end
    listbox_tasks.delete(0, tk.END)

# Setup main window
root = tk.Tk()
root.title("Simple To-Do List")

# GUI Elements
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=35, command=add_task)
add_button.pack(pady=5)

listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

delete_button = tk.Button(root, text="Delete Selected Task", width=35, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=35, command=clear_tasks)
clear_button.pack(pady=5)

root.mainloop()
