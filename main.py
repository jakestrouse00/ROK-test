import pygetwindow as gw
import pyautogui
from typing import *


def all_system_titles() -> List[str]:
    # Get a list of all the titles of currently open windows
    all_window_titles = gw.getAllTitles()

    # Print the titles of all open windows
    return all_window_titles


def take_screenshot_of_app(app_title):
    try:
        # Search for the application window by its title
        app_window = gw.getWindowsWithTitle(app_title)[0]

        # Get the position and size of the application window
        x, y, width, height = app_window.left, app_window.top, app_window.width, app_window.height

        # Take a screenshot of the application window
        screenshot = pyautogui.screenshot(region=(x, y, width, height))

        # Save the screenshot to a file
        screenshot.save(f'{app_title}_screenshot.png')
        print(f'Screenshot of {app_title} saved successfully!')
    except IndexError:
        print(f'Application with title "{app_title}" not found.')


app_title = "Rise of Kingdoms"
if app_title in all_system_titles():
    # Replace 'Your App Title' with the actual title of the application you want to capture
    take_screenshot_of_app(app_title)



input("hold")