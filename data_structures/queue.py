from typing import Any, List, Optional
from collections import deque

class Queue:
    """
    Queue implementation for task scheduling.
    Uses FIFO (First In, First Out) principle.
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize an empty queue.
        
        Args:
            max_size: Maximum size of the queue (None for unlimited)
        """
        self.items = deque()
        self.max_size = max_size
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def is_full(self) -> bool:
        """Check if the queue is full (only if max_size is set)."""
        if self.max_size is None:
            return False
        return len(self.items) >= self.max_size
    
    def size(self) -> int:
        """Get the current size of the queue."""
        return len(self.items)
    
    def enqueue(self, item: Any) -> bool:
        """
        Add an item to the end of the queue.
        
        Args:
            item: Item to add to the queue
            
        Returns:
            True if enqueue successful, False if queue is full
        """
        if self.is_full():
            return False
        
        self.items.append(item)
        return True
    
    def dequeue(self) -> Optional[Any]:
        """
        Remove and return the first item from the queue.
        
        Returns:
            First item from the queue, or None if queue is empty
        """
        if self.is_empty():
            return None
        
        return self.items.popleft()
    
    def peek(self) -> Optional[Any]:
        """
        Return the first item from the queue without removing it.
        
        Returns:
            First item from the queue, or None if queue is empty
        """
        if self.is_empty():
            return None
        
        return self.items[0]
    
    def peek_back(self) -> Optional[Any]:
        """
        Return the last item from the queue without removing it.
        
        Returns:
            Last item from the queue, or None if queue is empty
        """
        if self.is_empty():
            return None
        
        return self.items[-1]
    
    def clear(self) -> None:
        """Remove all items from the queue."""
        self.items.clear()
    
    def to_list(self) -> List[Any]:
        """Convert the queue to a Python list (front to back)."""
        return list(self.items)
    
    def display(self) -> None:
        """Display the queue contents (for debugging)."""
        if self.is_empty():
            print("Empty queue")
            return
        
        print("Queue (front to back):")
        for i, item in enumerate(self.items):
            print(f"  {i}: {item}")
    
    def get_max_size(self) -> Optional[int]:
        """Get the maximum size of the queue."""
        return self.max_size
    
    def set_max_size(self, max_size: Optional[int]) -> None:
        """
        Set the maximum size of the queue.
        
        Args:
            max_size: New maximum size (None for unlimited)
        """
        self.max_size = max_size
        
        # If new max_size is smaller than current size, remove excess items from front
        if max_size is not None and len(self.items) > max_size:
            while len(self.items) > max_size:
                self.items.popleft()
    
    def contains(self, item: Any) -> bool:
        """
        Check if the queue contains a specific item.
        
        Args:
            item: Item to search for
            
        Returns:
            True if item found, False otherwise
        """
        return item in self.items
    
    def remove(self, item: Any) -> bool:
        """
        Remove the first occurrence of an item from the queue.
        
        Args:
            item: Item to remove
            
        Returns:
            True if item was removed, False if not found
        """
        try:
            self.items.remove(item)
            return True
        except ValueError:
            return False
