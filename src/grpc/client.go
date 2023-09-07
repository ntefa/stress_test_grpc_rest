package grpc

import (
	"context"
	"fmt"
	"log"
	"time"

	pb "github.com/ntefa/stress_test_grpc_rest/src/proto/helloworld"

	"google.golang.org/grpc"
)

func RunGRPCClient() {
	serverAddress := "localhost:50051"

	// Set up a connection to the server.
	conn, err := grpc.Dial(serverAddress, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	// Create a gRPC client.
	client := pb.NewGreeterClient(conn)

	// Contact the server and print out its response.
	name := "World"
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	response, err := client.SayHello(ctx, &pb.HelloRequest{Name: name})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	fmt.Printf("Response from gRPC server: %s\n", response.Message)
}
