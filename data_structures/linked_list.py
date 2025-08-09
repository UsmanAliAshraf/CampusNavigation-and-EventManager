from typing import Optional, Any, List

class Node:
    """Node class for doubly linked list."""
    
    def __init__(self, data: Any):
        self.data = data
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

class DoublyLinkedList:
    """
    Doubly linked list implementation for event management.
    Supports efficient insertion, deletion, and traversal.
    """
    
    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None
    
    def get_size(self) -> int:
        """Get the size of the list."""
        return self.size
    
    def insert_at_beginning(self, data: Any) -> None:
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def insert_at_end(self, data: Any) -> None:
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def insert_at_position(self, data: Any, position: int) -> bool:
        """
        Insert a new node at a specific position.
        
        Args:
            data: Data to insert
            position: Position to insert at (0-indexed)
            
        Returns:
            True if insertion successful, False otherwise
        """
        if position < 0 or position > self.size:
            return False
        
        if position == 0:
            self.insert_at_beginning(data)
            return True
        elif position == self.size:
            self.insert_at_end(data)
            return True
        
        new_node = Node(data)
        current = self.head
        
        # Move to the position
        for _ in range(position):
            current = current.next
        
        # Insert the new node
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        
        self.size += 1
        return True
    
    def delete_from_beginning(self) -> Optional[Any]:
        """Delete and return the first node's data."""
        if self.is_empty():
            return None
        
        data = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        return data
    
    def delete_from_end(self) -> Optional[Any]:
        """Delete and return the last node's data."""
        if self.is_empty():
            return None
        
        data = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        return data
    
    def delete_at_position(self, position: int) -> Optional[Any]:
        """
        Delete node at a specific position.
        
        Args:
            position: Position to delete from (0-indexed)
            
        Returns:
            Data of deleted node, or None if position invalid
        """
        if position < 0 or position >= self.size:
            return None
        
        if position == 0:
            return self.delete_from_beginning()
        elif position == self.size - 1:
            return self.delete_from_end()
        
        current = self.head
        
        # Move to the position
        for _ in range(position):
            current = current.next
        
        # Delete the node
        data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        
        self.size -= 1
        return data
    
    def delete_by_value(self, value: Any) -> bool:
        """
        Delete the first occurrence of a node with the given value.
        
        Args:
            value: Value to delete
            
        Returns:
            True if deletion successful, False otherwise
        """
        current = self.head
        
        while current:
            if current.data == value:
                if current == self.head:
                    self.delete_from_beginning()
                elif current == self.tail:
                    self.delete_from_end()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, value: Any) -> Optional[int]:
        """
        Search for a value in the list.
        
        Args:
            value: Value to search for
            
        Returns:
            Position of first occurrence, or None if not found
        """
        current = self.head
        position = 0
        
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return None
    
    def get_at_position(self, position: int) -> Optional[Any]:
        """
        Get data at a specific position.
        
        Args:
            position: Position to get data from (0-indexed)
            
        Returns:
            Data at position, or None if position invalid
        """
        if position < 0 or position >= self.size:
            return None
        
        current = self.head
        
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def update_at_position(self, position: int, new_data: Any) -> bool:
        """
        Update data at a specific position.
        
        Args:
            position: Position to update (0-indexed)
            new_data: New data to set
            
        Returns:
            True if update successful, False otherwise
        """
        if position < 0 or position >= self.size:
            return False
        
        current = self.head
        
        for _ in range(position):
            current = current.next
        
        current.data = new_data
        return True
    
    def to_list(self) -> List[Any]:
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
    
    def clear(self) -> None:
        """Clear all nodes from the list."""
        self.head = None
        self.tail = None
        self.size = 0
    
    def display(self) -> None:
        """Display the linked list (for debugging)."""
        if self.is_empty():
            print("Empty list")
            return
        
        current = self.head
        while current:
            print(f"{current.data} <-> ", end="")
            current = current.next
        print("None")
    
    def display_reverse(self) -> None:
        """Display the linked list in reverse order (for debugging)."""
        if self.is_empty():
            print("Empty list")
            return
        
        current = self.tail
        while current:
            print(f"{current.data} <-> ", end="")
            current = current.prev
        print("None")
