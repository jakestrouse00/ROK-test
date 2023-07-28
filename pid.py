import psutil


def get_app_pid_by_name(app_name):
    for process in psutil.process_iter(['pid', 'name']):
        print(process)
        if process.name().lower().startswith("r"):
            print(process)
    return None


# Replace 'YourAppName.exe' with the actual name of the application (e.g., 'notepad.exe')
app_name_to_find = 'Rise of Kingdoms.exe'
app_pid = get_app_pid_by_name(app_name_to_find)

if app_pid:
    print(f"PID of {app_name_to_find}: {app_pid}")
else:
    print(f"Application '{app_name_to_find}' is not running.")

input("d")
