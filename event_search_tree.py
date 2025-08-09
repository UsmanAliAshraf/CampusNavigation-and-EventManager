"""
Event Search Tree Module
Provides efficient event searching using binary search trees.
"""

from data_structures.binary_tree import BinarySearchTree
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class EventNode:
    """Event node for binary search tree."""
    
    def __init__(self, event_id: str, title: str, date: str, time: str, location: str, 
                 category: str = "General", priority: str = "Medium", description: str = ""):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.category = category
        self.priority = priority
        self.description = description
        self.created_at = datetime.now()
    
    def __str__(self):
        return f"{self.title} ({self.category}) - {self.date} at {self.time}"
    
    def to_dict(self) -> Dict:
        """Convert event to dictionary for storage."""
        return {
            'event_id': self.event_id,
            'title': self.title,
            'date': self.date,
            'time': self.time,
            'location': self.location,
            'category': self.category,
            'priority': self.priority,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }
    
    def get_search_key(self) -> str:
        """Get the key used for searching (title + date)."""
        return f"{self.title.lower()}_{self.date}"

class EventSearchTree:
    """
    Event search system using binary search tree for efficient searching.
    """
    
    def __init__(self):
        """Initialize the event search tree."""
        self.bst = BinarySearchTree()
        self.event_counter = 0
        self.categories = set()
        self.priorities = {"Low", "Medium", "High"}
        
        # Load sample events
        self.load_sample_events()
    
    def load_sample_events(self):
        """Load sample events for demonstration."""
        sample_events = [
            ("Mid Exam", "2024-01-15", "10:00", "CS Department", "Academic", "High", "Data Structures mid-term exam"),
            ("Viva", "2024-01-20", "14:00", "Lab 3", "Academic", "High", "Project viva presentation"),
            ("Presentation", "2024-01-25", "11:00", "Auditorium", "Academic", "Medium", "Final project presentation"),
            ("Sports Day", "2024-02-01", "09:00", "Sports Complex", "Event", "Medium", "Annual sports competition"),
            ("Library Visit", "2024-01-12", "15:00", "Library", "Study", "Low", "Research for assignment"),
            ("Group Meeting", "2024-01-18", "16:00", "Cafeteria", "Meeting", "Medium", "Project group discussion"),
            ("Workshop", "2024-01-30", "13:00", "Lab 2", "Workshop", "Medium", "Programming workshop"),
            ("Cultural Event", "2024-02-05", "18:00", "Auditorium", "Event", "Low", "Cultural performance")
        ]
        
        for title, date, time, location, category, priority, description in sample_events:
            self.add_event(title, date, time, location, category, priority, description)
    
    def generate_event_id(self) -> str:
        """Generate a unique event ID."""
        self.event_counter += 1
        return f"EVT_{self.event_counter:04d}"
    
    def add_event(self, title: str, date: str, time: str, location: str, 
                  category: str = "General", priority: str = "Medium", description: str = "") -> bool:
        """
        Add a new event to the search tree.
        
        Args:
            title: Event title
            date: Event date
            time: Event time
            location: Event location
            category: Event category
            priority: Event priority
            description: Event description
            
        Returns:
            True if event added successfully
        """
        event_id = self.generate_event_id()
        event = EventNode(event_id, title, date, time, location, category, priority, description)
        
        # Use title + date as search key
        search_key = event.get_search_key()
        
        if self.bst.insert(search_key, event):
            self.categories.add(category)
            return True
        return False
    
    def search_by_title(self, title: str) -> List[EventNode]:
        """
        Search events by title.
        
        Args:
            title: Title to search for
            
        Returns:
            List of matching events
        """
        results = []
        all_events = self.bst.inorder_traversal()
        
        for key, event in all_events:
            if title.lower() in event.title.lower():
                results.append(event)
        
        return results
    
    def search_by_date(self, date: str) -> List[EventNode]:
        """
        Search events by date.
        
        Args:
            date: Date to search for
            
        Returns:
            List of matching events
        """
        results = []
        all_events = self.bst.inorder_traversal()
        
        for key, event in all_events:
            if event.date == date:
                results.append(event)
        
        return results
    
    def search_by_category(self, category: str) -> List[EventNode]:
        """
        Search events by category.
        
        Args:
            category: Category to search for
            
        Returns:
            List of matching events
        """
        results = []
        all_events = self.bst.inorder_traversal()
        
        for key, event in all_events:
            if event.category.lower() == category.lower():
                results.append(event)
        
        return results
    
    def search_by_priority(self, priority: str) -> List[EventNode]:
        """
        Search events by priority.
        
        Args:
            priority: Priority to search for
            
        Returns:
            List of matching events
        """
        results = []
        all_events = self.bst.inorder_traversal()
        
        for key, event in all_events:
            if event.priority.lower() == priority.lower():
                results.append(event)
        
        return results
    
    def search_by_location(self, location: str) -> List[EventNode]:
        """
        Search events by location.
        
        Args:
            location: Location to search for
            
        Returns:
            List of matching events
        """
        results = []
        all_events = self.bst.inorder_traversal()
        
        for key, event in all_events:
            if location.lower() in event.location.lower():
                results.append(event)
        
        return results
    
    def get_all_events(self) -> List[EventNode]:
        """Get all events in sorted order."""
        all_events = self.bst.inorder_traversal()
        return [event for key, event in all_events]
    
    def get_event_count(self) -> int:
        """Get the total number of events."""
        return self.bst.get_size()
    
    def get_categories(self) -> List[str]:
        """Get all available categories."""
        return sorted(list(self.categories))
    
    def get_priorities(self) -> List[str]:
        """Get all available priorities."""
        return sorted(list(self.priorities))
    
    def delete_event(self, event_id: str) -> bool:
        """
        Delete an event by ID.
        
        Args:
            event_id: ID of event to delete
            
        Returns:
            True if deletion successful
        """
        all_events = self.bst.inorder_traversal()
        
        for key, event in all_events:
            if event.event_id == event_id:
                return self.bst.delete(key)
        
        return False
    
    def get_events_by_date_range(self, start_date: str, end_date: str) -> List[EventNode]:
        """
        Get events within a date range.
        
        Args:
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            
        Returns:
            List of events in date range
        """
        results = []
        all_events = self.bst.inorder_traversal()
        
        for key, event in all_events:
            if start_date <= event.date <= end_date:
                results.append(event)
        
        return results
    
    def get_upcoming_events(self, days: int = 7) -> List[EventNode]:
        """
        Get upcoming events within specified days.
        
        Args:
            days: Number of days to look ahead
            
        Returns:
            List of upcoming events
        """
        from datetime import datetime, timedelta
        
        today = datetime.now().date()
        end_date = (today + timedelta(days=days)).strftime("%Y-%m-%d")
        today_str = today.strftime("%Y-%m-%d")
        
        return self.get_events_by_date_range(today_str, end_date)
    
    def display_events(self, events: List[EventNode], title: str = "EVENTS"):
        """Display a list of events."""
        if not events:
            print(f"\n📅 No {title.lower()} found.")
            return
        
        print(f"\n📅 {title} ({len(events)} total)")
        print("=" * 80)
        
        for i, event in enumerate(events, 1):
            print(f"{i}. {event.title}")
            print(f"   📅 Date: {event.date}")
            print(f"   ⏰ Time: {event.time}")
            print(f"   📍 Location: {event.location}")
            print(f"   🏷️  Category: {event.category}")
            print(f"   ⚡ Priority: {event.priority}")
            print(f"   🆔 ID: {event.event_id}")
            if event.description:
                print(f"   📝 Description: {event.description}")
            print("-" * 50)
    
    def display_tree_info(self):
        """Display information about the search tree."""
        print("\n🌳 EVENT SEARCH TREE INFO")
        print("=" * 40)
        print(f"📊 Total Events: {self.get_event_count()}")
        print(f"🌲 Tree Height: {self.bst.get_height()}")
        print(f"⚖️  Balanced: {'Yes' if self.bst.is_balanced() else 'No'}")
        print(f"🏷️  Categories: {', '.join(self.get_categories())}")
        print(f"⚡ Priorities: {', '.join(self.get_priorities())}")
        print("=" * 40)
    
    def run_search_menu(self):
        """Run the event search tree menu."""
        while True:
            print("\n🔍 EVENT SEARCH TREE")
            print("=" * 30)
            print("1. ➕ Add New Event")
            print("2. 📋 View All Events")
            print("3. 🔍 Search by Title")
            print("4. 📅 Search by Date")
            print("5. 🏷️  Search by Category")
            print("6. ⚡ Search by Priority")
            print("7. 📍 Search by Location")
            print("8. 📅 Upcoming Events")
            print("9. 🗑️  Delete Event")
            print("10. 📊 Tree Information")
            print("11. ↩️  Back to Main Menu")
            print("=" * 30)
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.add_event_menu()
            elif choice == "2":
                self.display_events(self.get_all_events(), "ALL EVENTS")
                input("Press Enter to continue...")
            elif choice == "3":
                self.search_by_title_menu()
            elif choice == "4":
                self.search_by_date_menu()
            elif choice == "5":
                self.search_by_category_menu()
            elif choice == "6":
                self.search_by_priority_menu()
            elif choice == "7":
                self.search_by_location_menu()
            elif choice == "8":
                self.upcoming_events_menu()
            elif choice == "9":
                self.delete_event_menu()
            elif choice == "10":
                self.display_tree_info()
                input("Press Enter to continue...")
            elif choice == "11":
                break
            else:
                print("❌ Invalid choice. Please try again.")
    
    def add_event_menu(self):
        """Menu for adding a new event."""
        print("\n➕ ADD NEW EVENT")
        print("=" * 30)
        
        title = input("Event Title: ").strip()
        if not title:
            print("❌ Title is required.")
            input("Press Enter to continue...")
            return
        
        date = input("Date (YYYY-MM-DD): ").strip()
        time = input("Time (HH:MM): ").strip()
        location = input("Location: ").strip()
        
        if not date or not time or not location:
            print("❌ Date, time, and location are required.")
            input("Press Enter to continue...")
            return
        
        print("\nAvailable Categories:")
        categories = self.get_categories()
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        print(f"{len(categories) + 1}. General")
        
        try:
            cat_choice = int(input("Enter category number: ")) - 1
            if 0 <= cat_choice < len(categories):
                category = categories[cat_choice]
            else:
                category = "General"
        except ValueError:
            category = "General"
        
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
        
        description = input("Description (optional): ").strip()
        
        if self.add_event(title, date, time, location, category, priority, description):
            print("✅ Event added successfully!")
        else:
            print("❌ Failed to add event.")
        
        input("Press Enter to continue...")
    
    def search_by_title_menu(self):
        """Menu for searching by title."""
        print("\n🔍 SEARCH BY TITLE")
        print("=" * 30)
        
        title = input("Enter title keyword: ").strip()
        if not title:
            print("❌ Please enter a title keyword.")
            input("Press Enter to continue...")
            return
        
        results = self.search_by_title(title)
        self.display_events(results, f"EVENTS CONTAINING '{title}'")
        input("Press Enter to continue...")
    
    def search_by_date_menu(self):
        """Menu for searching by date."""
        print("\n📅 SEARCH BY DATE")
        print("=" * 30)
        
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if not date:
            print("❌ Please enter a date.")
            input("Press Enter to continue...")
            return
        
        results = self.search_by_date(date)
        self.display_events(results, f"EVENTS ON {date}")
        input("Press Enter to continue...")
    
    def search_by_category_menu(self):
        """Menu for searching by category."""
        print("\n🏷️  SEARCH BY CATEGORY")
        print("=" * 30)
        
        categories = self.get_categories()
        print("Available categories:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        
        try:
            choice = int(input("\nEnter category number: ")) - 1
            if 0 <= choice < len(categories):
                category = categories[choice]
                results = self.search_by_category(category)
                self.display_events(results, f"EVENTS IN CATEGORY '{category}'")
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")
        
        input("Press Enter to continue...")
    
    def search_by_priority_menu(self):
        """Menu for searching by priority."""
        print("\n⚡ SEARCH BY PRIORITY")
        print("=" * 30)
        
        priorities = self.get_priorities()
        print("Available priorities:")
        for i, priority in enumerate(priorities, 1):
            print(f"{i}. {priority}")
        
        try:
            choice = int(input("\nEnter priority number: ")) - 1
            if 0 <= choice < len(priorities):
                priority = priorities[choice]
                results = self.search_by_priority(priority)
                self.display_events(results, f"EVENTS WITH PRIORITY '{priority}'")
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")
        
        input("Press Enter to continue...")
    
    def search_by_location_menu(self):
        """Menu for searching by location."""
        print("\n📍 SEARCH BY LOCATION")
        print("=" * 30)
        
        location = input("Enter location keyword: ").strip()
        if not location:
            print("❌ Please enter a location keyword.")
            input("Press Enter to continue...")
            return
        
        results = self.search_by_location(location)
        self.display_events(results, f"EVENTS AT LOCATION CONTAINING '{location}'")
        input("Press Enter to continue...")
    
    def upcoming_events_menu(self):
        """Menu for viewing upcoming events."""
        print("\n📅 UPCOMING EVENTS")
        print("=" * 30)
        
        try:
            days = int(input("Enter number of days to look ahead (default 7): ") or "7")
            if days <= 0:
                days = 7
        except ValueError:
            days = 7
        
        results = self.get_upcoming_events(days)
        self.display_events(results, f"UPCOMING EVENTS (NEXT {days} DAYS)")
        input("Press Enter to continue...")
    
    def delete_event_menu(self):
        """Menu for deleting an event."""
        events = self.get_all_events()
        if not events:
            print("❌ No events to delete.")
            input("Press Enter to continue...")
            return
        
        print("\n🗑️  DELETE EVENT")
        print("=" * 30)
        self.display_events(events, "ALL EVENTS")
        
        try:
            choice = int(input("\nEnter event number to delete: ")) - 1
            if 0 <= choice < len(events):
                event = events[choice]
                confirm = input(f"Are you sure you want to delete '{event.title}'? (y/N): ").strip().lower()
                if confirm == 'y':
                    if self.delete_event(event.event_id):
                        print("✅ Event deleted successfully!")
                    else:
                        print("❌ Failed to delete event.")
                else:
                    print("❌ Deletion cancelled.")
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")
        
        input("Press Enter to continue...")
