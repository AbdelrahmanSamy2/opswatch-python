# OPSWATCH Python Project - Monitors server CPU and memory usage and displays average utilization.
def main():
    # Get the number of Servers
    while True:
        number_servers = int(input("Number of servers: "))
        if number_servers > 0:
            break
    
    for server_number in range(number_servers):
        print(f"--- Server {server_number + 1} Input ---")
        server_name, server_ip, cpu_usage, memory_usage = get_server_info()
        average_usage = calculate_average_usage(cpu_usage, memory_usage)
        cpu_status = determine_health_status(cpu_usage)
        memory_status = determine_health_status(memory_usage)
        overall_status = determine_overall_health_status(cpu_status, memory_status)
        display_server(server_number, server_name, server_ip, cpu_usage, memory_usage, average_usage, cpu_status, memory_status, overall_status)


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
def display_server(number, name, ip, cpu_usage, memory_usage, average, cpu_status, memory_status, overall_status):
    align_width = 21
    print(f"""
    --- Server {number + 1} Report ---
    {'Server: ':<{align_width}} {name}
    {'IP Address: ':<{align_width}} {ip}

    {'CPU Usage: ':<{align_width}} {cpu_usage:.2f}%
    {'CPU Status: ':<{align_width}} {cpu_status}

    {'Memory Usage: ':<{align_width}} {memory_usage:.2f}%
    {'Memory Status: ':<{align_width}} {memory_status}

    {'Average Utilization: ':<{align_width}} {average:.2f}%
    {'Overall Status: ':<{align_width}} {overall_status}
    """)


main()

