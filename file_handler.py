"""
File Handler Module
Handles saving and loading events and tasks data to/from JSON files.
"""

import json
import os
from typing import List, Dict, Any
from datetime import datetime

class FileHandler:
    """Handles file operations for events and tasks data."""
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the file handler.
        
        Args:
            data_dir: Directory containing data files
        """
        self.data_dir = data_dir
        self.events_file = os.path.join(data_dir, "events.json")
        self.tasks_file = os.path.join(data_dir, "tasks.json")
        
        # Ensure data directory exists
        os.makedirs(data_dir, exist_ok=True)
    
    def save_events(self, events_list: List[Dict[str, Any]]) -> bool:
        """
        Save events list to JSON file.
        
        Args:
            events_list: List of event dictionaries
            
        Returns:
            True if save successful, False otherwise
        """
        try:
            data = {
                "events": events_list,
                "last_updated": datetime.now().isoformat()
            }
            
            with open(self.events_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"❌ Error saving events: {e}")
            return False
    
    def load_events(self) -> List[Dict[str, Any]]:
        """
        Load events list from JSON file.
        
        Returns:
            List of event dictionaries, empty list if file doesn't exist or error
        """
        try:
            if not os.path.exists(self.events_file):
                return []
            
            with open(self.events_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data.get("events", [])
        except Exception as e:
            print(f"❌ Error loading events: {e}")
            return []
    
    def save_tasks(self, tasks_list: List[Dict[str, Any]]) -> bool:
        """
        Save tasks list to JSON file.
        
        Args:
            tasks_list: List of task dictionaries
            
        Returns:
            True if save successful, False otherwise
        """
        try:
            data = {
                "tasks": tasks_list,
                "last_updated": datetime.now().isoformat()
            }
            
            with open(self.tasks_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"❌ Error saving tasks: {e}")
            return False
    
    def load_tasks(self) -> List[Dict[str, Any]]:
        """
        Load tasks list from JSON file.
        
        Returns:
            List of task dictionaries, empty list if file doesn't exist or error
        """
        try:
            if not os.path.exists(self.tasks_file):
                return []
            
            with open(self.tasks_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data.get("tasks", [])
        except Exception as e:
            print(f"❌ Error loading tasks: {e}")
            return []
    
    def save_event_tree_data(self, event_tree_data: List[Dict[str, Any]]) -> bool:
        """
        Save event tree data to JSON file.
        
        Args:
            event_tree_data: List of event node dictionaries
            
        Returns:
            True if save successful, False otherwise
        """
        try:
            data = {
                "event_tree_data": event_tree_data,
                "last_updated": datetime.now().isoformat()
            }
            
            tree_file = os.path.join(self.data_dir, "event_tree.json")
            with open(tree_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"❌ Error saving event tree data: {e}")
            return False
    
    def load_event_tree_data(self) -> List[Dict[str, Any]]:
        """
        Load event tree data from JSON file.
        
        Returns:
            List of event node dictionaries, empty list if file doesn't exist or error
        """
        try:
            tree_file = os.path.join(self.data_dir, "event_tree.json")
            if not os.path.exists(tree_file):
                return []
            
            with open(tree_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data.get("event_tree_data", [])
        except Exception as e:
            print(f"❌ Error loading event tree data: {e}")
            return []
    
    def clear_all_data(self) -> bool:
        """
        Clear all data files.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            files_to_clear = [self.events_file, self.tasks_file]
            tree_file = os.path.join(self.data_dir, "event_tree.json")
            files_to_clear.append(tree_file)
            
            for file_path in files_to_clear:
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            return True
        except Exception as e:
            print(f"❌ Error clearing data: {e}")
            return False
    
    def get_data_info(self) -> Dict[str, Any]:
        """
        Get information about data files.
        
        Returns:
            Dictionary with file information
        """
        info = {
            "events_file": {
                "exists": os.path.exists(self.events_file),
                "size": os.path.getsize(self.events_file) if os.path.exists(self.events_file) else 0
            },
            "tasks_file": {
                "exists": os.path.exists(self.tasks_file),
                "size": os.path.getsize(self.tasks_file) if os.path.exists(self.tasks_file) else 0
            },
            "event_tree_file": {
                "exists": os.path.exists(os.path.join(self.data_dir, "event_tree.json")),
                "size": os.path.getsize(os.path.join(self.data_dir, "event_tree.json")) if os.path.exists(os.path.join(self.data_dir, "event_tree.json")) else 0
            }
        }
        
        return info
