from concurrent import futures

import grpc

import course_service_pb2 as pb2
import course_service_pb2_grpc as pb2_grpc


class CourseServiceServicer(pb2_grpc.CourseServiceServicer):
	def GetCourse(self, request, context):
		print(f'Получим запрос к методу GetCourse: {request}')
		return pb2.GetCourseResponse(
			course_id=f'{request.course_id}',
			title=f'Автотесты API',
			description=f'Будем изучать написание API автотестов'
		)


def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
	server.add_insecure_port('[::]:50051')
	server.start()
	print("gRPC server started at 50051 ...")
	server.wait_for_termination()


if __name__ == '__main__':
	serve()
