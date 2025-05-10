# Step 3: API Parameters in FastAPI

This project demonstrates how to work with different types of parameters in a FastAPI application, focusing on **path parameters**, **query parameters**, and **request bodies** with enhanced validation.

## 🔧 Setup Instructions

1. **Initialize project and environment**

   uv init fastdca_p1
   cd fastdca_p1
   uv venv
   source .venv/bin/activate

2. **Install dependencies**

uv add "fastapi[standard]"

3. **Run the server**

fastapi dev main.py

**📦 Parameter Types in FastAPI**

FastAPI allows for robust parameter validation and supports the following input sources:

Path Parameters: /items/{item_id}
Query Parameters: /items?skip=0&limit=10
Request Body: JSON data in PUT/POST requests
Headers
Cookies
Form Data
File Uploads

In this example, we focus on path parameters, query parameters, and request body validation.

🛠️ Examples
✅ Path Parameter Validation

from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(..., title="The ID of the item", description="A unique identifier", ge=1)
):
    return {"item_id": item_id}
✅ Query Parameter Validation

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query(None, title="Query string", min_length=3, max_length=50),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return {"q": q, "skip": skip, "limit": limit}
✅ Combining Parameters (Path, Query, Body)

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

app = FastAPI()

@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result

**💡 Key Points**

Use Path() and Query() for validation and metadata.

Available validation options:

ge, gt, le, lt — numeric bounds

min_length, max_length — string length constraints

regex — pattern matching

enum — restrict to specific values

FastAPI will return a 422 Unprocessable Entity for validation errors with detailed messages.

Here is the blog link:

"https://medium.com/@ruba.haroon143/fastapi-secrets-mastering-parameters-for-rock-solid-apis-d8db040384c9"






