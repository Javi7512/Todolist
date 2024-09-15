import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        
        self.task_input = tk.Entry(root)
        self.task_input.pack()
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()
        
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_input.delete(0, tk.END)

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to complete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
