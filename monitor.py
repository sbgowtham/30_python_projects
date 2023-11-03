import psutil

# Get a list of all running processes
running_processes = psutil.process_iter(attrs=['pid', 'name', 'status'])

# Iterate through the list and print process information
for process in running_processes:
    process_info = process.info
    pid = process_info['pid']
    name = process_info['name']
    status = process_info['status']
    print(f"PID: {pid}, Name: {name}, Status: {status}")

