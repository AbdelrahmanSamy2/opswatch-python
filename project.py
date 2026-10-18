# OPSWATCH Python Project - Monitors server CPU and memory usage and displays average utilization.
def main():
    # Take the inputs about each server and store them into a list of dictionaries.
    fleet = store_fleet_data(get_number_servers())
    # Optional: Remove Servers
    optional_remove_server(fleet)
    # Display Servers Report
    display_servers(fleet)
    # Display Fleet Analysis Summary
    display_fleet_summary(analyze_fleet(fleet))
    display_attention_servers(get_attention_servers(fleet))
    display_utilization_map(fleet)


# Optional: Remove Servers from the Fleet
def optional_remove_server(fleet):
    if len(fleet) == 1:
        print("Cannot remove the only server in the fleet.")
        return
    do_you_want_to_remove = ask_to_remove()
    while do_you_want_to_remove == 'y':
        remove_server(fleet)
        if len(fleet) == 1:
            return
        do_you_want_to_remove = ask_to_remove()


# Remove a server from the fleet based on user input.
def remove_server(fleet):
    server_name = normalize_name(input("Server name: "))
    found = False
    for server in fleet:
        if server["name"] == server_name:
            found = True
            fleet.remove(server)
            break
    if not found:
        print("Server not found.")


# Ask the user if they want to remove a server from monitoring.
def ask_to_remove():
    while True:
        do_you_want_to_remove = input("Remove a server from monitoring? (y/n): ")
        if do_you_want_to_remove == 'y' or do_you_want_to_remove == 'n':
            break
    return do_you_want_to_remove


# Get the number of Servers (Keep asking until getting a positive number of servers)
def get_number_servers():
    while True:
        number_servers = int(input("Number of servers: "))
        if number_servers > 0:
            break
    return number_servers


# Take the inputs about each server and store them into a list of dictionaries.
def store_fleet_data(number_servers):
    fleet = []
    for server_number in range(number_servers):
        print(f"\n--- Server {server_number + 1} Input ---")
        server_name, server_ip, cpu_usage, memory_usage = get_server_info()
        normalized_name = normalize_name(server_name)
        short_id = make_short_id(normalized_name)
        average_usage = calculate_average_usage(cpu_usage, memory_usage)
        cpu_status = determine_health_status(cpu_usage)
        memory_status = determine_health_status(memory_usage)
        overall_status = determine_overall_health_status(cpu_status, memory_status)
        fleet.append({
            "number": server_number,
            "name": normalized_name,
            "short_id": short_id,
            "ip": server_ip,
            "cpu": cpu_usage,
            "memory": memory_usage,
            "average": average_usage,
            "cpu_status": cpu_status,
            "memory_status": memory_status,
            "overall_status": overall_status
        })
    return fleet


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
def display_servers(fleet):
    print(
    f"""
    ==============================
    {'SERVER REPORTS':^30}
    ============================== """)
    for server in fleet:
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
    {'Overall Status: ':<{align_width}} {server["overall_status"]}""")


# Function that analyzes the fleet and return fleet_summary dictionary
def analyze_fleet(fleet):
    # Analyze fleet of servers and store into fleet_summary
    fleet_summary={
        "HEALTHY": 0,
        "WARNING": 0,
        "CRITICAL": 0
    }
    total_cpu = 0
    total_memory = 0
    for server in fleet:
        fleet_summary[server["overall_status"]] += 1
        total_cpu += server["cpu"]
        total_memory += server["memory"]
    fleet_summary["cpu_average"] = total_cpu / len(fleet)
    fleet_summary["memory_average"] = total_memory / len(fleet)
    fleet_summary["total_servers"] = len(fleet)
    return fleet_summary


# Display fleet_summary report
def display_fleet_summary(fleet_summary):
    print(f"""
    ==============================
    {'FLEET SUMMARY':^30}
    ============================== 
    Total Servers:          {fleet_summary["total_servers"]}
    HEALTHY:                {fleet_summary["HEALTHY"]}
    WARNING:                {fleet_summary["WARNING"]}
    CRITICAL:               {fleet_summary["CRITICAL"]}

    Average Fleet CPU:      {fleet_summary["cpu_average"]:.2f}%
    Average Fleet Memory:   {fleet_summary["memory_average"]:.2f}%""")


# Identify the Servers that needs attention (WARNING/CRITICAL)
def get_attention_servers(fleet):
    attention_servers = []
    for server in fleet:
        if server["overall_status"] != "HEALTHY":
            attention_servers.append(server)
    return attention_servers


# Display the Attention Servers
def display_attention_servers(attention_servers):
    print(f""" 
    ==============================
         ATTENTION REQUIRED
    ==============================""")
    if not attention_servers:
        print("""
    No servers require attention
    """)
    else:
        for server in attention_servers:
            print(f"""
    ID:         {server["short_id"]}
    Server:     {server["name"]}
    CPU:        {server["cpu"]:.2f}% ({server["cpu_status"]})           
    Memory:     {server["memory"]:.2f}% ({server["memory_status"]})
    Overall:    {server["overall_status"]}""")


def normalize_name(server_name):
    return server_name.strip().lower()


def make_short_id(normalized_name):
    return normalized_name[:8]


def display_utilization_map(fleet):
    print(f"""==============================\n       UTILIZATION MAP\n==============================""")    
    for server in fleet:
        print(f"{server["name"]}")
        for resource_name, resource_utilization in server.items():
            if resource_name not in ["cpu", "memory"]:
                continue
            bar = ""
            bar_len = int(resource_utilization / 10)
            for point in range(1, 11):
                if point <= bar_len:
                    bar += "#"
                else:
                    bar += "-"
            print(f"{resource_name.upper()+":":<7} {bar} {resource_utilization:.2f}%")
        print()


main()