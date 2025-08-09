#!/usr/bin/env python3
"""
Test script to demonstrate Main Gate to Hostel navigation
"""

from navigator import CampusNavigator

def test_main_gate_to_hostel():
    """Test navigation from Main Gate to Hostel"""
    print("🧪 TESTING MAIN GATE TO HOSTEL NAVIGATION")
    print("=" * 50)
    
    # Initialize navigator
    navigator = CampusNavigator()
    
    # Set current location
    navigator.set_current_location("Main Gate")
    print(f"📍 Current Location: {navigator.get_current_location()}")
    
    # Navigate to Hostel
    print("\n🗺️  Finding all routes from Main Gate to Hostel...")
    navigator.navigate_to_building("Hostel")

if __name__ == "__main__":
    test_main_gate_to_hostel()
