import pyautogui
import time
import pygetwindow as gw


updowntime = 1
leftrighttime = 1.4

right_count_max = 3
down_count_max = 2

right_counter = down_counter = 0

download_interval = 10

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

def save_image(image_serial_no, name):
    # save button at top
    pyautogui.moveTo(570, 90)
    pyautogui.click(570, 90)
    print("Clicked at coordinates (570, 90)")
    pyautogui.sleep(1)
    # pyautogui.mouseclick()
    pyautogui.press('backspace')

    # pyautogui.press('W')
    # pyautogui.press('a')
    # pyautogui.press('t')
    # pyautogui.press('e')
    # pyautogui.press('r')
    # pyautogui.press('_')
    # pyautogui.press('b')
    # pyautogui.press('o')
    # pyautogui.press('d')
    # pyautogui.press('y')
    # pyautogui.press('_')
    
    pyautogui.typewrite(name, interval=0.5)
    pyautogui.sleep(0.5)
    pyautogui.typewrite(str(image_serial_no))
    time.sleep(1)
    # pyautogui.press('enter')

    # Wait for the application to open
    # time.sleep()

    # Click on coordinates (1061, 586)
    pyautogui.moveTo(882, 360)
    pyautogui.click(882, 360)
    print("Clicked at coordinates (882, 360)")
    pyautogui.sleep(download_interval)

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

for j in range(down_count_max):
    # Loop for moving right and capturing images
    for i in range(right_count_max):
        if i != 0:
            move_right(leftrighttime)
        save_image(right_count_max * j + i + 1, "dakka_")
        print("Image", i + 1, "captured")

    # move left n times
    for i in range(right_count_max-1):
        move_left(leftrighttime)

    # move down once
    move_down(updowntime)
    print("Moved down once")

pyautogui.hotkey('command', 'tab')