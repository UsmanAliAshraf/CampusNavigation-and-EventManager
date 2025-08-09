#!/usr/bin/env python3
"""
Campus Connect - Streamlit GUI Launcher
This script launches the Streamlit GUI application.
"""

import subprocess
import sys
import os

def main():
    """Launch the Streamlit GUI application."""
    print("🏫 Campus Connect - Streamlit GUI")
    print("=" * 50)
    
    # Check if streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit is not installed")
        print("Installing required dependencies...")
        
        # Install requirements
        requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
        if os.path.exists(requirements_path):
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit", "plotly", "pandas", "numpy"])
    
    # Get the path to the streamlit app
    app_path = os.path.join(os.path.dirname(__file__), "streamlit_app.py")
    
    if not os.path.exists(app_path):
        print(f"❌ Streamlit app not found at {app_path}")
        return
    
    print("🚀 Launching Campus Connect GUI...")
    print("📱 The application will open in your default web browser")
    print("🌐 URL: http://localhost:8501")
    print("=" * 50)
    
    # Launch streamlit
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_path, "--server.port", "8501"])
    except KeyboardInterrupt:
        print("\n👋 Campus Connect GUI closed")
    except Exception as e:
        print(f"❌ Error launching GUI: {e}")

if __name__ == "__main__":
    main()
