from flask import Flask, jsonify, request
import requests
import time
import json
import os

app = Flask(__name__)

# Simple in-memory cache
CACHE = {"timestamp": 0, "data": None}
CACHE_TTL = 60  # seconds

# If you already have local JSON file, set this to filename; else None
LOCAL_JSON = "sample_data.json" if os.path.exists("sample_data.json") else None

def fetch_reddit_json():
    # Use local file if present
    if LOCAL_JSON:
        with open(LOCAL_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    # caching
    now = time.time()
    if CACHE["data"] and now - CACHE["timestamp"] < CACHE_TTL:
        return CACHE["data"]

    url = "https://www.reddit.com/r/SideProject/.json"
    headers = {"User-Agent": "SideProjectFeed/0.1 by yourusername"}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    CACHE["data"] = data
    CACHE["timestamp"] = now
    return data

def simplify(data):
    posts = []
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        posts.append({
            "id": d.get("id"),
            "title": d.get("title"),
            "author": d.get("author"),
            "ups": d.get("ups"),
            "num_comments": d.get("num_comments"),
            "created_utc": d.get("created_utc"),
            "permalink": "https://reddit.com" + d.get("permalink", ""),
            "selftext": d.get("selftext"),
            "thumbnail": d.get("thumbnail") if d.get("thumbnail","").startswith("http") else None
        })
    return posts

@app.route("/api/posts")
def api_posts():
    try:
        data = fetch_reddit_json()
        posts = simplify(data)

        # optional: support query params e.g. ?q=ai or ?sort=ups
        q = request.args.get("q")
        if q:
            q = q.lower()
            posts = [p for p in posts if q in (p["title"] or "").lower() or q in (p["selftext"] or "").lower()]

        sort = request.args.get("sort", "new")  # "ups", "comments", "new"
        if sort == "ups":
            posts.sort(key=lambda x: x["ups"] or 0, reverse=True)
        elif sort == "comments":
            posts.sort(key=lambda x: x["num_comments"] or 0, reverse=True)
        else:  # new
            posts.sort(key=lambda x: x["created_utc"] or 0, reverse=True)

        return jsonify({"status": "ok", "count": len(posts), "posts": posts})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
