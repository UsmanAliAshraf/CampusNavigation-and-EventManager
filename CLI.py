import os
import sys
from typing import Optional

class CampusConnectCLI:
    """
    Command Line Interface for Campus Connect application.
    Provides menu-driven access to all modules.
    """
    
    def __init__(self):
        """Initialize the CLI interface."""
        self.running = True
        self.current_module = None
        
        # Import modules
        from navigator import CampusNavigator
        from events_manager import EventsManager
        from task_scheduler import TaskScheduler
        from event_search_tree import EventSearchTree
        
        self.navigator = CampusNavigator()
        self.events_manager = EventsManager()
        self.task_scheduler = TaskScheduler()
        self.event_search_tree = EventSearchTree()
    
    def run(self):
        """Main CLI loop."""
        while self.running:
            self.display_main_menu()
            choice = self.get_user_input("Enter your choice: ")
            self.handle_main_menu_choice(choice)
    
    def display_main_menu(self):
        """Display the main menu."""
        print("\n" + "=" * 50)
        print("🏫 CAMPUS CONNECT - MAIN MENU")
        print("=" * 50)
        print("1. 🗺️  Campus Navigator")
        print("2. 📅 Event Manager")
        print("3. ✅ Task Scheduler")
        print("4. 🔍 Event Search Tree")
        print("5. ℹ️  About")
        print("6. 🚪 Exit")
        print("=" * 50)
    
    def handle_main_menu_choice(self, choice: str):
        """Handle user choice from main menu."""
        if choice == "1":
            self.open_campus_navigator()
        elif choice == "2":
            self.open_event_manager()
        elif choice == "3":
            self.open_task_scheduler()
        elif choice == "4":
            self.open_event_search_tree()
        elif choice == "5":
            self.show_about()
        elif choice == "6":
            self.exit_application()
        else:
            print("❌ Invalid choice. Please try again.")
    
    def open_campus_navigator(self):
        """Open the Campus Navigator module."""
        self.navigator.run_navigation_menu()
    
    def open_event_manager(self):
        """Open the Event Manager module."""
        self.events_manager.run_events_menu()
    
    def open_task_scheduler(self):
        """Open the Task Scheduler module."""
        self.task_scheduler.run_task_menu()
    
    def open_event_search_tree(self):
        """Open the Event Search Tree module."""
        self.event_search_tree.run_search_menu()
    
    def show_about(self):
        """Show information about the application."""
        print("\n" + "=" * 50)
        print("ℹ️  ABOUT CAMPUS CONNECT")
        print("=" * 50)
        print("Campus Connect Navigation & Event Planner System")
        print("A comprehensive system for UET students to:")
        print("• Navigate campus using graph algorithms")
        print("• Manage events with linked lists and stacks")
        print("• Schedule tasks using queues")
        print("• Search events efficiently with binary trees")
        print("\nData Structures & Algorithms Project")
        print("Demonstrates real-world application of DSA concepts.")
        print("=" * 50)
        input("Press Enter to continue...")
    
    def exit_application(self):
        """Exit the application."""
        print("\n👋 Thank you for using Campus Connect!")
        print("Goodbye! 👋")
        self.running = False
    
    def get_user_input(self, prompt: str) -> str:
        """Get user input with error handling."""
        try:
            return input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            self.exit_application()
            return ""
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_module_menu(self, module_name: str, options: list):
        """Display a module-specific menu."""
        print(f"\n{module_name}")
        print("=" * 30)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print(f"{len(options) + 1}. ↩️  Back to Main Menu")
        print("=" * 30)
    
    def get_module_choice(self, max_options: int) -> Optional[int]:
        """Get user choice for module menu."""
        try:
            choice = int(self.get_user_input("Enter your choice: "))
            if 1 <= choice <= max_options:
                return choice
            elif choice == max_options + 1:
                return None  # Back to main menu
            else:
                print("❌ Invalid choice. Please try again.")
                return self.get_module_choice(max_options)
        except ValueError:
            print("❌ Please enter a valid number.")
            return self.get_module_choice(max_options)
