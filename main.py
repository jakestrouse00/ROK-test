# import pyautogui
#
# # Get the size of the screen
# screen_width, screen_height = pyautogui.size()
#
# # Get the current position of the active application's window
# x, y, width, height = pyautogui.getActiveWindow()
#
# # Ensure the window is within the screen boundaries
# x = max(x, 0)
# y = max(y, 0)
# width = min(width, screen_width - x)
# height = min(height, screen_height - y)
#
# # Take a screenshot of the active application's window
# screenshot = pyautogui.screenshot(region=(x, y, width, height))
#
# # Save the screenshot to a file
# screenshot.save('screenshot.png')

import pygetwindow as gw

# Get a list of all the titles of currently open windows
all_window_titles = gw.getAllTitles()

# Print the titles of all open windows
for title in all_window_titles:
    print(title)

input("\nhold")
