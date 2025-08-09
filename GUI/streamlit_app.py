import streamlit as st
import sys
import os
import json
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time
import math

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from data_structures.graph import Graph
    from data_structures.linked_list import DoublyLinkedList
    from data_structures.stack import Stack
    from data_structures.queue import Queue
    from data_structures.binary_tree import BinarySearchTree
except ImportError as e:
    st.error(f"Error importing data structures: {e}")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Campus Connect - Navigation & Event Planner",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d1b3d 100%);
        color: #ffffff;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d1b3d 100%);
    }
    
    .css-1d391kg {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d1b3d 100%);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 165, 0, 0.1);
        border-radius: 8px 8px 0px 0px;
        color: #ffffff;
        padding: 10px 16px;
        border: 1px solid rgba(255, 165, 0, 0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background-color: rgba(255, 165, 0, 0.8);
        color: #1a1a1a;
        font-weight: 600;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #ff8c00 0%, #ff6b35 100%);
        color: #1a1a1a;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #ff6b35 0%, #ff8c00 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 140, 0, 0.3);
    }
    
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 165, 0, 0.3);
        border-radius: 8px;
        color: #ffffff;
    }
    
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 165, 0, 0.3);
        border-radius: 8px;
        color: #ffffff;
    }
    
    .stTextArea > div > div > textarea {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 165, 0, 0.3);
        border-radius: 8px;
        color: #ffffff;
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(255, 165, 0, 0.1) 0%, rgba(45, 27, 61, 0.3) 100%);
        border: 1px solid rgba(255, 165, 0, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
    }
    
    .path-card {
        background: linear-gradient(135deg, rgba(255, 165, 0, 0.05) 0%, rgba(45, 27, 61, 0.1) 100%);
        border: 1px solid rgba(255, 165, 0, 0.2);
        border-radius: 8px;
        padding: 15px;
        margin: 8px 0;
        transition: all 0.3s ease;
    }
    
    .path-card:hover {
        background: linear-gradient(135deg, rgba(255, 165, 0, 0.1) 0%, rgba(45, 27, 61, 0.2) 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(255, 140, 0, 0.2);
    }
    
    .header-gradient {
        background: linear-gradient(135deg, #ff8c00 0%, #ff6b35 50%, #8b008b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d1b3d 100%);
    }
    
    .stSidebar {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d1b3d 100%);
    }
    
    .stAlert {
        background-color: rgba(255, 165, 0, 0.1);
        border: 1px solid rgba(255, 165, 0, 0.3);
        border-radius: 8px;
    }
    
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #ff8c00 0%, #ff6b35 100%);
    }
    
    .event-card {
        background: linear-gradient(135deg, rgba(255, 165, 0, 0.05) 0%, rgba(45, 27, 61, 0.1) 100%);
        border: 1px solid rgba(255, 165, 0, 0.2);
        border-radius: 8px;
        padding: 15px;
        margin: 8px 0;
    }
    
    .task-card {
        background: linear-gradient(135deg, rgba(255, 165, 0, 0.05) 0%, rgba(45, 27, 61, 0.1) 100%);
        border: 1px solid rgba(255, 165, 0, 0.2);
        border-radius: 8px;
        padding: 15px;
        margin: 8px 0;
    }
    
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    if 'current_location' not in st.session_state:
        st.session_state.current_location = None
    if 'graph' not in st.session_state:
        st.session_state.graph = Graph()
    if 'events' not in st.session_state:
        st.session_state.events = DoublyLinkedList()
    if 'tasks' not in st.session_state:
        st.session_state.tasks = Queue()
    if 'event_tree' not in st.session_state:
        st.session_state.event_tree = BinarySearchTree()
    if 'undo_stack' not in st.session_state:
        st.session_state.undo_stack = Stack()
    if 'redo_stack' not in st.session_state:
        st.session_state.redo_stack = Stack()
    if 'events_list' not in st.session_state:
        st.session_state.events_list = []
    if 'tasks_list' not in st.session_state:
        st.session_state.tasks_list = []

# Load campus data
def load_campus_data():
    try:
        json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "campus_data.json")
        if os.path.exists(json_path):
            with open(json_path, 'r') as file:
                data = json.load(file)
                return data.get("buildings", {}), data.get("routes", [])
        else:
            st.error("Campus data file not found!")
            return {}, []
    except Exception as e:
        st.error(f"Error loading campus data: {e}")
        return {}, []

