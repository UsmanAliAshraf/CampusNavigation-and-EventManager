# 🏫 Campus Connect Navigation & Event Planner System

A comprehensive CLI-based application for UET students to navigate campus, manage events, schedule tasks, and search events efficiently using various data structures and algorithms.

## 🎯 Project Overview

This project demonstrates real-world application of Data Structures and Algorithms concepts through a practical campus management system. It showcases:

- **Graph Algorithms**: BFS, DFS, and Dijkstra's shortest path for campus navigation
- **Linked Lists**: Doubly linked list for event management with undo/redo
- **Stacks**: Command pattern for undo/redo functionality
- **Queues**: FIFO task scheduling system
- **Binary Search Trees**: Efficient event searching and categorization

## 📁 Project Structure

```
campus_connect/
├── main.py                    # Main application entry point
├── CLI.py                     # CLI menu interface
├── navigator.py               # Campus navigation module
├── events_manager.py          # Event management module
├── task_scheduler.py          # Task scheduling module
├── event_search_tree.py       # Event search tree module
├── data_structures/
│   ├── __init__.py
│   ├── graph.py              # Graph implementation
│   ├── linked_list.py        # Doubly linked list
│   ├── stack.py              # Stack for undo/redo
│   ├── queue.py              # Queue for tasks
│   └── binary_tree.py        # Binary search tree
├── data/                     # Data files (future)
└── tests/                    # Test files (future)
```

## 🚀 Features

### 1. 🗺️ Campus Navigator
- **Graph-based campus modeling** with buildings as nodes and walkways as edges
- **BFS**: Find all reachable buildings from current location
- **DFS**: Explore campus connectivity
- **Dijkstra's Algorithm**: Find shortest path between buildings
- Interactive campus map with distance calculations

### 2. 📅 Event Manager
- **Doubly linked list** for efficient event storage
- **Stack-based undo/redo** system for all operations
- Add, edit, delete events with full validation
- Search events by keyword
- Event categorization and priority management

### 3. ✅ Task Scheduler
- **Queue-based FIFO** task management
- Task priority levels (Low, Medium, High)
- Task completion tracking and statistics
- View pending and completed tasks
- Task deadline management

### 4. 🔍 Event Search Tree
- **Binary search tree** for efficient event searching
- Search by title, date, category, priority, or location
- Event categorization and filtering
- Upcoming events detection
- Tree balance and height information

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Running the Application

1. **Clone or download the project**
2. **Navigate to the project directory**
3. **Run the main application:**
   ```bash
   python main.py
   ```

### Using the Application

1. **Main Menu**: Choose from 4 modules or view about information
2. **Campus Navigator**: Set location and navigate to buildings
3. **Event Manager**: Manage events with undo/redo functionality
4. **Task Scheduler**: Schedule and complete tasks using FIFO
5. **Event Search Tree**: Search and categorize events efficiently

## 📊 Data Structures & Algorithms Used

### Graph Algorithms
- **Breadth-First Search (BFS)**: O(V + E) time complexity
- **Depth-First Search (DFS)**: O(V + E) time complexity  
- **Dijkstra's Algorithm**: O((V + E) log V) time complexity
- **Adjacency List Representation**: O(V + E) space complexity

### Linked Lists
- **Doubly Linked List**: O(1) insertion/deletion at ends
- **Position-based operations**: O(n) for random access
- **Bidirectional traversal**: Efficient for undo/redo

### Stacks
- **LIFO operations**: O(1) push/pop
- **Command pattern**: Store operation history
- **Undo/Redo system**: Limited history with max size

### Queues
- **FIFO operations**: O(1) enqueue/dequeue
- **Task scheduling**: First-in-first-out processing
- **Priority handling**: Maintains task order

### Binary Search Trees
- **Search operations**: O(log n) average case
- **Insertion/Deletion**: O(log n) average case
- **Inorder traversal**: O(n) for sorted output
- **Balanced tree**: Efficient for large datasets

## 🎓 Learning Outcomes

This project demonstrates:

1. **Real-world DSA applications** in campus management
2. **Algorithm implementation** (BFS, DFS, Dijkstra's)
3. **Data structure integration** across multiple modules
4. **Time/space complexity** considerations
5. **Modular software design** principles
6. **User interface design** for CLI applications
7. **Error handling** and input validation
8. **Documentation** and code organization

## 🔧 Technical Details

### Time Complexities
- **Graph operations**: O(V + E) for BFS/DFS, O((V + E) log V) for Dijkstra's
- **Linked list operations**: O(1) for ends, O(n) for random access
- **Stack/Queue operations**: O(1) for all operations
- **BST operations**: O(log n) average, O(n) worst case

### Space Complexities
- **Graph**: O(V + E) for adjacency list
- **Linked list**: O(n) for n elements
- **Stack/Queue**: O(n) for n elements
- **BST**: O(n) for n nodes

## 🚀 Future Enhancements

### GUI Implementation
- **Tkinter/PyQt** interface for better user experience
- **Visual campus map** with interactive navigation
- **Calendar view** for events and tasks
- **Drag-and-drop** functionality

### Advanced Features
- **Data persistence** with JSON/database storage
- **User authentication** and profiles
- **Real-time notifications** for upcoming events
- **Mobile app** version
- **API integration** for external services

### Performance Optimizations
- **AVL/RB trees** for better BST balance
- **Graph caching** for faster navigation
- **Lazy loading** for large datasets
- **Memory optimization** for large event lists

## 📝 Contributing

This is a learning project demonstrating DSA concepts. Feel free to:
- Add new features
- Improve existing algorithms
- Enhance the user interface
- Add more test cases
- Optimize performance

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

## 👨‍💻 Author

Created as a Data Structures & Algorithms project for UET students.

---

**Happy Coding! 🎉**
