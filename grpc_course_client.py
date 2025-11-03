import grpc

import course_service_pb2 as pb2
import course_service_pb2_grpc as pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = pb2_grpc.CourseServiceStub(channel)

response = stub.GetCourse(pb2.GetCourseRequest(course_id="api-course"))
print(response)
