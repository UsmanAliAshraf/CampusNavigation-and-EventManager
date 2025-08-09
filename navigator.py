"""
Campus Navigator Module
Provides graph-based campus navigation using BFS, DFS, and Dijkstra's algorithms.
"""

import json
import os
from data_structures.graph import Graph
from typing import List, Tuple, Dict, Optional

class CampusNavigator:
    """
    Campus navigation system using graph algorithms.
    Models UET campus as a graph with buildings as nodes and walkways as edges.
    """
    
    def __init__(self):
        """Initialize the campus navigator with a graph."""
        self.graph = Graph()
        self.buildings = {}
        self.current_location = None
        self.load_campus_data()
    
    def load_campus_data(self):
        """Load campus buildings and routes data from JSON file."""
        try:
            # Try to load from JSON file
            json_path = os.path.join("data", "campus_data.json")
            if os.path.exists(json_path):
                with open(json_path, 'r') as file:
                    data = json.load(file)
                    self.buildings = data.get("buildings", {})
                    routes = data.get("routes", [])
            else:
                print("⚠️  campus_data.json not found. Using default data.")
                self.load_default_data()
                return
            
            # Add buildings as vertices
            for building in self.buildings.keys():
                self.graph.add_vertex(building)
            
            # Add routes with distances
            for route in routes:
                from_building = route["from"]
                to_building = route["to"]
                distance = route["distance"]
                self.graph.add_edge(from_building, to_building, distance)
                
        except Exception as e:
            print(f"❌ Error loading campus data: {e}")
            print("⚠️  Issue in loading campus_data.json. Please ensure the file exists and is valid.")
    
    def set_current_location(self, building: str) -> bool:
        """
        Set the current location for navigation.
        
        Args:
            building: Building name to set as current location
            
        Returns:
            True if location set successfully, False otherwise
        """
        if building in self.buildings:
            self.current_location = building
            return True
        return False
    
    def get_current_location(self) -> Optional[str]:
        """Get the current location."""
        return self.current_location
    
    def get_all_buildings(self) -> List[str]:
        """Get list of all buildings in campus."""
        return list(self.buildings.keys())
    
    def get_building_info(self, building: str) -> Optional[Dict]:
        """Get information about a specific building."""
        return self.buildings.get(building)
    
    def find_shortest_path(self, destination: str) -> Tuple[List[str], float]:
        """
        Find shortest path from current location to destination.
        
        Args:
            destination: Target building
            
        Returns:
            Tuple of (path as list of buildings, total distance)
        """
        if not self.current_location:
            return [], 0.0
        
        return self.graph.dijkstra(self.current_location, destination)
    
    def get_reachable_buildings(self) -> List[str]:
        """
        Get all buildings reachable from current location using BFS.
        
        Returns:
            List of reachable buildings
        """
        if not self.current_location:
            return []
        
        return self.graph.get_all_reachable_vertices(self.current_location)
    
    def explore_campus_dfs(self) -> List[str]:
        """
        Explore campus using DFS from current location.
        
        Returns:
            List of buildings in DFS order
        """
        if not self.current_location:
            return []
        
        return self.graph.dfs(self.current_location)
    
    def get_campus_info(self) -> Dict:
        """Get information about the campus graph."""
        return self.graph.get_graph_info()
    
    def display_campus_map(self):
        """Display a simple text-based campus map."""
        print("\n🗺️  UET CAMPUS MAP")
        print("=" * 40)
        
        if not self.current_location:
            print("⚠️  No current location set.")
            print("Available buildings:")
            for building in self.buildings:
                info = self.buildings[building]
                print(f"  • {building} - {info['description']}")
        else:
            print(f"📍 Current Location: {self.current_location}")
            print("\nReachable buildings:")
            reachable = self.get_reachable_buildings()
            for building in reachable:
                if building != self.current_location:
                    distance = self.graph.dijkstra(self.current_location, building)[1]
                    print(f"  • {building} ({distance:.0f}m)")
        
        print("=" * 40)
    
    def navigate_to_building(self, destination: str):
        """
        Navigate to a specific building.
        
        Args:
            destination: Target building name
        """
        if not self.current_location:
            print("❌ Please set your current location first.")
            return
        
        if destination not in self.buildings:
            print(f"❌ Building '{destination}' not found.")
            return
        
        # Find all possible paths
        all_paths = self.graph.find_all_paths(self.current_location, destination)
        
        if not all_paths:
            print(f"❌ No path found to {destination}.")
            return
        
        # Get the shortest path (first one after sorting)
        shortest_path, shortest_distance = all_paths[0]
        
        print(f"\n🗺️  NAVIGATION TO {destination.upper()}")
        print("=" * 60)
        print(f"📍 From: {self.current_location}")
        print(f"🎯 To: {destination}")
        print(f"🔍 Found {len(all_paths)} possible route(s)")
        print("=" * 60)
        
        # Display all paths
        for i, (path, distance) in enumerate(all_paths, 1):
            path_str = " → ".join(path)
            print(f"\n🛣️  Route {i}: {path_str}")
            print(f"   📏 Distance: {distance:.0f} meters")
            
            if i == 1:
                print(f"   ⭐ SHORTEST PATH (Dijkstra's Algorithm)")
        
        print("\n" + "=" * 60)
        print(f"💡 RECOMMENDATION: Take Route 1 ({shortest_distance:.0f}m)")
        print("=" * 60)
    
    def run_navigation_menu(self):
        """Run the navigation module menu."""
        while True:
            print("\n🗺️  CAMPUS NAVIGATOR")
            print("=" * 30)
            print("1. 🗺️  View Campus Map")
            print("2. 🧭 Navigate to Building")
            print("3. 🔍 Explore Campus (DFS)")
            print("4. 📊 Campus Information")
            print("5. ↩️  Back to Main Menu")
            print("=" * 30)
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.display_campus_map()
                input("Press Enter to continue...")
            elif choice == "2":
                self.navigate_menu()
            elif choice == "3":
                self.explore_campus_menu()
            elif choice == "4":
                self.show_campus_info()
            elif choice == "5":
                break
            else:
                print("❌ Invalid choice. Please try again.")
    
    def navigate_menu(self):
        """Menu for navigation."""
        print(f"\n🧭 NAVIGATE TO BUILDING")
        print("=" * 40)
        
        buildings = self.get_all_buildings()
        
        # First, ask for current location if not set
        if not self.current_location:
            print("📍 Select your current location:")
            for i, building in enumerate(buildings, 1):
                print(f"{i}. {building}")
            
            try:
                choice = int(input("\nEnter current location number: ")) - 1
                if 0 <= choice < len(buildings):
                    current_location = buildings[choice]
                    self.set_current_location(current_location)
                    print(f"✅ Current location set to: {current_location}")
                else:
                    print("❌ Invalid choice.")
                    input("Press Enter to continue...")
                    return
            except ValueError:
                print("❌ Please enter a valid number.")
                input("Press Enter to continue...")
                return
        else:
            print(f"📍 Current location: {self.current_location}")
        
        # Now ask for destination
        print(f"\n🎯 Select your destination:")
        for i, building in enumerate(buildings, 1):
            if building != self.current_location:
                print(f"{i}. {building}")
        
        try:
            choice = int(input("\nEnter destination number: ")) - 1
            if 0 <= choice < len(buildings):
                destination = buildings[choice]
                if destination != self.current_location:
                    self.navigate_to_building(destination)
                else:
                    print("❌ Cannot navigate to current location.")
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")
        
        input("Press Enter to continue...")
    
    def explore_campus_menu(self):
        """Menu for campus exploration."""
        print(f"\n🔍 EXPLORE CAMPUS")
        print("=" * 50)
        
        buildings = self.get_all_buildings()
        
        # First, ask for current location if not set
        if not self.current_location:
            print("📍 Select your starting location for exploration:")
            for i, building in enumerate(buildings, 1):
                print(f"{i}. {building}")
            
            try:
                choice = int(input("\nEnter starting location number: ")) - 1
                if 0 <= choice < len(buildings):
                    current_location = buildings[choice]
                    self.set_current_location(current_location)
                    print(f"✅ Starting location set to: {current_location}")
                else:
                    print("❌ Invalid choice.")
                    input("Press Enter to continue...")
                    return
            except ValueError:
                print("❌ Please enter a valid number.")
                input("Press Enter to continue...")
                return
        else:
            print(f"📍 Starting location: {self.current_location}")
        
        print(f"\n🔍 EXPLORING CAMPUS FROM {self.current_location.upper()}")
        print("=" * 50)
        
        path = self.explore_campus_dfs()
        print("DFS Exploration Path:")
        for i, building in enumerate(path, 1):
            print(f"  {i}. {building}")
        
        print(f"\nTotal buildings explored: {len(path)}")
        input("Press Enter to continue...")
    
    def show_campus_info(self):
        """Show campus graph information."""
        print("\n📊 CAMPUS INFORMATION")
        print("=" * 30)
        
        info = self.get_campus_info()
        print(f"🏢 Total Buildings: {info['vertices']}")
        print(f"🛣️  Total Routes: {info['edges']}")
        print(f"🔗 Connected: {'Yes' if info['connected'] else 'No'}")
        
        if self.current_location:
            reachable = self.get_reachable_buildings()
            print(f"📍 Reachable from {self.current_location}: {len(reachable)} buildings")
        
        input("Press Enter to continue...")
