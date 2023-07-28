import psutil


def get_app_pid():
    for process in psutil.process_iter(['pid', 'name']):
        if process.name() == "MASS.exe":
            return process.pid
    return None


# Replace 'YourAppName.exe' with the actual name of the application (e.g., 'notepad.exe')

