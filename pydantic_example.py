from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")


class ShortUserSchema(BaseModel):
    id: str = "123"
    email: str = "fbg@sdf.rt"

class FullUserSchema(ShortUserSchema):
    last_name: str
    first_name: str
    middle_name: str

u = FullUserSchema(last_name="Jonson", first_name="John", middle_name="jo")
print(u)


user_data ={
    "id": 1,
    "name": "Alice",
    "email": "Alice@examlpe.com",
    "isActive": True,
}
user = User(**user_data)
print(user.model_dump())