# Campus Navigator Module
def campus_navigator():
    st.markdown("""
    <div class="header-gradient">
        <h1>🗺️ Campus Navigator</h1>
    </div>
    """, unsafe_allow_html=True)
    
    buildings, routes = load_campus_data()
    
    if not buildings:
        st.error("No campus data available!")
        return
    
    # Initialize graph if not already done
    if len(st.session_state.graph.get_vertices()) == 0:
        st.info("🔧 Initializing campus graph...")
        for building in buildings.keys():
            st.session_state.graph.add_vertex(building)
        
        for route in routes:
            st.session_state.graph.add_edge(route["from"], route["to"], route["distance"])
        
        st.success(f"✅ Graph initialized with {len(st.session_state.graph.get_vertices())} vertices and {len(routes)} routes")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📍 Navigation")
        
        # Current location selection
        current_location = st.selectbox(
            "Select your current location:",
            options=list(buildings.keys()),
            index=list(buildings.keys()).index(st.session_state.current_location) if st.session_state.current_location else 0,
            key="current_loc"
        )
        
        if current_location != st.session_state.current_location:
            st.session_state.current_location = current_location
            st.success(f"📍 Current location set to: {current_location}")
        
        # Destination selection
        destinations = [b for b in buildings.keys() if b != current_location]
        destination = st.selectbox(
            "Select your destination:",
            options=destinations,
            key="destination"
        )
        
        if st.button("🚀 Find Route", use_container_width=True):
            if current_location and destination:
                with st.spinner("Finding the best route..."):
                    time.sleep(0.5)  # Animation delay
                    find_and_display_routes(current_location, destination)
        
        # Campus statistics
        st.markdown("### 📊 Campus Statistics")
        col1a, col1b, col1c = st.columns(3)
        with col1a:
            st.metric("Buildings", len(buildings))
        with col1b:
            st.metric("Routes", len(routes))
        with col1c:
            reachable = len(st.session_state.graph.get_all_reachable_vertices(current_location)) if current_location else 0
            st.metric("Reachable", reachable)
    
    with col2:
        st.markdown("### 🗺️ Campus Map")
        display_campus_map(buildings, routes)

def find_and_display_routes(start, end):
    # Check if vertices exist
    if start not in st.session_state.graph.get_vertices():
        st.error(f"❌ Start vertex '{start}' not found in graph!")
        return
    
    if end not in st.session_state.graph.get_vertices():
        st.error(f"❌ End vertex '{end}' not found in graph!")
        return
    
    # Find all paths
    all_paths = st.session_state.graph.find_all_paths(start, end, max_paths=3)
    
    if not all_paths:
        st.error(f"❌ No path found from {start} to {end}")
        return
    
    st.markdown("### 🛣️ Available Routes")
    
    # Display all paths
    for i, (path, distance) in enumerate(all_paths, 1):
        with st.container():
            st.markdown(f"""
            <div class="path-card">
                <h4>🛣️ Route {i}: {distance:.0f}m</h4>
                <p><strong>Path:</strong> {' → '.join(path)}</p>
                {f"<p style='color: #ff8c00; font-weight: 600;'>⭐ SHORTEST PATH</p>" if i == 1 else ""}
            </div>
            """, unsafe_allow_html=True)
    
    # Show recommendation
    shortest_path, shortest_distance = all_paths[0]
    st.success(f"💡 **Recommendation:** Take Route 1 ({shortest_distance:.0f}m)")

