#!/usr/bin/env python3
"""
Find specific route: Main Gate -> Library -> CRP -> Bus Stand -> SSC Cafe -> Hostel
"""

from navigator import CampusNavigator

def find_specific_route():
    """Find the specific route we expect"""
    print("LOOKING FOR SPECIFIC ROUTE")
    print("=" * 50)
    
    # Initialize navigator
    navigator = CampusNavigator()
    
    # Check if the expected route exists
    expected_route = ["Main Gate", "Library", "CRP Department", "Bus Stand", "SSC Cafe", "Hostel"]
    
    print("Expected route: Main Gate -> Library -> CRP Department -> Bus Stand -> SSC Cafe -> Hostel")
    print("Expected distance: 70 + 30 + 30 + 40 + 40 = 210m")
    print("\nChecking if this route exists...")
    
    # Check each step of the route
    total_distance = 0
    route_exists = True
    
    for i in range(len(expected_route) - 1):
        from_building = expected_route[i]
        to_building = expected_route[i + 1]
        
        # Check if this connection exists
        neighbors = navigator.graph.get_neighbors(from_building)
        connection_found = False
        
        for neighbor, weight in neighbors:
            if neighbor == to_building:
                print(f"✓ {from_building} -> {to_building}: {weight}m")
                total_distance += weight
                connection_found = True
                break
        
        if not connection_found:
            print(f"✗ {from_building} -> {to_building}: NOT FOUND")
            route_exists = False
    
    print(f"\nTotal distance: {total_distance}m")
    print(f"Route exists: {route_exists}")
    
    # Now check what the system actually finds
    print("\n" + "=" * 50)
    print("WHAT THE SYSTEM ACTUALLY FINDS:")
    
    all_paths = navigator.graph.find_all_paths("Main Gate", "Hostel")
    
    for i, (path, distance) in enumerate(all_paths[:5], 1):  # Show first 5 routes
        path_str = " -> ".join(path)
        print(f"\nRoute {i}: {path_str}")
        print(f"Distance: {distance:.0f}m")
        
        # Check if this is our expected route
        if path == expected_route:
            print("*** THIS IS OUR EXPECTED ROUTE! ***")

if __name__ == "__main__":
    find_specific_route()
