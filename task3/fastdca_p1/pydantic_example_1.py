from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  

# Valid data
user_data = {"id": 1, "name": "Ruba", "email": "ruba2@gmail.com", "age": 25}
user = User(**user_data)
print(user)  
print(user.model_dump())  

# Invalid data (will raise an error)
try:
    invalid_user = User(id="not_an_int", name="Bob", email="bob@gmail.com")
except ValidationError as e:
    print(e)