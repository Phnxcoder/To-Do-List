import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def mark_complete():
    try:
        selected_task = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)
        task_listbox.insert(tk.END, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as complete!")

# Main Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg="lightgray")

# UI Elements
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

complete_button = tk.Button(root, text="Mark Complete", command=mark_complete)
complete_button.pack()

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Run the App
root.mainloop()