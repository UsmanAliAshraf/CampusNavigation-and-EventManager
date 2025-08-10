#!/usr/bin/env python3
"""
Campus Connect Navigation & Event Planner System
GUI Application Launcher

This script launches the Streamlit GUI application.
"""

import subprocess
import sys
import os

def main():
    """Launch the GUI application."""
    print("🏫 Campus Connect Navigation & Event Planner System")
    print("=" * 60)
    print("Launching GUI application...")
    print("The application will open in your default web browser")
    print("URL: http://localhost:8501")
    print("=" * 60)
    
    # Get the path to the streamlit app
    gui_dir = os.path.join(os.path.dirname(__file__), "GUI")
    app_path = os.path.join(gui_dir, "streamlit_app.py")
    
    if not os.path.exists(app_path):
        print(f"❌ Streamlit app not found at {app_path}")
        print("Please ensure the GUI directory exists with streamlit_app.py")
        return
    
    # Change to GUI directory and run streamlit
    try:
        os.chdir(gui_dir)
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py", "--server.port", "8501"])
    except KeyboardInterrupt:
        print("\n👋 Campus Connect GUI closed")
    except Exception as e:
        print(f"❌ Error launching GUI: {e}")
        print("Please ensure Streamlit is installed: pip install streamlit")

if __name__ == "__main__":
    main()
