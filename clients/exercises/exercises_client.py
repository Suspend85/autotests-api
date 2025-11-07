from idlelib import query
from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
	courseId: str

class CreateExerciseRequestDict(TypedDict):
	"""
	Описание структуры запроса на создание задания.
	"""
	title: str
	courseId: str
	maxScore: str
	minScore: str
	orderIndex: str | None
	description: str
	estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
	"""
	Описание структуры запроса на обновление задания.
	"""
	title: str | None
	maxScore: str | None
	minScore: str | None
	orderIndex: str | None
	description: str | None
	estimatedTime: str | None


class ExercisesClient(APIClient):
	def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
		"""
		Метод получения списка заданий по CourseId.

		:param query: Словарь с courseId.
		:return: Ответ от сервера в виде объекта httpx.Response
		"""
		return self.get('/api/v1/exercises', params=query)

	def get_exercise_api(self, exercise_id: str) -> Response:
		"""
		Метод получения информации о задании по exercise_id.

		:param exercise_id: идентификатор задания.
		:return: Ответ от сервера в виде объекта httpx.Response
		"""
		return self.get(f'/api/v1/exercises/{exercise_id}')

	def	create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
		"""
		Метод создания задания.

		:param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
		:return: Ответ от сервера в виде объекта httpx.Response
		"""
		return self.post(f'/api/v1/exercises/', json=request)

	def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict):
		"""
		Метод обновления задания.

		:param exercise_id: Идентификатор задания.
		:param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
		:return: Ответ от сервера в виде объекта httpx.Response
		"""
		return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

	def delete_exercise_api(self, exercise_id: str) -> Response:
		"""
		Метод удаления задания.

		:param exercise_id: Идентификатор задания.
		:return: Ответ от сервера в виде объекта httpx.Response
		"""
		return self.delete(f'/api/v1/exercises/{exercise_id}')

