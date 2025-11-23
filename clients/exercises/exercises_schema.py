from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class ExerciseSchema(BaseModel):
	"""
	Описание структуры упражнения.
	"""
	model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

	id: str
	title: str
	courseId: str
	max_score: Optional[int]
	min_score: Optional[int]
	order_index: int = 0
	description: str
	estimated_time: Optional[str]


class GetExerciseResponseSchema(BaseModel):
	"""
	Описание структуры ответа на получение списка упраженений.
	"""
	exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
	"""
	Описание структуры запроса на получение списка упраженений.
	"""
	course_id: str = Field(alias='courseId')


class GetExercisesResponseSchema(BaseModel):
	"""
	Описание структуры ответа на получение списка упраженений.
	"""
	exercises: List[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
	"""
	Описание структуры запроса на создание упражнения.
	"""
	model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

	title: str
	course_id: str
	max_score: Optional[int]
	min_score: Optional[int]
	order_index: int
	description: str
	estimated_time: Optional[str]


class CreateExerciseResponseSchema(BaseModel):
	"""
	Описание структуры ответа создания упражнения.
	"""
	exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
	"""
	Описание структуры запроса на обновление упражнения.
	"""
	model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

	title: Optional[str]
	max_score: Optional[int]
	min_score: Optional[int]
	order_index: Optional[int]
	description: Optional[str]
	estimated_time: Optional[str]


class UpdateExerciseResponseSchema(BaseModel):
	"""
	Описание структуры ответа обновления упражнения.
	"""
	exercise: ExerciseSchema
