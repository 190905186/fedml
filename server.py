
import flwr as fl


# Start Flower server
fl.server.start_server(
        server_address="172.16.58.37:8080",
    config=fl.server.ServerConfig(num_rounds=3),
)                               
