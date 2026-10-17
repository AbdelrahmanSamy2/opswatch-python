# OPSWATCH Python Project - Monitors server CPU and memory usage and displays average utilization.
def main():
    # Initialize the fleet list
    fleet = []
    fleet_summary={
        "HEALTHY": 0,
        "WARNING": 0,
        "CRITICAL": 0
    }
    # Get the number of Servers
    while True:
        number_servers = int(input("Number of servers: "))
        if number_servers > 0:
            break
    # Take the inputs about each server and store them into a list of dictionaries.
    for server_number in range(number_servers):
        print(f"\n--- Server {server_number + 1} Input ---")
        server_name, server_ip, cpu_usage, memory_usage = get_server_info()
        average_usage = calculate_average_usage(cpu_usage, memory_usage)
        cpu_status = determine_health_status(cpu_usage)
        memory_status = determine_health_status(memory_usage)
        overall_status = determine_overall_health_status(cpu_status, memory_status)
        fleet.append({
            "number": server_number,
            "name": server_name,
            "ip": server_ip,
            "cpu": cpu_usage,
            "memory": memory_usage,
            "average": average_usage,
            "cpu_status": cpu_status,
            "memory_status": memory_status,
            "overall_status": overall_status
        })
    # Analyze fleet of servers and store into fleet_summary
    for server in fleet:
        fleet_summary[server["overall_status"]] += 1

    print(f"""
==============================
{'SERVER REPORTS':^30}
============================== """)
    for server in fleet:
        display_server(server)

    print(f"""
==============================
{'FLEET SUMMARY':^30}
============================== 
Total Servers: {len(fleet)}
HEALTHY:       {fleet_summary["HEALTHY"]}
WARNING:       {fleet_summary["WARNING"]}
CRITICAL:      {fleet_summary["CRITICAL"]}

""")



# Retrieves server information from user input.
def get_server_info():
    server_name = input("Server name: ")
    server_ip = input("IP address: ")
    cpu_usage = float(input("CPU usage (%): "))
    memory_usage = float(input("Memory usage (%): "))
    return server_name, server_ip, cpu_usage, memory_usage


# Calculates the average CPU and memory usage.
def calculate_average_usage(cpu, memory):
    return (cpu + memory) / 2


# Determine the health status
def determine_health_status(usage):
    if usage >= 80:
        return "CRITICAL"
    elif usage >= 60:
        return "WARNING"
    else:
        return "HEALTHY"


# Determine the overall health status
def determine_overall_health_status(cpu_status, memory_status):
    if cpu_status == "CRITICAL" or memory_status == "CRITICAL":
        return "CRITICAL"
    elif cpu_status == "WARNING" or memory_status == "WARNING":
        return "WARNING"
    else:
        return "HEALTHY"


# Displays server information and average utilization.
def display_server(server):
    align_width = 21
    print(f"""
--- Server {server["number"] + 1} ---
{'Server: ':<{align_width}} {server["name"]}
{'IP Address: ':<{align_width}} {server["ip"]}
{'CPU Usage: ':<{align_width}} {server["cpu"]:.2f}%
{'CPU Status: ':<{align_width}} {server["cpu_status"]}
{'Memory Usage: ':<{align_width}} {server["memory"]:.2f}%
{'Memory Status: ':<{align_width}} {server["memory_status"]}
{'Average Utilization: ':<{align_width}} {server["average"]:.2f}%
{'Overall Status: ':<{align_width}} {server["overall_status"]}
    """)


main()

