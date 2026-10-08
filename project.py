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
    return (cpu + memory) / 2


# Displays server information and average utilization.
def display_server(name, ip, cpu, memory, average):
    print("--------------------------------")
    print("         OPSWATCH")
    print("--------------------------------")
    print(f"Server: {name:>14}")
    print(f"IP Address: {ip:>10}")
    print(f"CPU Usage: {cpu:>13}%")
    print(f"Memory Usage: {memory:>10}%")
    print(f"Average Utilization: {average}%")
    print("--------------------------------")


main()