def display_campus_map(buildings, routes):
    # Create a simple network visualization using plotly
    if not routes:
        st.info("No route data available for map visualization")
        return
    
    # Prepare data for visualization
    nodes = list(buildings.keys())
    edges = [(route["from"], route["to"], route["distance"]) for route in routes]
    
    # Create node positions (simple circular layout)
    n_nodes = len(nodes)
    node_positions = {}
    for i, node in enumerate(nodes):
        angle = 2 * math.pi * i / n_nodes
        x = math.cos(angle)
        y = math.sin(angle)
        node_positions[node] = (x, y)
    
    # Create the network graph
    fig = go.Figure()
    
    # Add edges
    for from_node, to_node, distance in edges:
        if from_node in node_positions and to_node in node_positions:
            x0, y0 = node_positions[from_node]
            x1, y1 = node_positions[to_node]
            
            fig.add_trace(go.Scatter(
                x=[x0, x1],
                y=[y0, y1],
                mode='lines',
                line=dict(color='rgba(255, 165, 0, 0.6)', width=2),
                showlegend=False,
                hoverinfo='text',
                text=f"{from_node} → {to_node}<br>Distance: {distance}m"
            ))
    
    # Add nodes
    node_x = [node_positions[node][0] for node in nodes]
    node_y = [node_positions[node][1] for node in nodes]
    
    fig.add_trace(go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        marker=dict(
            size=20,
            color='rgba(255, 165, 0, 0.8)',
            line=dict(color='rgba(255, 165, 0, 1)', width=2)
        ),
        text=nodes,
        textposition="middle center",
        textfont=dict(color='white', size=10),
        showlegend=False
    ))
    
    fig.update_layout(
        title="Campus Network Map",
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        margin=dict(l=0, r=0, t=30, b=0),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Event Manager Module
def event_manager():
    st.markdown("""
    <div class="header-gradient">
        <h1>📅 Event Manager</h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### ➕ Add New Event")
        
        with st.form("add_event_form"):
            event_name = st.text_input("Event Name")
            event_date = st.date_input("Event Date")
            event_time = st.time_input("Event Time")
            event_location = st.text_input("Event Location")
            event_description = st.text_area("Event Description")
            event_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
            
            if st.form_submit_button("➕ Add Event", use_container_width=True):
                if event_name and event_location:
                    # Create event object
                    event = {
                        'name': event_name,
                        'date': event_date,
                        'time': event_time,
                        'location': event_location,
                        'description': event_description,
                        'priority': event_priority,
                        'id': len(st.session_state.events_list) + 1
                    }
                    
                    # Add to events list
                    st.session_state.events_list.append(event)
                    
                    # Add to data structures
                    st.session_state.events.insert_at_end(event)
                    st.session_state.event_tree.insert(event['name'], event)
                    
                    st.success(f"✅ Event '{event_name}' added successfully!")
                    st.rerun()
                else:
                    st.error("Please fill in all required fields!")
    
    with col2:
        st.markdown("### 📋 Current Events")
        
        if st.session_state.events_list:
            for event in st.session_state.events_list:
                with st.container():
                    st.markdown(f"""
                    <div class="event-card">
                        <h4>📅 {event['name']}</h4>
                        <p><strong>Date:</strong> {event['date']} at {event['time']}</p>
                        <p><strong>Location:</strong> {event['location']}</p>
                        <p><strong>Priority:</strong> {event['priority']}</p>
                        <p><strong>Description:</strong> {event['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("No events added yet.")
        
        col2a, col2b = st.columns(2)
        with col2a:
            if st.button("↩️ Undo", use_container_width=True):
                if st.session_state.events_list:
                    removed_event = st.session_state.events_list.pop()
                    st.success(f"Undid: {removed_event['name']}")
                    st.rerun()
                else:
                    st.info("Nothing to undo")
        
        with col2b:
            if st.button("↪️ Redo", use_container_width=True):
                st.info("Redo functionality coming soon")

# Task Scheduler Module
def task_scheduler():
    st.markdown("""
    <div class="header-gradient">
        <h1>✅ Task Scheduler</h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### ➕ Add New Task")
        
        with st.form("add_task_form"):
            task_name = st.text_input("Task Name")
            task_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
            task_deadline = st.date_input("Deadline")
            task_description = st.text_area("Task Description")
            
            if st.form_submit_button("➕ Add Task", use_container_width=True):
                if task_name:
                    # Create task object
                    task = {
                        'name': task_name,
                        'priority': task_priority,
                        'deadline': task_deadline,
                        'description': task_description,
                        'id': len(st.session_state.tasks_list) + 1,
                        'status': 'Pending'
                    }
                    
                    # Add to tasks list
                    st.session_state.tasks_list.append(task)
                    
                    # Add to queue
                    st.session_state.tasks.enqueue(task)
                    
                    st.success(f"✅ Task '{task_name}' added successfully!")
                    st.rerun()
                else:
                    st.error("Please enter a task name!")
    
    with col2:
        st.markdown("### 📋 Current Tasks")
        
        if st.session_state.tasks_list:
            for task in st.session_state.tasks_list:
                if task['status'] == 'Pending':
                    with st.container():
                        st.markdown(f"""
                        <div class="task-card">
                            <h4>✅ {task['name']}</h4>
                            <p><strong>Priority:</strong> {task['priority']}</p>
                            <p><strong>Deadline:</strong> {task['deadline']}</p>
                            <p><strong>Description:</strong> {task['description']}</p>
                            <p><strong>Status:</strong> {task['status']}</p>
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.info("No tasks added yet.")
        
        if st.button("✅ Complete Next Task", use_container_width=True):
            if st.session_state.tasks_list:
                # Find first pending task
                for task in st.session_state.tasks_list:
                    if task['status'] == 'Pending':
                        task['status'] = 'Completed'
                        st.success(f"Completed: {task['name']}")
                        st.rerun()
                        break
                else:
                    st.info("No pending tasks to complete")
            else:
                st.info("No tasks to complete")

# Event Search Tree Module
def event_search_tree():
    st.markdown("""
    <div class="header-gradient">
        <h1>🔍 Event Search Tree</h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🔍 Search Events")
        
        search_type = st.selectbox("Search Type", ["By Name", "By Date", "By Priority"])
        
        if search_type == "By Name":
            search_term = st.text_input("Enter event name")
        elif search_type == "By Date":
            search_term = st.date_input("Enter date")
        else:
            search_term = st.selectbox("Select priority", ["Low", "Medium", "High"])
        
        if st.button("🔍 Search", use_container_width=True):
            if search_term:
                search_results = perform_search(search_type, search_term)
                st.session_state.search_results = search_results
                st.success(f"Found {len(search_results)} result(s)")
            else:
                st.error("Please enter a search term!")
    
    with col2:
        st.markdown("### 📊 Search Results")
        
        if 'search_results' in st.session_state and st.session_state.search_results:
            for result in st.session_state.search_results:
                with st.container():
                    st.markdown(f"""
                    <div class="event-card">
                        <h4>📅 {result['name']}</h4>
                        <p><strong>Date:</strong> {result['date']} at {result['time']}</p>
                        <p><strong>Location:</strong> {result['location']}</p>
                        <p><strong>Priority:</strong> {result['priority']}</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("Search results will be displayed here")

def perform_search(search_type, search_term):
    results = []
    
    if search_type == "By Name":
        # Search by name using binary tree
        for event in st.session_state.events_list:
            if search_term.lower() in event['name'].lower():
                results.append(event)
    elif search_type == "By Date":
        # Search by date
        for event in st.session_state.events_list:
            if event['date'] == search_term:
                results.append(event)
    elif search_type == "By Priority":
        # Search by priority
        for event in st.session_state.events_list:
            if event['priority'] == search_term:
                results.append(event)
    
    return results

# Main application
def main():
    load_css()
    init_session_state()
    
    # Sidebar
    with st.sidebar:
        st.markdown("""
        <div class="header-gradient">
            <h2>🏫 Campus Connect</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Navigation")
        
        # Main navigation
        page = st.selectbox(
            "Choose a module:",
            ["🗺️ Campus Navigator", "📅 Event Manager", "✅ Task Scheduler", "🔍 Event Search Tree"],
            key="page_selector"
        )
        
        st.markdown("---")
        
        # Quick stats
        st.markdown("### 📊 Quick Stats")
        st.metric("Buildings", len(st.session_state.graph.get_vertices()))
        st.metric("Events", len(st.session_state.events_list))
        st.metric("Tasks", len([t for t in st.session_state.tasks_list if t['status'] == 'Pending']))
        
        st.markdown("---")
        
        # About section
        st.markdown("### ℹ️ About")
        st.markdown("""
        **Campus Connect** is a comprehensive system for UET students to:
        • Navigate campus using graph algorithms
        • Manage events with linked lists and stacks
        • Schedule tasks using queues
        • Search events efficiently with binary trees
        """)
    
    # Main content area
    if page == "🗺️ Campus Navigator":
        campus_navigator()
    elif page == "📅 Event Manager":
        event_manager()
    elif page == "✅ Task Scheduler":
        task_scheduler()
    elif page == "🔍 Event Search Tree":
        event_search_tree()

if __name__ == "__main__":
    main()
