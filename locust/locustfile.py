from locust import HttpUser, TaskSet, task
import grpc
import your_generated_code  # Import the generated gRPC code
import requests

# gRPC TaskSet
class GRPCTest(TaskSet):
    def on_start(self):
        # Initialize a gRPC client
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = your_generated_code.GreeterStub(self.channel)

    @task
    def test_grpc_hello(self):
        response = self.stub.SayHello(your_generated_code.HelloRequest(name="Locust"))
        print("gRPC response:", response.message)

# REST API TaskSet
class APITest(TaskSet):
    @task
    def test_rest_hello(self):
        response = self.client.get("/api/hello")
        print("REST API response:", response.text)

# Main User class
class MyUser(HttpUser):
    tasks = {GRPCTest: 1, APITest: 2}  # Weighted tasks, gRPC tasks have weight 1, REST API tasks have weight 2
    min_wait = 1000
    max_wait = 5000
