# Campus Connect - Streamlit GUI Deployment Guide

## 🎯 Overview

This guide provides comprehensive instructions for deploying and running the Campus Connect Streamlit GUI application. The application features a modern, interactive interface with orange, black, and dark purple color scheme, designed for professional deployment.

## 🏗️ Architecture

### Frontend
- **Framework**: Streamlit 1.28.1+
- **Styling**: Custom CSS with gradient themes
- **Visualization**: Plotly for interactive charts
- **State Management**: Streamlit Session State

### Backend Integration
- **Data Structures**: Custom Python implementations
  - Graph (for campus navigation)
  - DoublyLinkedList (for events)
  - Stack (for undo/redo)
  - Queue (for tasks)
  - BinarySearchTree (for event search)

### Color Scheme
- **Primary Orange**: `#ff8c00` to `#ff6b35`
- **Dark Purple**: `#2d1b3d`
- **Black**: `#1a1a1a`
- **Accent**: `#8b008b`

## 🚀 Quick Start

### Option 1: Using the Launcher Script (Recommended)

#### Windows
```bash
# Navigate to GUI directory
cd CampusNavigation-and-EventManager/GUI

# Run the batch file
run_gui.bat
```

#### Linux/Mac
```bash
# Navigate to GUI directory
cd CampusNavigation-and-EventManager/GUI

# Run the Python launcher
python run_gui.py
```

### Option 2: Manual Installation

1. **Install Dependencies**:
   ```bash
   cd CampusNavigation-and-EventManager/GUI
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   streamlit run streamlit_app.py --server.port 8501
   ```

3. **Access the Application**:
   - Open your web browser
   - Navigate to `http://localhost:8501`

## 📁 File Structure

```
GUI/
├── streamlit_app.py      # Main Streamlit application
├── requirements.txt      # Python dependencies
├── run_gui.py           # Python launcher script
├── run_gui.bat          # Windows batch launcher
├── README.md            # Basic documentation
└── DEPLOYMENT_GUIDE.md  # This file
```

## 🎨 Features

### 1. Campus Navigator
- **Interactive Map**: Visual campus network with Plotly
- **Route Finding**: All possible paths with distances
- **Shortest Path**: Dijkstra's algorithm implementation
- **Real-time Updates**: Dynamic route calculation

### 2. Event Manager
- **Add Events**: Form-based event creation
- **Event Display**: Card-based event listing
- **Undo/Redo**: Stack-based functionality
- **Priority Levels**: Low, Medium, High

### 3. Task Scheduler
- **Queue Management**: FIFO task processing
- **Task Status**: Pending/Completed tracking
- **Priority System**: Task prioritization
- **Deadline Management**: Date-based scheduling

### 4. Event Search Tree
- **Multiple Search Types**: Name, Date, Priority
- **Binary Tree**: Efficient search implementation
- **Real-time Results**: Instant search feedback
- **Filtered Display**: Organized result presentation

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Set custom port
export STREAMLIT_SERVER_PORT=8501

# Optional: Set custom host
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### Customization
1. **Colors**: Modify CSS in `streamlit_app.py`
2. **Layout**: Adjust column configurations
3. **Features**: Enable/disable modules in sidebar

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Deploy automatically

### 2. Heroku
1. Create `Procfile`:
   ```
   web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Deploy using Heroku CLI

### 3. AWS/GCP
1. Use Docker containerization
2. Deploy to cloud platform
3. Configure load balancer

### 4. Local Network
1. Set `server.address=0.0.0.0`
2. Configure firewall rules
3. Access via local IP

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**:
   ```bash
   # Ensure parent directory is in Python path
   export PYTHONPATH="${PYTHONPATH}:$(pwd)/.."
   ```

2. **Port Already in Use**:
   ```bash
   # Use different port
   streamlit run streamlit_app.py --server.port 8502
   ```

3. **Dependencies Missing**:
   ```bash
   # Reinstall requirements
   pip install -r requirements.txt --force-reinstall
   ```

4. **Data File Not Found**:
   - Ensure `data/campus_data.json` exists
   - Check file permissions

### Performance Optimization

1. **Caching**: Use `@st.cache_data` for expensive operations
2. **Lazy Loading**: Load data only when needed
3. **Session State**: Minimize state updates
4. **Memory Management**: Clear unused data

## 📊 Monitoring

### Health Checks
- Application responsiveness
- Memory usage
- Error rates
- User activity

### Logging
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

## 🔒 Security

### Best Practices
1. **Input Validation**: Sanitize user inputs
2. **Authentication**: Implement user login (if needed)
3. **HTTPS**: Use SSL certificates in production
4. **Rate Limiting**: Prevent abuse

### Environment Security
```bash
# Secure environment variables
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_SERVER_ENABLE_CORS=false
```

## 📈 Scaling

### Horizontal Scaling
1. **Load Balancer**: Distribute traffic
2. **Multiple Instances**: Run multiple app instances
3. **Database**: Use external database for persistence

### Vertical Scaling
1. **Resource Allocation**: Increase CPU/memory
2. **Optimization**: Profile and optimize code
3. **Caching**: Implement Redis/memcached

## 🎯 Future Enhancements

### Planned Features
1. **User Authentication**: Login system
2. **Data Persistence**: Database integration
3. **Real-time Updates**: WebSocket support
4. **Mobile App**: React Native companion
5. **API Integration**: RESTful API endpoints

### Technical Improvements
1. **Testing**: Unit and integration tests
2. **CI/CD**: Automated deployment pipeline
3. **Documentation**: API documentation
4. **Performance**: Optimization and caching

## 📞 Support

### Getting Help
1. **Documentation**: Check README.md
2. **Issues**: Create GitHub issue
3. **Community**: Streamlit community forums
4. **Email**: Contact development team

### Contributing
1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

## 📄 License

This project is part of the Campus Connect Navigation & Event Planner System.
All rights reserved.

---

**Last Updated**: January 2025
**Version**: 1.0.0
**Author**: Campus Connect Development Team
