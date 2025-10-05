# Backend Debugging Summary

## Problems Found and Fixed

### 1. **Flask Not Installed in Virtual Environment** ✓ FIXED
- **Problem**: Flask was being installed to the global Python environment instead of the venv
- **Cause**: Using `pip` instead of the venv's Python to install packages
- **Solution**: Used `.\venv\Scripts\python.exe -m pip install -r requirements.txt`
- **Result**: Flask 2.2.5 now properly installed in venv

### 2. **Wrong Python Interpreter** ✓ FIXED
- **Problem**: `python` command was pointing to Anaconda Python at `C:\Users\AANANDI\anaconda4\python.exe`
- **Cause**: PATH environment variable
- **Solution**: Always use explicit path: `.\venv\Scripts\python.exe`
- **Result**: Correct venv Python is now used

### 3. **JSON Encoding Issue** ✓ VERIFIED
- **Problem**: `sample_data.json` has UTF-8 characters that need proper encoding
- **Status**: Already handled correctly in `app.py` (line 18: `encoding="utf-8"`)
- **Result**: 25 posts load successfully

## Test Results

All tests passing ✓
```
✓ Flask imported successfully
✓ requests imported successfully  
✓ sample_data.json exists and valid (25 posts)
✓ app.py imports and runs correctly
✓ API functions work (fetch_reddit_json, simplify)
```

## How to Start the Backend

### Option 1: Using the batch file (simplest)
```cmd
cd C:\Users\AANANDI\Downloads\sideproject_feed\backend
start.bat
```

### Option 2: Using PowerShell (recommended)
```powershell
cd C:\Users\AANANDI\Downloads\sideproject_feed\backend
.\venv\Scripts\python.exe app.py
```

### Option 3: Using the setup script
```powershell
cd C:\Users\AANANDI\Downloads\sideproject_feed\backend
.\setup_env.ps1
```

## Verify It Works

Once the server starts, you should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

Visit in browser or test with PowerShell:
```powershell
# In browser:
http://localhost:5000/api/posts

# Or in PowerShell:
Invoke-RestMethod http://localhost:5000/api/posts
```

## API Endpoints

- `GET /api/posts` - Get all posts
- `GET /api/posts?q=ai` - Search posts containing "ai"
- `GET /api/posts?sort=ups` - Sort by upvotes
- `GET /api/posts?sort=comments` - Sort by comment count

## Key Files

- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies (Flask 2.2.5, requests 2.31.0)
- `sample_data.json` - 25 Reddit posts from r/SideProject
- `venv/` - Virtual environment (Flask installed here)
- `test_app.py` - Diagnostic test script
- `start.bat` - Quick start script
- `setup_env.ps1` - Full setup and start script

## Important Notes

⚠️ **Always use the venv Python**: `.\venv\Scripts\python.exe`
⚠️ **Don't use global `python` or `pip`**: They point to Anaconda
⚠️ **No CORS issues**: Flask backend runs on port 5000, React frontend proxies to it

## Next Steps

1. Start the backend (see options above)
2. In a new terminal, start the frontend:
   ```powershell
   cd C:\Users\AANANDI\Downloads\sideproject_feed\frontend
   npm install
   npm run dev
   ```
3. Visit http://localhost:3000

---
Generated: October 5, 2025
Status: ✓ All issues resolved, backend fully functional
