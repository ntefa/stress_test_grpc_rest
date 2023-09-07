package grpc

import (
	"context"
	"fmt"
	"log"
	"net"

	pb "github.com/ntefa/stress_test_grpc_rest/src/proto/helloworld"

	"google.golang.org/grpc"
)

type server struct {
	pb.GreeterServer
}

func StartGRPCServer() {
	listen, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterGreeterServer(s, &server{})

	fmt.Println("gRPC Server is running on port 50051...")
	if err := s.Serve(listen); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}

func (s *server) SayHello(ctx context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
	return &pb.HelloReply{Message: "Hello, " + in.Name + "!"}, nil
}
