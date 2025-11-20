import uuid

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
	model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

	id: str = Field(default_factory=lambda: str(uuid.uuid4()))
	email: EmailStr = "john@wick.film"
	last_name: str = Field(alias="lastName", default="Wick")
	first_name: str = Field(alias="firstName", default="Jordanni")
	middle_name: str = Field(alias="middleName", default="Yovanovich")

class CreateUserRequestSchema(BaseModel):
	email: EmailStr = "john@wick.film"
	password: str = "123"
	last_name: str = Field(alias="lastName", default="Wick")
	first_name: str = Field(alias="firstName", default="Jordanni")
	middle_name: str = Field(alias="middleName", default="Yovanovich")

class CreateUserResponseSchema(BaseModel):
	user: UserSchema


user1 = UserSchema()
print(user1)

created_user_request = CreateUserRequestSchema()
print(created_user_request)
