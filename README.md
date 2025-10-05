# 📱 r/SideProject Feed - Full Stack Web Application

A full-stack web application that displays posts from Reddit's r/SideProject community with search, sort, and filtering capabilities.

![Tech Stack](https://img.shields.io/badge/Frontend-React-61dafb?style=flat-square&logo=react)
![Tech Stack](https://img.shields.io/badge/Backend-Flask-000000?style=flat-square&logo=flask)
![Tech Stack](https://img.shields.io/badge/Language-Python%20%7C%20JavaScript-blue?style=flat-square)


<img width="1923" height="883" alt="Screenshot 2025-10-05 161903" src="https://github.com/user-attachments/assets/a12a4c4f-2f87-4e3b-9d5a-6dd909344b96" />


🔗 **GitHub Repository:** [https://github.com/Rajan167030/sideproject](https://github.com/Rajan167030/sideproject)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [File Analysis](#file-analysis)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

This application fetches and displays posts from Reddit's r/SideProject subreddit. It consists of:
- **Backend**: Flask REST API that fetches data from Reddit or serves cached local JSON
- **Frontend**: React SPA with search, sort, and filter functionality
- **Data**: 25 pre-loaded Reddit posts with full metadata

---

## ✨ Features

### Frontend Features
- ✅ Real-time search across post titles and content
- ✅ Multiple sort options (Newest, Top by upvotes, Top by comments)
- ✅ Responsive card-based UI
- ✅ Live refresh functionality
- ✅ Clean, minimal design
- ✅ Thumbnail preview support

### Backend Features
- ✅ RESTful API endpoints
- ✅ Smart caching (60-second TTL)
- ✅ Local JSON fallback (no internet required)
- ✅ Query parameter support for filtering and sorting
- ✅ Error handling with proper HTTP status codes
- ✅ CORS-ready (proxied through React dev server)

---

## 🛠️ Tech Stack

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.13 | Runtime environment |
| **Flask** | 2.2.5 | Web framework |
| **requests** | 2.31.0 | HTTP client for Reddit API |
| **Werkzeug** | >=2.2.2 | WSGI utility library |
| **Jinja2** | >=3.0 | Template engine (Flask dependency) |

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| **React** | 18.2.0 | UI library |
| **react-dom** | 18.2.0 | React DOM renderer |
| **react-scripts** | 5.0.1 | Create React App tooling |
| **cross-env** | 7.0.3 | Cross-platform environment variables |

---

## 📁 Project Structure

```
sideproject_feed/
│
├── backend/                          # Flask API Server
│   ├── app.py                        # Main Flask application (83 lines)
│   ├── requirements.txt              # Python dependencies
│   ├── sample_data.json              # 25 cached Reddit posts (4289 lines)
│   ├── test_app.py                   # Diagnostic test suite (73 lines)
│   ├── setup_env.ps1                 # PowerShell setup script (38 lines)
│   ├── start.bat                     # Windows batch start script
│   ├── DEBUG_SUMMARY.md              # Debug documentation
│   └── venv/                         # Python virtual environment
│       └── Scripts/
│           └── python.exe            # Isolated Python interpreter
│
├── frontend/                         # React Application
│   ├── package.json                  # NPM dependencies & scripts
│   ├── public/
│   │   └── index.html                # HTML template (10 lines)
│   ├── src/
│   │   ├── index.js                  # React entry point (7 lines)
│   │   ├── App.js                    # Main App component (56 lines)
│   │   └── components/
│   │       └── PostCard.js           # Post card component (14 lines)
│   └── node_modules/                 # NPM packages
│
├── README.md                         # Project documentation (this file)
└── README_RUN.txt                    # Quick start instructions
```

---

## 📥 Installation

### Prerequisites
- **Python 3.7+** (tested on 3.13)
- **Node.js 14+** and npm
- **Windows PowerShell** (for Windows users)
- **Git** (optional, for cloning)

### Step 1: Clone/Extract the Project

**Option A: Clone from GitHub**
```powershell
git clone https://github.com/Rajan167030/sideproject.git
cd sideproject
```

**Option B: If you have the ZIP file**
```powershell
cd C:\Users\AANANDI\Downloads\sideproject_feed
```

### Step 2: Backend Setup

#### Option A: Automated Setup (Recommended)
```powershell
cd backend
.\setup_env.ps1
```

#### Option B: Manual Setup
```powershell
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Verify installation
python -m pip show Flask
```

### Step 3: Frontend Setup
```powershell
cd frontend

# Install dependencies
npm install

# Install cross-env for cross-platform compatibility
npm install --save-dev cross-env
```

---

## 🚀 Usage

### Starting the Application

#### 1. Start Backend Server
Open PowerShell in the `backend` folder:

```powershell
# Using batch file (simplest)
.\start.bat

# OR using Python directly
.\venv\Scripts\python.exe app.py

# OR with global Python (if venv activated)
python app.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Debugger PIN: xxx-xxx-xxx
```

#### 2. Start Frontend Server
Open a **new** PowerShell window in the `frontend` folder:

```powershell
npm run dev
# OR
npm start
```

**Expected output:**
```
Compiled successfully!

You can now view sideproject-feed in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.x.x:3000
```

#### 3. Access the Application
Open your browser and navigate to:
```
http://localhost:3000
```

---

## 📡 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### `GET /api/posts`
Retrieve posts from r/SideProject

**Query Parameters:**
| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `q` | string | Search query (title or content) | `?q=ai` |
| `sort` | string | Sort order: `new`, `ups`, `comments` | `?sort=ups` |

**Response Format:**
```json
{
  "status": "ok",
  "count": 25,
  "posts": [
    {
      "id": "1nyfuav",
      "title": "I built real dark mode for my website...",
      "author": "the2ndfloorguy",
      "ups": 16,
      "num_comments": 7,
      "created_utc": 1728121847,
      "permalink": "https://reddit.com/r/SideProject/...",
      "selftext": "I spent my weekend building...",
      "thumbnail": "https://..."
    }
  ]
}
```

**Example Requests:**

```powershell
# Get all posts (newest first)
Invoke-RestMethod http://localhost:5000/api/posts

# Search for posts containing "AI"
Invoke-RestMethod http://localhost:5000/api/posts?q=ai

# Get top posts by upvotes
Invoke-RestMethod http://localhost:5000/api/posts?sort=ups

# Get top posts by comments
Invoke-RestMethod http://localhost:5000/api/posts?sort=comments
```

---

## 🔍 File Analysis

### Backend Files

#### `app.py` (83 lines)
**Purpose:** Main Flask application server

**Key Components:**
```python
# Imports
from flask import Flask, jsonify, request
import requests, time, json, os

# Configuration
CACHE_TTL = 60  # seconds
LOCAL_JSON = "sample_data.json"

# Functions
- fetch_reddit_json()     # Fetches from local file or Reddit API
- simplify(data)          # Transforms Reddit JSON to simplified format
- api_posts()             # API endpoint handler

# Routes
@app.route("/api/posts")  # Main API endpoint
```

**Features:**
- In-memory caching with 60-second TTL
- Automatic fallback to local JSON file
- Support for search (`?q=`) and sort (`?sort=`) parameters
- Error handling with 500 status codes
- Debug mode enabled for development

#### `requirements.txt` (2 lines)
```
Flask==2.2.5
requests==2.31.0
```

#### `sample_data.json` (4289 lines)
**Purpose:** Cached Reddit API response with 25 posts from r/SideProject

**Structure:**
```json
{
  "kind": "Listing",
  "data": {
    "children": [
      {
        "kind": "t3",
        "data": {
          "title": "...",
          "author": "...",
          "ups": 16,
          "num_comments": 7,
          // ... full Reddit post metadata
        }
      }
    ]
  }
}
```

#### `test_app.py` (73 lines)
**Purpose:** Comprehensive diagnostic test suite

**Tests:**
1. Flask import verification
2. requests library verification
3. JSON file validation
4. App functionality testing
5. Sample data display

#### `setup_env.ps1` (38 lines)
**Purpose:** Automated PowerShell setup script

**Actions:**
- Creates virtual environment
- Upgrades pip
- Installs requirements
- Verifies Flask installation
- Starts the Flask app

#### `start.bat` (5 lines)
**Purpose:** Simple Windows batch script to start Flask server

#### `DEBUG_SUMMARY.md`
**Purpose:** Debugging documentation with solutions to common issues

---

### Frontend Files

#### `src/App.js` (56 lines)
**Purpose:** Main React application component

**State Management:**
```javascript
const [posts, setPosts] = useState([]);      // Post data
const [q, setQ] = useState("");              // Search query
const [loading, setLoading] = useState(false); // Loading state
const [sort, setSort] = useState("new");     // Sort option
```

**Features:**
- `useEffect` hook for data fetching on mount and sort change
- Client-side filtering for search
- API integration with `/api/posts`
- Error handling in try-catch blocks

**UI Components:**
- Search input field
- Sort dropdown (Newest, Top by ups, Top by comments)
- Refresh button
- Post card list

#### `src/components/PostCard.js` (14 lines)
**Purpose:** Reusable post card component

**Props:**
- `post` object with title, author, ups, num_comments, thumbnail, selftext, permalink

**Rendering:**
- Clickable title (opens Reddit permalink)
- Author name and post metadata
- Thumbnail image (if available)
- Truncated self-text preview (200 characters)

#### `src/index.js` (7 lines)
**Purpose:** React application entry point

**Functionality:**
- Creates root React element
- Renders `<App />` component into `#root` div

#### `public/index.html` (10 lines)
**Purpose:** HTML template for React SPA

**Contents:**
- Meta tags for charset and viewport
- Title: "r/SideProject Feed"
- Root div for React mounting

#### `package.json` (30 lines)
**Purpose:** NPM configuration and dependencies

**Scripts:**
```json
{
  "start": "cross-env PORT=3000 react-scripts start",
  "dev": "cross-env PORT=3000 react-scripts start",
  "build": "react-scripts build"
}
```

**Key Configuration:**
- `"proxy": "http://localhost:5000"` - Routes API calls to Flask backend
- React 18.2.0 with Hooks support
- Create React App 5.0.1 tooling

---

## 🐛 Troubleshooting

### Backend Issues

#### Issue: `ModuleNotFoundError: No module named 'flask'`
**Cause:** Flask not installed in virtual environment  
**Solution:**
```powershell
cd backend
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

#### Issue: `UnicodeDecodeError` when reading JSON
**Cause:** JSON file has UTF-8 characters  
**Solution:** Already handled in `app.py` with `encoding="utf-8"`

#### Issue: Wrong Python interpreter
**Cause:** Using global Python instead of venv  
**Solution:** Always use `.\venv\Scripts\python.exe` explicitly

#### Issue: `404 Not Found` on `http://localhost:5000/`
**Cause:** Root path has no route  
**Solution:** Use `/api/posts` endpoint instead

### Frontend Issues

#### Issue: `npm run dev` - Missing script error
**Cause:** Old `package.json` without `dev` script  
**Solution:** Use `npm start` or update `package.json`

#### Issue: `PORT is not recognized` error
**Cause:** Windows doesn't support `PORT=3000` syntax  
**Solution:** Install `cross-env`:
```powershell
npm install --save-dev cross-env
```

#### Issue: API calls fail with CORS error
**Cause:** Proxy not configured  
**Solution:** Verify `"proxy": "http://localhost:5000"` in `package.json`

### General Issues

#### Issue: Backend works but frontend can't connect
**Solution:**
1. Verify backend is running on port 5000
2. Check `package.json` has proxy configured
3. Restart frontend dev server

#### Issue: Ports already in use
**Solution:**
```powershell
# Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Kill process on port 3000
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

---

## 📊 Application Flow

```
┌─────────────────────────────────────────────────────────────┐
│                         USER BROWSER                        │
│                    http://localhost:3000                    │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                    REACT FRONTEND (PORT 3000)               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  App.js                                             │   │
│  │  - Fetches data from /api/posts                     │   │
│  │  - Handles search & sort logic                      │   │
│  │  - Renders PostCard components                      │   │
│  └─────────────────────────────────────────────────────┘   │
│              │                                              │
│              │ Proxy: http://localhost:5000                 │
└──────────────┼──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│                   FLASK BACKEND (PORT 5000)                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  app.py                                             │   │
│  │  @app.route("/api/posts")                           │   │
│  │                                                      │   │
│  │  1. Check if sample_data.json exists                │   │
│  │     ├─ YES: Load from local file (UTF-8)            │   │
│  │     └─ NO: Fetch from Reddit API with caching       │   │
│  │                                                      │   │
│  │  2. Simplify data structure                         │   │
│  │  3. Apply filters (q parameter)                     │   │
│  │  4. Apply sorting (sort parameter)                  │   │
│  │  5. Return JSON response                            │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔐 Security Notes

⚠️ **Development Mode Only**
- Flask debug mode is enabled (`debug=True`)
- No authentication or authorization
- No input sanitization on search queries
- CORS handled via proxy (not production-ready)

**For Production:**
- Use Gunicorn/uWSGI instead of Flask dev server
- Disable debug mode
- Implement proper CORS headers
- Add input validation and sanitization
- Use environment variables for configuration
- Add rate limiting

---

## 📈 Performance Considerations

- **Caching:** Backend caches Reddit API responses for 60 seconds
- **Local Data:** Uses `sample_data.json` to avoid API rate limits
- **Client-side Filtering:** Search is performed on frontend (fast, but loads all data)
- **Minimal Dependencies:** Small bundle size for quick loading

---

## 🎨 Customization

### Change Port Numbers

**Backend (Flask):**
Edit `app.py`, line 83:
```python
app.run(debug=True, port=5000)  # Change 5000 to desired port
```

**Frontend (React):**
Edit `package.json`, scripts section:
```json
"start": "cross-env PORT=3000 react-scripts start"  // Change 3000
```

Don't forget to update the proxy setting in `package.json`:
```json
"proxy": "http://localhost:5000"  // Match backend port
```

### Add More Reddit Data

Replace `backend/sample_data.json` with fresh data from:
```
https://www.reddit.com/r/SideProject/.json
```

Or change the subreddit in `app.py`, line 27:
```python
url = "https://www.reddit.com/r/SideProject/.json"
```

---

## 📝 License

This project is for educational purposes. Reddit data is subject to Reddit's API terms and policies.

---

## 👨‍💻 Author

**Created:** October 5, 2025  
**Platform:** Windows 11 with Python 3.13 & Node.js  
**Status:** ✅ Fully functional and tested  
**GitHub:** [@Rajan167030](https://github.com/Rajan167030)  
**Repository:** [https://github.com/Rajan167030/sideproject](https://github.com/Rajan167030/sideproject)

---

## 🙏 Acknowledgments

- Reddit API for data
- r/SideProject community
- Flask and React communities
- Create React App team

---

**Happy Coding! 🚀**
