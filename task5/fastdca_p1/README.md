🚀 Step 4: Dependency Injection in FastAPI
Welcome to Step 4 of your FastAPI learning journey! In this step, we unlock one of FastAPI’s most powerful features: Dependency Injection (DI).

Dependency Injection lets you create reusable, testable, and clean code by defining shared logic once and injecting it wherever needed—like checking headers, validating users, simulating databases, or reusing query parameters.

📘 What You’ll Learn
✅ What Dependency Injection is
✅ Why it's useful in building clean APIs
✅ How to use Depends and Annotated
✅ Real-world examples: login validation, shared queries, mock databases, sub-dependencies, and class-based dependencies


🔄 Sub-Dependencies

🏷️ Dependencies in Decorators

💡 Why Use Dependency Injection?
🔁 Code Reusability: Define logic once and use it everywhere

✂️ Separation of Concerns: Keep your endpoints clean and focused

🧪 Easy Testing: Replace real logic with mocks during tests

🧹 Organized Code: Centralize logic for cleaner project structure

🛠️ Setup Instructions
If continuing from Step 3, use your existing project. Or, start fresh:

bash
Copy
Edit
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate
uv add "fastapi[standard]"
Create a file called main.py and follow along!

🧪 Examples
1️⃣ Basic Dependency
Inject a simple dictionary with a message:

python
Copy
Edit
from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}

@app.get("/get-simple-goal")
def simple_goal(response: Annotated[dict, Depends(get_simple_goal)]):
    return response
2️⃣ Dependency with Parameters
Inject a username into the response dynamically:

python
Copy
Edit
def get_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "username": username}

@app.get("/get-goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    return response
3️⃣ Login Check with Query Parameters
Inject logic that checks credentials passed via query parameters:

python
Copy
Edit
from fastapi import Query

def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    return {"message": "Login Failed"}

@app.get("/signin")
def login_api(user: Annotated[dict, Depends(dep_login)]):
    return user
4️⃣ Multiple Dependencies in a Single Endpoint
Combine multiple dependency functions to build up your logic:

python
Copy
Edit
def depfunc1(num: int):
    return int(num) + 1

def depfunc2(num: int):
    return int(num) + 2

@app.get("/main/{num}")
def get_main(
    num: int,
    num1: Annotated[int, Depends(depfunc1)],
    num2: Annotated[int, Depends(depfunc2)]
):
    total = num + num1 + num2
    return f"Pakistan {total}"
5️⃣ Class-Based Dependencies (Like Django’s get_object_or_404)
Inject class logic to simulate object retrieval and error handling:

python
Copy
Edit
from fastapi import HTTPException, status

blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

class GetObjectOr404():
    def __init__(self, model):
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj

blog_dependency = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name

user_dependency = GetObjectOr404(users)

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return user_name
👨‍💻 What You Just Mastered
✅ Injecting simple and parameterized dependencies
✅ Sharing logic across routes
✅ Securing endpoints with dependency logic
✅ Simulating databases using classes
✅ Clean, testable, and DRY FastAPI code

here is the blog link

"https://medium.com/@ruba.haroon143/dependency-injection-in-fastapi-your-apis-secret-superpower-c0f7d23f7b98"
