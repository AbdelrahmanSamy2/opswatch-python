servers = ["web-01", "api-01", "db-01"]

server = {
    "name": "web-01",
    "ip": "10.0.0.10",
    "cpu": 65,
    "memory": 40
}

servers.extend("worker-01", "cache-01")

servers.insert("gateway-01", 1)