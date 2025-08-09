from typing import Any, List, Optional

class Stack:
    """
    Stack implementation for undo/redo functionality.
    Uses LIFO (Last In, First Out) principle.
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize an empty stack.
        
        Args:
            max_size: Maximum size of the stack (None for unlimited)
        """
        self.items: List[Any] = []
        self.max_size = max_size
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def is_full(self) -> bool:
        """Check if the stack is full (only if max_size is set)."""
        if self.max_size is None:
            return False
        return len(self.items) >= self.max_size
    
    def size(self) -> int:
        """Get the current size of the stack."""
        return len(self.items)
    
    def push(self, item: Any) -> bool:
        """
        Push an item onto the top of the stack.
        
        Args:
            item: Item to push onto the stack
            
        Returns:
            True if push successful, False if stack is full
        """
        if self.is_full():
            return False
        
        self.items.append(item)
        return True
    
    def pop(self) -> Optional[Any]:
        """
        Remove and return the top item from the stack.
        
        Returns:
            Top item from the stack, or None if stack is empty
        """
        if self.is_empty():
            return None
        
        return self.items.pop()
    
    def peek(self) -> Optional[Any]:
        """
        Return the top item from the stack without removing it.
        
        Returns:
            Top item from the stack, or None if stack is empty
        """
        if self.is_empty():
            return None
        
        return self.items[-1]
    
    def clear(self) -> None:
        """Remove all items from the stack."""
        self.items.clear()
    
    def to_list(self) -> List[Any]:
        """Convert the stack to a Python list (top to bottom)."""
        return self.items.copy()
    
    def display(self) -> None:
        """Display the stack contents (for debugging)."""
        if self.is_empty():
            print("Empty stack")
            return
        
        print("Stack (top to bottom):")
        for i in range(len(self.items) - 1, -1, -1):
            print(f"  {self.items[i]}")
    
    def get_max_size(self) -> Optional[int]:
        """Get the maximum size of the stack."""
        return self.max_size
    
    def set_max_size(self, max_size: Optional[int]) -> None:
        """
        Set the maximum size of the stack.
        
        Args:
            max_size: New maximum size (None for unlimited)
        """
        self.max_size = max_size
        
        # If new max_size is smaller than current size, remove excess items
        if max_size is not None and len(self.items) > max_size:
            self.items = self.items[-max_size:]
