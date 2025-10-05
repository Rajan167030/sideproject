"""
Test script to verify the Flask app works correctly
"""
import json
import os

print("=" * 60)
print("BACKEND DIAGNOSTICS")
print("=" * 60)

# Test 1: Check if Flask is importable
print("\n1. Testing Flask import...")
try:
    from flask import Flask, jsonify, request
    print("   ✓ Flask imported successfully")
except ImportError as e:
    print(f"   ✗ Flask import failed: {e}")
    exit(1)

# Test 2: Check if requests is importable
print("\n2. Testing requests import...")
try:
    import requests
    print("   ✓ requests imported successfully")
except ImportError as e:
    print(f"   ✗ requests import failed: {e}")
    exit(1)

# Test 3: Check if sample_data.json exists and is valid
print("\n3. Testing sample_data.json...")
if os.path.exists("sample_data.json"):
    print("   ✓ sample_data.json exists")
    try:
        with open("sample_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        post_count = len(data.get("data", {}).get("children", []))
        print(f"   ✓ Valid JSON with {post_count} posts")
    except Exception as e:
        print(f"   ✗ JSON validation failed: {e}")
        exit(1)
else:
    print("   ⚠ sample_data.json not found (will fetch from Reddit)")

# Test 4: Import and test the app
print("\n4. Testing app.py functions...")
try:
    import app as flask_app
    print("   ✓ app.py imported successfully")
    
    # Test fetch_reddit_json
    data = flask_app.fetch_reddit_json()
    print("   ✓ fetch_reddit_json() works")
    
    # Test simplify
    posts = flask_app.simplify(data)
    print(f"   ✓ simplify() works - returned {len(posts)} posts")
    
    if posts:
        print(f"\n   Sample post:")
        sample = posts[0]
        print(f"   - Title: {sample['title'][:60]}...")
        print(f"   - Author: {sample['author']}")
        print(f"   - Ups: {sample['ups']}")
        print(f"   - Comments: {sample['num_comments']}")
    
except Exception as e:
    print(f"   ✗ App test failed: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n" + "=" * 60)
print("✓ ALL TESTS PASSED - Backend is working correctly!")
print("=" * 60)
print("\nYou can now run: python app.py")
print("Then visit: http://localhost:5000/api/posts")
