"""
Task Scheduler Module
Provides queue-based task scheduling with FIFO management.
"""

from data_structures.queue import Queue
from typing import Dict, List, Optional
from datetime import datetime

class Task:
    """Task class to store task information."""
    
    def __init__(self, title: str, description: str = "", priority: str = "Medium", deadline: str = ""):
        self.title = title
        self.description = description
        self.priority = priority  # Low, Medium, High
        self.deadline = deadline
        self.created_at = datetime.now()
        self.completed = False
        self.completed_at = None
    
    def __str__(self):
        status = "✅ Completed" if self.completed else "⏳ Pending"
        return f"{self.title} ({self.priority}) - {status}"
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for storage."""
        return {
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'deadline': self.deadline,
            'created_at': self.created_at.isoformat(),
            'completed': self.completed,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }
    
    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True
        self.completed_at = datetime.now()

class TaskScheduler:
    """
    Task scheduling system using queue for FIFO task management.
    """
    
    def __init__(self):
        """Initialize the task scheduler."""
        self.task_queue = Queue()
        self.completed_tasks = []
        self.total_tasks_created = 0
        self.total_tasks_completed = 0
        
        # Load sample tasks
        self.load_sample_tasks()
    
    def load_sample_tasks(self):
        """Load sample academic tasks."""
        sample_tasks = [
            Task("Study DSA", "Review graph algorithms and data structures", "High", "2024-01-15"),
            Task("Complete Assignment", "Finish programming assignment", "High", "2024-01-10"),
            Task("Attend Class", "Go to Data Structures lecture", "Medium", "2024-01-08"),
            Task("Prepare Presentation", "Create slides for project presentation", "Medium", "2024-01-20"),
            Task("Review Notes", "Go through lecture notes", "Low", "2024-01-12")
        ]
        
        for task in sample_tasks:
            self.add_task(task)
    
    def add_task(self, task: Task) -> bool:
        """
        Add a new task to the queue.
        
        Args:
            task: Task object to add
            
        Returns:
            True if task added successfully
        """
        if self.task_queue.enqueue(task):
            self.total_tasks_created += 1
            return True
        return False
    
    def complete_next_task(self) -> Optional[Task]:
        """
        Complete the next task in the queue (FIFO).
        
        Returns:
            Completed task, or None if queue is empty
        """
        task = self.task_queue.dequeue()
        if task:
            task.mark_completed()
            self.completed_tasks.append(task)
            self.total_tasks_completed += 1
            return task
        return None
    
    def peek_next_task(self) -> Optional[Task]:
        """
        View the next task without completing it.
        
        Returns:
            Next task, or None if queue is empty
        """
        return self.task_queue.peek()
    
    def get_pending_tasks(self) -> List[Task]:
        """Get all pending tasks in the queue."""
        return self.task_queue.to_list()
    
    def get_completed_tasks(self) -> List[Task]:
        """Get all completed tasks."""
        return self.completed_tasks.copy()
    
    def get_task_count(self) -> int:
        """Get the total number of pending tasks."""
        return self.task_queue.size()
    
    def get_completed_count(self) -> int:
        """Get the total number of completed tasks."""
        return len(self.completed_tasks)
    
    def get_total_created(self) -> int:
        """Get the total number of tasks created."""
        return self.total_tasks_created
    
    def clear_completed_tasks(self):
        """Clear the completed tasks list."""
        self.completed_tasks.clear()
    
    def get_task_statistics(self) -> Dict:
        """Get statistics about tasks."""
        pending = self.get_task_count()
        completed = self.get_completed_count()
        total = self.get_total_created()
        
        return {
            'pending': pending,
            'completed': completed,
            'total_created': total,
            'completion_rate': (completed / total * 100) if total > 0 else 0
        }
    
    def display_pending_tasks(self):
        """Display all pending tasks."""
        tasks = self.get_pending_tasks()
        
        if not tasks:
            print("\n✅ No pending tasks!")
            return
        
        print(f"\n⏳ PENDING TASKS ({len(tasks)} total)")
        print("=" * 60)
        
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.title}")
            print(f"   📝 Description: {task.description}")
            print(f"   ⚡ Priority: {task.priority}")
            if task.deadline:
                print(f"   📅 Deadline: {task.deadline}")
            print(f"   📅 Created: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
            print("-" * 40)
    
    def display_completed_tasks(self):
        """Display all completed tasks."""
        tasks = self.get_completed_tasks()
        
        if not tasks:
            print("\n📊 No completed tasks yet.")
            return
        
        print(f"\n✅ COMPLETED TASKS ({len(tasks)} total)")
        print("=" * 60)
        
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.title}")
            print(f"   📝 Description: {task.description}")
            print(f"   ⚡ Priority: {task.priority}")
            if task.deadline:
                print(f"   📅 Deadline: {task.deadline}")
            print(f"   ✅ Completed: {task.completed_at.strftime('%Y-%m-%d %H:%M')}")
            print("-" * 40)
    
    def display_statistics(self):
        """Display task statistics."""
        stats = self.get_task_statistics()
        
        print("\n📊 TASK STATISTICS")
        print("=" * 30)
        print(f"⏳ Pending Tasks: {stats['pending']}")
        print(f"✅ Completed Tasks: {stats['completed']}")
        print(f"📈 Total Created: {stats['total_created']}")
        print(f"📊 Completion Rate: {stats['completion_rate']:.1f}%")
        
        if stats['pending'] > 0:
            next_task = self.peek_next_task()
            if next_task:
                print(f"\n🎯 Next Task: {next_task.title}")
        
        print("=" * 30)
    
    def run_task_menu(self):
        """Run the task scheduler menu."""
        while True:
            print("\n✅ TASK SCHEDULER")
            print("=" * 30)
            print("1. ➕ Add New Task")
            print("2. ✅ Complete Next Task")
            print("3. 👀 View Next Task")
            print("4. 📋 View Pending Tasks")
            print("5. ✅ View Completed Tasks")
            print("6. 📊 View Statistics")
            print("7. 🗑️  Clear Completed Tasks")
            print("8. ↩️  Back to Main Menu")
            print("=" * 30)
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.add_task_menu()
            elif choice == "2":
                self.complete_task_menu()
            elif choice == "3":
                self.view_next_task()
            elif choice == "4":
                self.display_pending_tasks()
                input("Press Enter to continue...")
            elif choice == "5":
                self.display_completed_tasks()
                input("Press Enter to continue...")
            elif choice == "6":
                self.display_statistics()
                input("Press Enter to continue...")
            elif choice == "7":
                self.clear_completed_menu()
            elif choice == "8":
                break
            else:
                print("❌ Invalid choice. Please try again.")
    
    def add_task_menu(self):
        """Menu for adding a new task."""
        print("\n➕ ADD NEW TASK")
        print("=" * 30)
        
        title = input("Task Title: ").strip()
        if not title:
            print("❌ Title is required.")
            input("Press Enter to continue...")
            return
        
        description = input("Description (optional): ").strip()
        
        print("\nPriority Levels:")
        print("1. Low")
        print("2. Medium")
        print("3. High")
        
        try:
            priority_choice = int(input("Enter priority (1-3): "))
            if priority_choice == 1:
                priority = "Low"
            elif priority_choice == 2:
                priority = "Medium"
            elif priority_choice == 3:
                priority = "High"
            else:
                priority = "Medium"
        except ValueError:
            priority = "Medium"
        
        deadline = input("Deadline (YYYY-MM-DD, optional): ").strip()
        
        task = Task(title, description, priority, deadline)
        
        if self.add_task(task):
            print("✅ Task added successfully!")
        else:
            print("❌ Failed to add task.")
        
        input("Press Enter to continue...")
    
    def complete_task_menu(self):
        """Menu for completing the next task."""
        if self.task_queue.is_empty():
            print("✅ No pending tasks to complete!")
            input("Press Enter to continue...")
            return
        
        next_task = self.peek_next_task()
        print(f"\n✅ COMPLETE NEXT TASK")
        print("=" * 40)
        print(f"Next task: {next_task.title}")
        print(f"Description: {next_task.description}")
        print(f"Priority: {next_task.priority}")
        if next_task.deadline:
            print(f"Deadline: {next_task.deadline}")
        
        confirm = input("\nMark this task as completed? (y/N): ").strip().lower()
        if confirm == 'y':
            completed_task = self.complete_next_task()
            if completed_task:
                print(f"✅ Task '{completed_task.title}' completed successfully!")
            else:
                print("❌ Failed to complete task.")
        else:
            print("❌ Task completion cancelled.")
        
        input("Press Enter to continue...")
    
    def view_next_task(self):
        """View the next task without completing it."""
        if self.task_queue.is_empty():
            print("✅ No pending tasks!")
            input("Press Enter to continue...")
            return
        
        next_task = self.peek_next_task()
        print(f"\n👀 NEXT TASK")
        print("=" * 30)
        print(f"Title: {next_task.title}")
        print(f"Description: {next_task.description}")
        print(f"Priority: {next_task.priority}")
        if next_task.deadline:
            print(f"Deadline: {next_task.deadline}")
        print(f"Created: {next_task.created_at.strftime('%Y-%m-%d %H:%M')}")
        print("=" * 30)
        
        input("Press Enter to continue...")
    
    def clear_completed_menu(self):
        """Menu for clearing completed tasks."""
        if not self.completed_tasks:
            print("📊 No completed tasks to clear.")
            input("Press Enter to continue...")
            return
        
        print(f"\n🗑️  CLEAR COMPLETED TASKS")
        print("=" * 40)
        print(f"You have {len(self.completed_tasks)} completed tasks.")
        
        confirm = input("Are you sure you want to clear all completed tasks? (y/N): ").strip().lower()
        if confirm == 'y':
            self.clear_completed_tasks()
            print("✅ Completed tasks cleared successfully!")
        else:
            print("❌ Clear operation cancelled.")
        
        input("Press Enter to continue...")
