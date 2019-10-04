import socket, sys, time
import json

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
jsonPayload = json.dumps(x)

# the result is a JSON string:
print(jsonPayload)

for i in range(10):
	s.sendto(jsonPayload.encode('UTF-8'), server_address)
	x['age'] += 1
	jsonPayload = json.dumps(x)
quit()