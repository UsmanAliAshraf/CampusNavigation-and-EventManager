#!/usr/bin/env python3
"""
Campus Connect Navigation & Event Planner System
Main Application Entry Point

This is the main entry point for the Campus Connect application.
It coordinates all modules and provides the primary interface.
"""

import sys
import os

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from CLI import CampusConnectCLI

def main():
    """Main function to start the Campus Connect application."""
    print("=" * 60)
    print("🏫 Campus Connect Navigation & Event Planner System")
    print("=" * 60)
    print("Welcome to UET Campus Connect!")
    print("Navigate campus, manage events, schedule tasks, and more.")
    print("=" * 60)
    
    try:
        # Initialize and start the CLI
        cli = CampusConnectCLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\n👋 Thank you for using Campus Connect!")
        print("Goodbye! 👋")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try again or contact support.")
    finally:
        print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
