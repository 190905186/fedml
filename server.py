
import flwr as fl
import socket

ipaddr=socket.gethostbyname(socket.gethostname())
print("the server ipaddr is ", ipaddr)

# Start Flower server
fl.server.start_server(
        server_address='localhost:8080",
    config=fl.server.ServerConfig(num_rounds=3),
)                               
