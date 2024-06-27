import pyautogui
import time

print("2s sleep -> cmd+tab")

time.sleep(2)
pyautogui.hotkey('enter')
# Press command+tab to switch to the next application
pyautogui.hotkey('command', 'tab')

# Wait for the switcher to appear
time.sleep(1)

# Move mouse to coordinates (570, 90)
pyautogui.click(570, 90)
pyautogui.sleep(1)
# pyautogui.mouseclick()

# Press command+tab again to select the desired application (assuming Water_body_1 is an application)
pyautogui.typewrite('vanga')
time.sleep(1)
# pyautogui.press('enter')

# Wait for the application to open
# time.sleep()

# Click on coordinates (1061, 586)
pyautogui.click(882, 360)
pyautogui.sleep(5)

# Press command+tab to switch back to the previous application
pyautogui.hotkey('command', 'tab')

# Wait for the switcher to appear
time.sleep(1)

# Press ctrl+c to copy
# pyautogui.hotkey('control', 'c')
