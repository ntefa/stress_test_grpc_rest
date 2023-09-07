package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/ntefa/stress_test_grpc_rest/src/grpc"
	"github.com/ntefa/stress_test_grpc_rest/src/rest"

	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/api/hello", rest.HelloHandler).Methods("GET")

	http.Handle("/", r)

	fmt.Println("REST API Server is running on port 8080...")
	go func() {
		log.Fatal(http.ListenAndServe(":8080", nil))
	}()

	grpc.StartGRPCServer()
}
