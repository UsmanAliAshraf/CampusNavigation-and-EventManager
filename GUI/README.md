# Campus Connect - Streamlit GUI

A modern, interactive web interface for the Campus Connect Navigation & Event Planner System.

## Features

- 🎨 **Modern UI Design**: Orange, black, and dark purple color scheme
- 🗺️ **Interactive Campus Navigation**: Visual map with route finding
- 📅 **Event Management**: Add, edit, and manage events
- ✅ **Task Scheduling**: Queue-based task management
- 🔍 **Event Search**: Binary tree-based event search
- 📊 **Real-time Visualizations**: Interactive charts and graphs
- 🎯 **Responsive Design**: Works on desktop and mobile devices

## Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the Application**:
   - Open your web browser
   - Navigate to `http://localhost:8501`

## Usage

### Campus Navigator
- Select your current location from the dropdown
- Choose your destination
- View all possible routes with distances
- See the interactive campus map

### Event Manager
- Add new events with date, time, and location
- View current events
- Use undo/redo functionality

### Task Scheduler
- Add tasks with priority levels
- View current task queue
- Complete tasks in FIFO order

### Event Search Tree
- Search events by name, date, or priority
- View search results in an organized format

## Technical Details

- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas
- **Styling**: Custom CSS with gradient themes
- **State Management**: Streamlit Session State

## Color Scheme

- **Primary Orange**: `#ff8c00` to `#ff6b35`
- **Dark Purple**: `#2d1b3d`
- **Black**: `#1a1a1a`
- **Accent**: `#8b008b`

## Deployment

This application is ready for deployment on:
- Streamlit Cloud
- Heroku
- AWS
- Google Cloud Platform
- Any platform supporting Python web applications

## File Structure

```
GUI/
├── streamlit_app.py      # Main Streamlit application
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is part of the Campus Connect Navigation & Event Planner System.
