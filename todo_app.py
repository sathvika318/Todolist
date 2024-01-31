import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.configure(bg="black")  # Set background color to black

        # Task list
        self.tasks = []

        # Heading for new task entry
        tk.Label(root, text="New Task:", fg="white", bg="black").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        # Entry for new task
        self.task_entry = tk.Entry(root, width=40, bg="white", fg="black", insertbackground="black")
        self.task_entry.grid(row=1, column=0, padx=10, pady=10)

        # Heading for due date entry
        tk.Label(root, text="Due Date:", fg="white", bg="black").grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Due date entry
        self.due_date_entry = tk.Entry(root, width=20, bg="white", fg="black", insertbackground="black")
        self.due_date_entry.insert(0, "YYYY-MM-DD")  # Placeholder
        self.due_date_entry.grid(row=1, column=1, padx=10, pady=10)
        self.due_date_entry.bind("<FocusIn>", self.on_due_date_focus_in)  # Bind focus event

        # Buttons
        add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="white", fg="black")
        add_button.grid(row=1, column=2, padx=10, pady=10)

        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg="white", fg="black")
        remove_button.grid(row=2, column=0, padx=10, pady=10)

        complete_button = tk.Button(root, text="Complete Task", command=self.complete_task, bg="white", fg="black")
        complete_button.grid(row=2, column=1, padx=10, pady=10)

        clear_button = tk.Button(root, text="Clear All", command=self.clear_all, bg="white", fg="black")
        clear_button.grid(row=2, column=2, padx=10, pady=10)

        # Heading for task list
        tk.Label(root, text="Task List:", fg="white", bg="black").grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky=tk.W)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50, bg="white", fg="black")
        self.task_listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    def on_due_date_focus_in(self, event):
        # Clear the placeholder text when the user clicks on the "Due Date" entry
        if self.due_date_entry.get() == "YYYY-MM-DD":
            self.due_date_entry.delete(0, tk.END)
            self.due_date_entry.config(fg="black")  # Change text color to black

    def add_task(self):
        new_task = self.task_entry.get()
        due_date_str = self.due_date_entry.get()

        if new_task:
            due_date = None
            if due_date_str and self.is_valid_date(due_date_str):
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()

            task_info = {"task": new_task, "due_date": due_date, "completed": False}
            self.tasks.append(task_info)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
            self.due_date_entry.insert(0, "YYYY-MM-DD")  # Reset placeholder
            self.due_date_entry.config(fg="black")  # Change text color to black
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_list()

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]["completed"] = True
            self.update_task_list()

    def clear_all(self):
        self.tasks = []
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task_info in enumerate(self.tasks, start=1):
            task_display = f"{idx}. {task_info['task']}"
            if task_info["due_date"]:
                task_display += f" (Due: {task_info['due_date']})"
            if task_info["completed"]:
                task_display = f"✅ {task_display}"
            self.task_listbox.insert(tk.END, task_display)

    @staticmethod
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
