from AppKit import NSWorkspace
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
import psutil
import time

def get_active_window_name():
    options = kCGWindowListOptionOnScreenOnly
    window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    for window in window_list:
        if window['kCGWindowLayer'] == 0:
            app_name = window['kCGWindowOwnerName']
            window_name = window.get('kCGWindowName', 'Unknown')
            return app_name, window_name
    return None, None

while True:
    app_name, window_name = get_active_window_name()
    if app_name and window_name:
        print(f"Active window title: {window_name}")
        print(f"Application name: {app_name}")
    else:
        print("No active window found")
    
    time.sleep(1)  # Check every second
