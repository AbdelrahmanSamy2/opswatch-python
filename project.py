# OPSWATCH Python Project - Monitors server CPU and memory usage and displays average utilization.
def main():
    server_name, server_ip, cpu_usage, memory_usage = get_server_info()
    average_usage = calculate_average_usage(cpu_usage, memory_usage)
    display_server(server_name, server_ip, cpu_usage, memory_usage, average_usage)


# Retrieves server information from user input.
def get_server_info():
    server_name = input("Server name: ")
    server_ip = input("IP address: ")
    cpu_usage = float(input("CPU usage (%): "))
    memory_usage = float(input("Memory usage (%): "))
    return server_name, server_ip, cpu_usage, memory_usage


# Calculates the average CPU and memory usage.
def calculate_average_usage(cpu, memory):
    return f"{(cpu + memory) / 2:.2f}"

# Displays server information and average utilization.
def display_server(name, ip, cpu, memory, average):
    align_width = 21
    print("--------------------------------")
    print("         OPSWATCH")
    print("--------------------------------")
    print(f"{'Server: ':<{align_width}} {name}")
    print(f"{'IP Address: ':<{align_width}} {ip}")
    print(f"{'CPU Usage: ':<{align_width}} {cpu}%")
    print(f"{'Memory Usage: ':<{align_width}} {memory}%")
    print(f"{'Average Utilization: ':<{align_width}} {average}%")
    print("--------------------------------")


main()

