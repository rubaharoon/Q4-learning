# 🚀 FastAPI - Hello World & Items API

This is a simple FastAPI project that includes:
- A root endpoint returning "Hello World"
- A dynamic `/items/{item_id}` endpoint with optional query parameter support

Perfect for beginners learning how to build APIs with FastAPI.

## ⚙️ Setup Instructions

### ✅ Prerequisites
- Python 3.11 or newer
- `uv` tool installed:  
  Install it if needed:
  ```bash
  pip install uv

  # Step 1: Initialize the project
uv init fastapi-app
cd fastapi-app

# Step 2: Create and activate virtual environment
uv venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Step 3: Add FastAPI and Uvicorn
uv add "fastapi[standard]"

Here is the blog link:

"https://medium.com/@ruba.haroon143/build-your-first-fastapi-app-with-uv-the-easy-way-to-say-hello-to-apis-32abfc00da3c"
