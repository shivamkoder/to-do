class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks, 1):
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

    def mark_done(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["done"] = True
            print(f"Task {index} marked as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as done: "))
            todo.mark_done(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            todo.delete_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
