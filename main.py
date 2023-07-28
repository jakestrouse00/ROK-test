import pygetwindow as gw
import pyautogui
from typing import *
import psutil
from pywinauto import Application


def all_system_titles() -> List[str]:
    # Get a list of all the titles of currently open windows
    all_window_titles = gw.getAllTitles()

    # Print the titles of all open windows
    return all_window_titles


def get_app_pid():
    for process in psutil.process_iter(['pid', 'name']):
        if process.name() == "MASS.exe":
            return int(process.pid)
    return None


def take_screenshot_of_app(app_title):
    try:
        # Search for the application window by its title
        app_window = gw.getWindowsWithTitle(app_title)[0]
        # screen_width, screen_height = pyautogui.size()
        # print(screen_width, screen_height)
        # # Set the application window to cover the entire screen
        # app_window.moveTo(0, 0)
        # app_window.resizeTo(screen_width, screen_height)
        # Get the position and size of the application window
        x, y, width, height = app_window.left, app_window.top, app_window.width, app_window.height

        # Take a screenshot of the application window
        screenshot = pyautogui.screenshot(region=(x, y, width, height))

        # Save the screenshot to a file
        screenshot.save(f'{app_title}_screenshot.png')
        print(f'Screenshot of {app_title} saved successfully!')
    except IndexError:
        print(f'Application with title "{app_title}" not found.')


if __name__ == '__main__':

    try:
        app_title = "Rise of Kingdoms"
        if app_title in all_system_titles():
            pid = get_app_pid()
            print(pid)
            app = Application().connect(process=12856)
            print(app.process)
            # app = Application(backend="uia").connect(process=pid)
            # print(app.process)

            # app = Application(backend="uia").connect(process=12856)
            # print(app.process)


            # app.top_window().set_focus()
            # Replace 'Your App Title' with the actual title of the application you want to capture
            take_screenshot_of_app(app_title)
    except Exception as e:
        print(e)

    input("hold")
