import pyautogui

# Get the current mouse cursor position
current_pos = pyautogui.position()

print("Move your mouse cursor to the desired location...")
print("Press Ctrl+C to exit and print the coordinates.")
prev_cur_pos = pyautogui.position()
try:
    while True:
        # Continuously print the current mouse cursor position
        current_pos = pyautogui.position()
        if(prev_cur_pos != current_pos):
            print("Current mouse position:", current_pos)
            prev_cur_pos = current_pos

except KeyboardInterrupt:
    # Exit gracefully when Ctrl+C is pressed
    pass
