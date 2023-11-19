# udp-pinger-client-server

# My Awesome Project

Welcome to my project! This project involves a simple client and server built with python.The client sends a simple ping message to the server, and receives a corresponding pong message back from the server. The delay between sending and receiving a ping is called the Round Trip Time (RTT), which this project aims to determine. The client sends 10 pings to the server over UDP, which is an unreliable protocol. So, while the RTT is being computed and the time exceeds 1s, we assume that the packet is lost, and will print the corresponding message.

## Usage

To run this project, follow these steps:

1. Clone this repository
2. Run the server file 
3. Run the client file

It is important that the server file will be running as the client file is executed. 

