from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


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

	title: str
	max_score: Optional[int]
	min_score: Optional[int]
	description: str
	estimated_time: Optional[str]
	preview_file_id: str
	created_by_user_id: str

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

	title: Optional[str]
	max_score: Optional[int]
	min_score: Optional[int]
	description: Optional[str]
	estimated_time: Optional[str]

class UpdateCourseResponseSchema(BaseModel):
	"""
	Описание структуры ответа на обновление курса.
	"""
	course: CourseSchema

