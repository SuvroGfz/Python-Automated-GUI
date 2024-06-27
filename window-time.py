from AppKit import NSWorkspace
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
import time
from datetime import datetime

def get_active_window_info():
    options = kCGWindowListOptionOnScreenOnly
    window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    for window in window_list:
        if window['kCGWindowLayer'] == 0:
            window_id = window['kCGWindowNumber']
            app_name = window['kCGWindowOwnerName']
            window_name = window.get('kCGWindowName', 'Unknown')
            return window_id, app_name, window_name
    return None, None, None

active_window = None
start_time = None

# Open the log file in append mode
with open("active_window_log.txt", "a") as log_file:
    # Log the start time
    log_file.write(f"\nProgram started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    try:
        while True:
            window_id, app_name, window_name = get_active_window_info()
            if app_name and window_name:
                current_window = (window_id, app_name, window_name)
                if current_window != active_window:
                    if active_window is not None:
                        end_time = time.time()
                        active_time = end_time - start_time
                        log_file.write(f"Window ID '{active_window[0]}', '{active_window[2]}' from application '{active_window[1]}' was active for {active_time:.2f} seconds.\n")
                    active_window = current_window
                    start_time = time.time()
                    log_file.write(f"Switched to window ID '{window_id}', '{window_name}' from application '{app_name}'\n")
            else:
                log_file.write("No active window found\n")
            
            time.sleep(1)  # Check every second
    except KeyboardInterrupt:
        if active_window is not None:
            end_time = time.time()
            active_time = end_time - start_time
            log_file.write(f"Window ID '{active_window[0]}', '{active_window[2]}' from application '{active_window[1]}' was active for {active_time:.2f} seconds.\n")
        # Log the end time
        log_file.write(f"Program ended at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write("Stopped.\n")
