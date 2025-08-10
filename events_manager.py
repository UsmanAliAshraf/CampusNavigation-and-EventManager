"""
Events Manager Module
Provides event management using doubly linked lists and undo/redo with stacks.
"""

from data_structures.linked_list import DoublyLinkedList
from data_structures.stack import Stack
from typing import Dict, List, Optional
from datetime import datetime
import json
import os

class Event:
    """Event class to store event information."""
    
    def __init__(self, title: str, date: str, time: str, location: str, description: str = ""):
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.description = description
        self.created_at = datetime.now()
    
    def __str__(self):
        return f"{self.title} - {self.date} at {self.time} ({self.location})"
    
    def to_dict(self) -> Dict:
        """Convert event to dictionary for storage."""
        return {
            'title': self.title,
            'date': self.date,
            'time': self.time,
            'location': self.location,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }

class EventsManager:
    """
    Event management system using doubly linked list and stack-based undo/redo.
    """
    
    def __init__(self):
        """Initialize the events manager."""
        self.events_list = DoublyLinkedList()
        self.undo_stack = Stack(max_size=50)  # Limit undo history
        self.redo_stack = Stack(max_size=50)  # Limit redo history
        
        # Command types for undo/redo
        self.ADD_EVENT = "ADD"
        self.DELETE_EVENT = "DELETE"
        self.EDIT_EVENT = "EDIT"
        
        # File handling
        self.events_file = os.path.join("data", "events.json")
        self.load_events_from_file()
    
    def add_event(self, event: Event) -> bool:
        """
        Add a new event to the list.
        
        Args:
            event: Event object to add
            
        Returns:
            True if event added successfully
        """
        # Store command for undo
        command = {
            'type': self.DELETE_EVENT,
            'position': self.events_list.get_size(),
            'event': event
        }
        self.undo_stack.push(command)
        self.redo_stack.clear()  # Clear redo stack when new action is performed
        
        # Add event to list
        self.events_list.insert_at_end(event)
        return True
    
    def delete_event(self, position: int) -> Optional[Event]:
        """
        Delete an event at a specific position.
        
        Args:
            position: Position of event to delete (0-indexed)
            
        Returns:
            Deleted event, or None if position invalid
        """
        if position < 0 or position >= self.events_list.get_size():
            return None
        
        # Get event before deletion for undo
        event = self.events_list.get_at_position(position)
        if event is None:
            return None
        
        # Store command for undo
        command = {
            'type': self.ADD_EVENT,
            'position': position,
            'event': event
        }
        self.undo_stack.push(command)
        self.redo_stack.clear()
        
        # Delete event
        return self.events_list.delete_at_position(position)
    
    def edit_event(self, position: int, new_event: Event) -> bool:
        """
        Edit an event at a specific position.
        
        Args:
            position: Position of event to edit (0-indexed)
            new_event: New event data
            
        Returns:
            True if edit successful, False otherwise
        """
        if position < 0 or position >= self.events_list.get_size():
            return False
        
        # Get old event for undo
        old_event = self.events_list.get_at_position(position)
        if old_event is None:
            return False
        
        # Store command for undo
        command = {
            'type': self.EDIT_EVENT,
            'position': position,
            'old_event': old_event,
            'new_event': new_event
        }
        self.undo_stack.push(command)
        self.redo_stack.clear()
        
        # Update event
        return self.events_list.update_at_position(position, new_event)
    
    def undo(self) -> bool:
        """
        Undo the last action.
        
        Returns:
            True if undo successful, False if no actions to undo
        """
        if self.undo_stack.is_empty():
            return False
        
        command = self.undo_stack.pop()
        
        if command['type'] == self.ADD_EVENT:
            # Undo add: delete the event
            deleted_event = self.events_list.delete_at_position(command['position'])
            if deleted_event:
                # Store for redo
                redo_command = {
                    'type': self.ADD_EVENT,
                    'position': command['position'],
                    'event': deleted_event
                }
                self.redo_stack.push(redo_command)
                return True
        
        elif command['type'] == self.DELETE_EVENT:
            # Undo delete: add the event back
            self.events_list.insert_at_position(command['event'], command['position'])
            # Store for redo
            redo_command = {
                'type': self.DELETE_EVENT,
                'position': command['position'],
                'event': command['event']
            }
            self.redo_stack.push(redo_command)
            return True
        
        elif command['type'] == self.EDIT_EVENT:
            # Undo edit: restore old event
            self.events_list.update_at_position(command['position'], command['old_event'])
            # Store for redo
            redo_command = {
                'type': self.EDIT_EVENT,
                'position': command['position'],
                'old_event': command['new_event'],
                'new_event': command['old_event']
            }
            self.redo_stack.push(redo_command)
            return True
        
        return False
    
    def redo(self) -> bool:
        """
        Redo the last undone action.
        
        Returns:
            True if redo successful, False if no actions to redo
        """
        if self.redo_stack.is_empty():
            return False
        
        command = self.redo_stack.pop()
        
        if command['type'] == self.ADD_EVENT:
            # Redo add: add the event back
            self.events_list.insert_at_position(command['event'], command['position'])
            # Store for undo
            undo_command = {
                'type': self.DELETE_EVENT,
                'position': command['position'],
                'event': command['event']
            }
            self.undo_stack.push(undo_command)
            return True
        
        elif command['type'] == self.DELETE_EVENT:
            # Redo delete: delete the event
            deleted_event = self.events_list.delete_at_position(command['position'])
            if deleted_event:
                # Store for undo
                undo_command = {
                    'type': self.ADD_EVENT,
                    'position': command['position'],
                    'event': deleted_event
                }
                self.undo_stack.push(undo_command)
                return True
        
        elif command['type'] == self.EDIT_EVENT:
            # Redo edit: apply new event
            self.events_list.update_at_position(command['position'], command['new_event'])
            # Store for undo
            undo_command = {
                'type': self.EDIT_EVENT,
                'position': command['position'],
                'old_event': command['new_event'],
                'new_event': command['old_event']
            }
            self.undo_stack.push(undo_command)
            return True
        
        return False
    
    def get_all_events(self) -> List[Event]:
        """Get all events as a list."""
        return self.events_list.to_list()
    
    def get_event_count(self) -> int:
        """Get the total number of events."""
        return self.events_list.get_size()
    
    def search_events(self, keyword: str) -> List[Event]:
        """
        Search events by keyword in title or description.
        
        Args:
            keyword: Keyword to search for
            
        Returns:
            List of matching events
        """
        results = []
        events = self.get_all_events()
        
        for event in events:
            if (keyword.lower() in event.title.lower() or 
                keyword.lower() in event.description.lower() or
                keyword.lower() in event.location.lower()):
                results.append(event)
        
        return results
    
    def display_events(self):
        """Display all events."""
        events = self.get_all_events()
        
        if not events:
            print("\n📅 No events found.")
            return
        
        print(f"\n📅 EVENTS ({len(events)} total)")
        print("=" * 60)
        
        for i, event in enumerate(events):
            print(f"{i+1}. {event.title}")
            print(f"   📅 Date: {event.date}")
            print(f"   ⏰ Time: {event.time}")
            print(f"   📍 Location: {event.location}")
            if event.description:
                print(f"   📝 Description: {event.description}")
            print("-" * 40)
    
    def run_events_menu(self):
        """Run the events manager menu."""
        while True:
            print("\n📅 EVENTS MANAGER")
            print("=" * 30)
            print("1. ➕ Add New Event")
            print("2. 📋 View All Events")
            print("3. 🔍 Search Events")
            print("4. ✏️  Edit Event")
            print("5. 🗑️  Delete Event")
            print("6. ↩️  Undo")
            print("7. ↪️  Redo")
            print("8. ↩️  Back to Main Menu")
            print("=" * 30)
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.add_event_menu()
            elif choice == "2":
                self.display_events()
                input("Press Enter to continue...")
            elif choice == "3":
                self.search_events_menu()
            elif choice == "4":
                self.edit_event_menu()
            elif choice == "5":
                self.delete_event_menu()
            elif choice == "6":
                self.undo_action()
            elif choice == "7":
                self.redo_action()
            elif choice == "8":
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
        description = input("Description (optional): ").strip()
        
        if not date or not time or not location:
            print("❌ Date, time, and location are required.")
            input("Press Enter to continue...")
            return
        
        event = Event(title, date, time, location, description)
        
        if self.add_event(event):
            print("✅ Event added successfully!")
        else:
            print("❌ Failed to add event.")
        
        input("Press Enter to continue...")
    
    def search_events_menu(self):
        """Menu for searching events."""
        print("\n🔍 SEARCH EVENTS")
        print("=" * 30)
        
        keyword = input("Enter search keyword: ").strip()
        if not keyword:
            print("❌ Please enter a keyword.")
            input("Press Enter to continue...")
            return
        
        results = self.search_events(keyword)
        
        if not results:
            print(f"❌ No events found matching '{keyword}'.")
        else:
            print(f"\n🔍 SEARCH RESULTS ({len(results)} found)")
            print("=" * 50)
            for i, event in enumerate(results, 1):
                print(f"{i}. {event}")
        
        input("Press Enter to continue...")
    
    def edit_event_menu(self):
        """Menu for editing an event."""
        events = self.get_all_events()
        if not events:
            print("❌ No events to edit.")
            input("Press Enter to continue...")
            return
        
        print("\n✏️  EDIT EVENT")
        print("=" * 30)
        self.display_events()
        
        try:
            choice = int(input("\nEnter event number to edit: ")) - 1
            if 0 <= choice < len(events):
                self.edit_specific_event(choice)
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")
        
        input("Press Enter to continue...")
    
    def edit_specific_event(self, position: int):
        """Edit a specific event."""
        event = self.events_list.get_at_position(position)
        if not event:
            print("❌ Event not found.")
            return
        
        print(f"\n✏️  EDITING: {event.title}")
        print("=" * 40)
        print("Leave blank to keep current value.")
        
        title = input(f"Title [{event.title}]: ").strip() or event.title
        date = input(f"Date [{event.date}]: ").strip() or event.date
        time = input(f"Time [{event.time}]: ").strip() or event.time
        location = input(f"Location [{event.location}]: ").strip() or event.location
        description = input(f"Description [{event.description}]: ").strip() or event.description
        
        new_event = Event(title, date, time, location, description)
        
        if self.edit_event(position, new_event):
            print("✅ Event updated successfully!")
        else:
            print("❌ Failed to update event.")
    
    def delete_event_menu(self):
        """Menu for deleting an event."""
        events = self.get_all_events()
        if not events:
            print("❌ No events to delete.")
            input("Press Enter to continue...")
            return
        
        print("\n🗑️  DELETE EVENT")
        print("=" * 30)
        self.display_events()
        
        try:
            choice = int(input("\nEnter event number to delete: ")) - 1
            if 0 <= choice < len(events):
                event = events[choice]
                confirm = input(f"Are you sure you want to delete '{event.title}'? (y/N): ").strip().lower()
                if confirm == 'y':
                    deleted_event = self.delete_event(choice)
                    if deleted_event:
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
    
    def undo_action(self):
        """Undo the last action."""
        if self.undo():
            print("✅ Action undone successfully!")
        else:
            print("❌ No actions to undo.")
        input("Press Enter to continue...")
    
    def redo_action(self):
        """Redo the last undone action."""
        if self.redo():
            print("✅ Action redone successfully!")
        else:
            print("❌ No actions to redo.")
        input("Press Enter to continue...")
