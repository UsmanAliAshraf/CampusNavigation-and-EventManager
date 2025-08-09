#!/usr/bin/env python3
"""
Debug script to trace path calculation
"""

from navigator import CampusNavigator

def debug_main_gate_to_hostel():
    """Debug the Main Gate to Hostel path calculation"""
    print("🔍 DEBUGGING MAIN GATE TO HOSTEL PATH")
    print("=" * 50)
    
    # Initialize navigator
    navigator = CampusNavigator()
    
    # Set current location
    navigator.set_current_location("Main Gate")
    print(f"📍 Current Location: {navigator.get_current_location()}")
    
    # Get all paths
    all_paths = navigator.graph.find_all_paths("Main Gate", "Hostel")
    
    print(f"\n🔍 Found {len(all_paths)} possible paths:")
    print("=" * 50)
    
    for i, (path, distance) in enumerate(all_paths, 1):
        path_str = " → ".join(path)
        print(f"\n🛣️  Route {i}: {path_str}")
        print(f"   📏 Distance: {distance:.0f} meters")
        
        # Calculate distance manually
        manual_distance = 0
        for j in range(len(path) - 1):
            from_building = path[j]
            to_building = path[j + 1]
            # Find the edge weight
            for neighbor, weight in navigator.graph.get_neighbors(from_building):
                if neighbor == to_building:
                    manual_distance += weight
                    print(f"      {from_building} → {to_building}: {weight}m")
                    break
        
        print(f"   🔢 Manual calculation: {manual_distance:.0f}m")
        
        if i == 1:
            print(f"   ⭐ SHORTEST PATH (Dijkstra's Algorithm)")

if __name__ == "__main__":
    debug_main_gate_to_hostel()
