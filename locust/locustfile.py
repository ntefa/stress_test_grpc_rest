from locust import HttpUser, TaskSet, task
import grpc
import hello_pb2_grpc
import hello_pb2
from interceptor import GrpcUser # Import grpc_user module if not already imported

# gRPC TaskSet
# class GRPCTest(TaskSet):
#     def on_start(self):
#         # Initialize a gRPC client
#         self.channel = grpc.insecure_channel("localhost:50051")
#         self.stub = hello_pb2_grpc.GreeterStub(self.channel)

#     @task
#     def test_grpc_hello(self):
#         response = self.stub.SayHello(hello_pb2.HelloRequest(name="Locust"))
#         print("gRPC response:", response.message)

# REST API TaskSet
class APITest(TaskSet):
    @task
    def test_rest_hello(self):
        response = self.client.get("/api/hello")
        print("REST API response:", response.text)

# Main User class
class MyUser(HttpUser):
    host = "http://localhost:8080"
    tasks = {APITest: 1}  # Weighted tasks, gRPC tasks have weight 1, REST API tasks have weight 2
    min_wait = 1000
    max_wait = 5000

# class HelloGrpcUser(GrpcUser):
#     host = "http://localhost:50051"
#     stub_class = hello_pb2_grpc.GreeterStub

#     tasks = {GRPCTest: 1}

class HelloGrpcUser(GrpcUser):
    host = "localhost:50051"
    stub_class = hello_pb2_grpc.GreeterStub

    @task
    def sayHello(self):
        # self.stub = hello_pb2_grpc.GreeterStub(self.host)
        response = self.stub.SayHello(hello_pb2.HelloRequest(name="Locust"))
        print("gRPC response:", response.message)
