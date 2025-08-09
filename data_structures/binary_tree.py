from typing import Any, List, Optional, Tuple

class TreeNode:
    """Node class for binary search tree."""
    
    def __init__(self, key: Any, value: Any = None):
        self.key = key
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class BinarySearchTree:
    """
    Binary Search Tree implementation for efficient event searching.
    Supports insertion, deletion, searching, and traversal operations.
    """
    
    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root: Optional[TreeNode] = None
        self.size = 0
    
    def is_empty(self) -> bool:
        """Check if the tree is empty."""
        return self.root is None
    
    def get_size(self) -> int:
        """Get the number of nodes in the tree."""
        return self.size
    
    def insert(self, key: Any, value: Any = None) -> bool:
        """
        Insert a new key-value pair into the tree.
        
        Args:
            key: Key to insert
            value: Value associated with the key
            
        Returns:
            True if insertion successful, False if key already exists
        """
        if self.root is None:
            self.root = TreeNode(key, value)
            self.size += 1
            return True
        
        return self._insert_recursive(self.root, key, value)
    
    def _insert_recursive(self, node: TreeNode, key: Any, value: Any) -> bool:
        """Recursive helper for insertion."""
        if key == node.key:
            # Key already exists, update value
            node.value = value
            return False
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key, value)
                self.size += 1
                return True
            else:
                return self._insert_recursive(node.left, key, value)
        else:
            if node.right is None:
                node.right = TreeNode(key, value)
                self.size += 1
                return True
            else:
                return self._insert_recursive(node.right, key, value)
    
    def search(self, key: Any) -> Optional[Any]:
        """
        Search for a key in the tree.
        
        Args:
            key: Key to search for
            
        Returns:
            Value associated with the key, or None if not found
        """
        if self.root is None:
            return None
        
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node: TreeNode, key: Any) -> Optional[Any]:
        """Recursive helper for search."""
        if node is None:
            return None
        elif key == node.key:
            return node.value
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def delete(self, key: Any) -> bool:
        """
        Delete a key-value pair from the tree.
        
        Args:
            key: Key to delete
            
        Returns:
            True if deletion successful, False if key not found
        """
        if self.root is None:
            return False
        
        self.root, deleted = self._delete_recursive(self.root, key)
        if deleted:
            self.size -= 1
        return deleted
    
    def _delete_recursive(self, node: Optional[TreeNode], key: Any) -> Tuple[Optional[TreeNode], bool]:
        """Recursive helper for deletion."""
        if node is None:
            return None, False
        
        if key < node.key:
            node.left, deleted = self._delete_recursive(node.left, key)
            return node, deleted
        elif key > node.key:
            node.right, deleted = self._delete_recursive(node.right, key)
            return node, deleted
        else:
            # Node to delete found
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                # Node has two children
                successor = self._find_min(node.right)
                node.key = successor.key
                node.value = successor.value
                node.right, _ = self._delete_recursive(node.right, successor.key)
                return node, True
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        """Find the minimum key in a subtree."""
        while node.left is not None:
            node = node.left
        return node
    
    def find_min(self) -> Optional[Any]:
        """Find the minimum key in the tree."""
        if self.root is None:
            return None
        
        min_node = self._find_min(self.root)
        return min_node.key
    
    def find_max(self) -> Optional[Any]:
        """Find the maximum key in the tree."""
        if self.root is None:
            return None
        
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key
    
    def inorder_traversal(self) -> List[Tuple[Any, Any]]:
        """Perform inorder traversal (left, root, right)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[TreeNode], result: List[Tuple[Any, Any]]) -> None:
        """Recursive helper for inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append((node.key, node.value))
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self) -> List[Tuple[Any, Any]]:
        """Perform preorder traversal (root, left, right)."""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: Optional[TreeNode], result: List[Tuple[Any, Any]]) -> None:
        """Recursive helper for preorder traversal."""
        if node is not None:
            result.append((node.key, node.value))
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self) -> List[Tuple[Any, Any]]:
        """Perform postorder traversal (left, right, root)."""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node: Optional[TreeNode], result: List[Tuple[Any, Any]]) -> None:
        """Recursive helper for postorder traversal."""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append((node.key, node.value))
    
    def level_order_traversal(self) -> List[Tuple[Any, Any]]:
        """Perform level-order traversal (breadth-first)."""
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append((node.key, node.value))
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def get_height(self) -> int:
        """Get the height of the tree."""
        return self._get_height_recursive(self.root)
    
    def _get_height_recursive(self, node: Optional[TreeNode]) -> int:
        """Recursive helper for getting height."""
        if node is None:
            return -1
        
        left_height = self._get_height_recursive(node.left)
        right_height = self._get_height_recursive(node.right)
        
        return max(left_height, right_height) + 1
    
    def is_balanced(self) -> bool:
        """Check if the tree is balanced."""
        return self._is_balanced_recursive(self.root) != -1
    
    def _is_balanced_recursive(self, node: Optional[TreeNode]) -> int:
        """Recursive helper for checking balance."""
        if node is None:
            return 0
        
        left_height = self._is_balanced_recursive(node.left)
        if left_height == -1:
            return -1
        
        right_height = self._is_balanced_recursive(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    
    def clear(self) -> None:
        """Clear all nodes from the tree."""
        self.root = None
        self.size = 0
    
    def display(self) -> None:
        """Display the tree structure (for debugging)."""
        if self.is_empty():
            print("Empty tree")
            return
        
        print("Binary Search Tree (inorder):")
        inorder_result = self.inorder_traversal()
        for key, value in inorder_result:
            print(f"  {key}: {value}")
    
    def get_all_keys(self) -> List[Any]:
        """Get all keys in the tree (inorder)."""
        return [key for key, _ in self.inorder_traversal()]
    
    def get_all_values(self) -> List[Any]:
        """Get all values in the tree (inorder)."""
        return [value for _, value in self.inorder_traversal()]
