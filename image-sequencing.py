import pyautogui
import time

updowntime = 1.39
leftrighttime = 2.18

right_count_max = 3
down_count_max = 3

right_counter = down_counter = 0

def move_right(t):
    pyautogui.keyDown('right')
    time.sleep(t)  # Hold for t seconds
    pyautogui.keyUp('right')
    print("Right key pressed and released")

def move_left(t):
    pyautogui.keyDown('left')
    time.sleep(t)  # Hold for t seconds
    pyautogui.keyUp('left')
    print("Left key pressed and released")

def move_down(t):
    pyautogui.keyDown('down')
    time.sleep(t)  # Hold for t seconds
    pyautogui.keyUp('down')
    print("Down key pressed and released")

def move_up(t):
    pyautogui.keyDown('up')
    time.sleep(t)  # Hold for t seconds
    pyautogui.keyUp('up')
    print("Up key pressed and released")

def save_image(image_serial_no):
    # save button at top
    pyautogui.moveTo(570, 90)
    pyautogui.click(570, 90)
    print("Clicked at coordinates (570, 90)")
    pyautogui.sleep(1)
    # pyautogui.mouseclick()
    pyautogui.press('backspace')

    pyautogui.typewrite('xyz', interval=0.5)
    pyautogui.sleep(0.5)
    pyautogui.typewrite(str(image_serial_no))
    time.sleep(1)
    # pyautogui.press('enter')

    # Wait for the application to open
    # time.sleep()

    # Click on coordinates (1061, 586)
    pyautogui.moveTo(1061, 532)
    pyautogui.click(1061, 532)
    print("Clicked at coordinates (1061, 532)")
    pyautogui.sleep(5)

# ------------------------------------------------------------------------------------------------------------------------------------
# automation starts here

time.sleep(0.5)
pyautogui.hotkey('enter')
print("Pressed 'enter'")
# Press command+tab to switch to the next application
pyautogui.hotkey('command', 'tab')
print("Pressed 'command+tab'")

# First, ensure the system is responsive
time.sleep(1)

# Loop for moving right and capturing images
for i in range(right_count_max):
    save_image(i + 1)
    pyautogui.click(1000,600)
    move_right(leftrighttime)
