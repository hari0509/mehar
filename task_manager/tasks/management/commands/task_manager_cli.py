from django.core.management.base import BaseCommand
from tasks.models import Task
from django.utils.text import capfirst

class Command(BaseCommand):
    help = 'Command-line interface for Task Manager application'

    def handle(self, *args, **kwargs):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.edit_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.view_all_tasks()
            elif choice == '5':
                self.filter_tasks_by_priority()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

    def print_menu(self):
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Filter Tasks by Priority")
        print("6. Exit")

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        priority = input("Enter task priority (High/Medium/Low): ").capitalize()
        status = input("Enter task status (Pending/In Progress/Completed): ").capitalize()
        Task.objects.create(title=title, description=description, priority=priority, status=status)
        print("Task added successfully!")

    def edit_task(self):
        task_id = int(input("Enter task ID to edit: "))
        try:
            task = Task.objects.get(id=task_id)
            title = input(f"Enter new title (current: {task.title}): ") or task.title
            description = input(f"Enter new description (current: {task.description}): ") or task.description
            priority = input(f"Enter new priority (current: {task.priority}): ").capitalize() or task.priority
            status = input(f"Enter new status (current: {task.status}): ").capitalize() or task.status
            task.title = title
            task.description = description
            task.priority = priority
            task.status = status
            task.save()
            print("Task updated successfully!")
        except Task.DoesNotExist:
            print("Task not found.")

    def delete_task(self):
        task_id = int(input("Enter task ID to delete: "))
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            print("Task deleted successfully!")
        except Task.DoesNotExist:
            print("Task not found.")

    def view_all_tasks(self):
        tasks = Task.objects.all()
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Priority: {task.priority}, Status: {task.status}")

    def filter_tasks_by_priority(self):
        priority = input("Enter priority to filter by (High/Medium/Low): ").capitalize()
        tasks = Task.objects.filter(priority=priority)
        if not tasks:
            print("No tasks found with the given priority.")
            return
        for task in tasks:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Priority: {task.priority}, Status: {task.status}")
