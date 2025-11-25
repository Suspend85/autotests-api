from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
	"""
	Описание структуры курса.
	"""
	model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

	id: str
	title: str
	max_score: Optional[int]
	min_score: Optional[int]
	description: str
	preview_file: FileSchema
	estimated_time: Optional[str]
	created_by_user: UserSchema


class GetCoursesRequestSchema(BaseModel):
	"""
	Описание структуры запроса на получение списка курсов.
	"""
	user_id : str = Field(alias='userId')


class CreateCourseRequestSchema(BaseModel):
	"""
	Описание структуры запроса на создание курса.
	"""
	model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

	title: str = Field(default_factory=fake.sentence)
	max_score: Optional[int] = Field(default_factory=fake.max_score)
	min_score: Optional[int] = Field(default_factory=fake.min_score)
	description: str = Field(default_factory=fake.text)
	estimated_time: Optional[str] = Field(default_factory=fake.estimated_time)
	preview_file_id: str = Field(default_factory=fake.uuid4) #  случайные данные тут подходят только для негативных кейсов
	created_by_user_id: str = Field(default_factory=fake.uuid4) #  случайные данные тут подходят только для негативных кейсов

class CreateCourseResponseSchema(BaseModel):
	"""
	Описание структуры ответа на создание курса.
	"""
	course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
	"""
	Описание структуры запроса на обновление курса.
	"""
	model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

	title: Optional[str] = Field(default_factory=fake.sentence)
	max_score: Optional[int] = Field(default_factory=fake.max_score)
	min_score: Optional[int] = Field(default_factory=fake.min_score)
	description: Optional[str] = Field(default_factory=fake.text)
	estimated_time: Optional[str] = Field(default_factory=fake.estimated_time)

class UpdateCourseResponseSchema(BaseModel):
	"""
	Описание структуры ответа на обновление курса.
	"""
	course: CourseSchema

