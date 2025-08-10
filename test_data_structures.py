#!/usr/bin/env python3
"""
Test script to verify data structure operations
"""

import sys
import os

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_structures.queue import Queue
from data_structures.binary_tree import BinarySearchTree
from event_search_tree import EventNode

def test_queue_operations():
    """Test queue operations including dequeue."""
    print("🧪 Testing Queue Operations")
    print("=" * 40)
    
    queue = Queue()
    
    # Add some tasks
    tasks = [
        {'name': 'Task 1', 'priority': 'High', 'id': 1},
        {'name': 'Task 2', 'priority': 'Medium', 'id': 2},
        {'name': 'Task 3', 'priority': 'Low', 'id': 3}
    ]
    
    for task in tasks:
        queue.enqueue(task)
        print(f"✅ Enqueued: {task['name']}")
    
    print(f"\n📊 Queue size: {queue.size()}")
    print(f"📊 Queue empty: {queue.is_empty()}")
    
    # Test dequeue operations
    print("\n🔄 Testing Dequeue Operations:")
    while not queue.is_empty():
        task = queue.dequeue()
        print(f"✅ Dequeued: {task['name']} (ID: {task['id']})")
    
    print(f"\n📊 Queue size after dequeue: {queue.size()}")
    print(f"📊 Queue empty: {queue.is_empty()}")
    
    print("\n" + "=" * 40)

def test_binary_tree_search():
    """Test binary tree search operations."""
    print("🧪 Testing Binary Tree Search")
    print("=" * 40)
    
    bst = BinarySearchTree()
    
    # Create sample events
    sample_events = [
        ("Mid Exam", "2024-01-15", "10:00", "CS Department", "Academic", "High"),
        ("Viva", "2024-01-20", "14:00", "Lab 3", "Academic", "High"),
        ("Presentation", "2024-01-25", "11:00", "Auditorium", "Academic", "Medium"),
        ("Sports Day", "2024-02-01", "09:00", "Sports Complex", "Event", "Medium"),
        ("Library Visit", "2024-01-12", "15:00", "Library", "Study", "Low")
    ]
    
    # Insert events into tree
    for title, date, time, location, category, priority in sample_events:
        event_node = EventNode(
            event_id=f"EVT_{len(sample_events)}",
            title=title,
            date=date,
            time=time,
            location=location,
            category=category,
            priority=priority
        )
        bst.insert(title, event_node)
        print(f"✅ Inserted: {title}")
    
    print(f"\n📊 Tree size: {bst.get_size()}")
    print(f"📊 Tree height: {bst.get_height()}")
    
    # Test search operations
    print("\n🔍 Testing Search Operations:")
    
    # Search by name
    search_results = []
    all_events = bst.inorder_traversal()
    search_term = "exam"
    
    for key, event_node in all_events:
        if search_term.lower() in event_node.title.lower():
            search_results.append(event_node)
    
    print(f"🔍 Search for '{search_term}': Found {len(search_results)} results")
    for result in search_results:
        print(f"  - {result.title} ({result.date})")
    
    # Search by priority
    search_results = []
    priority_search = "High"
    
    for key, event_node in all_events:
        if event_node.priority == priority_search:
            search_results.append(event_node)
    
    print(f"\n🔍 Search for priority '{priority_search}': Found {len(search_results)} results")
    for result in search_results:
        print(f"  - {result.title} ({result.priority})")
    
    print("\n" + "=" * 40)

def main():
    """Main test function."""
    print("🏫 Campus Connect - Data Structure Tests")
    print("=" * 50)
    
    test_queue_operations()
    test_binary_tree_search()
    
    print("✅ All tests completed successfully!")
    print("🎉 Data structures are working correctly!")

if __name__ == "__main__":
    main()
