#!/usr/bin/env python3
"""
Check connections from Main Gate
"""

from navigator import CampusNavigator

def check_main_gate_connections():
    """Check what routes are connected to Main Gate"""
    print("🔍 CHECKING MAIN GATE CONNECTIONS")
    print("=" * 50)
    
    # Initialize navigator
    navigator = CampusNavigator()
    
    # Check Main Gate connections
    main_gate_neighbors = navigator.graph.get_neighbors("Main Gate")
    print(f"📍 Main Gate connections:")
    for neighbor, weight in main_gate_neighbors:
        print(f"   Main Gate → {neighbor}: {weight}m")
    
    print(f"\n🔍 Library connections:")
    library_neighbors = navigator.graph.get_neighbors("Library")
    for neighbor, weight in library_neighbors:
        print(f"   Library → {neighbor}: {weight}m")
    
    print(f"\n🔍 CRP Department connections:")
    crp_neighbors = navigator.graph.get_neighbors("CRP Department")
    for neighbor, weight in crp_neighbors:
        print(f"   CRP Department → {neighbor}: {weight}m")
    
    print(f"\n🔍 Bus Stand connections:")
    bus_stand_neighbors = navigator.graph.get_neighbors("Bus Stand")
    for neighbor, weight in bus_stand_neighbors:
        print(f"   Bus Stand → {neighbor}: {weight}m")
    
    print(f"\n🔍 SSC Cafe connections:")
    ssc_cafe_neighbors = navigator.graph.get_neighbors("SSC Cafe")
    for neighbor, weight in ssc_cafe_neighbors:
        print(f"   SSC Cafe → {neighbor}: {weight}m")

if __name__ == "__main__":
    check_main_gate_connections()
