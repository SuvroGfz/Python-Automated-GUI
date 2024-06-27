from AppKit import NSWorkspace
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
import time
from datetime import datetime
import csv

def get_active_windows_info():
    options = kCGWindowListOptionOnScreenOnly
    window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
    windows_info = []
    
    for window in window_list:
        if window['kCGWindowLayer'] == 0:
            window_id = window['kCGWindowNumber']
            app_name = window['kCGWindowOwnerName']
            window_name = window.get('kCGWindowName', 'Unknown')
            windows_info.append((window_id, app_name, window_name))
    
    return windows_info

active_windows = {}
log_file_path = "window-lifetime.txt"
csv_file_path = "window-lifetime.csv"

# Open the log file in append mode
with open(log_file_path, "a") as log_file, open(csv_file_path, "a", newline='') as csv_file:
    # Log the start time of the program
    log_file.write(f"\nProgram started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # CSV writer setup
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([])
    csv_writer.writerow(["Window ID", "Application Name", "Window Name", "Start Time", "End Time", "Duration (seconds)"])
    
    try:
        while True:
            current_windows = get_active_windows_info()
            current_window_ids = {win[0] for win in current_windows}

            # Check for closed windows
            for window_id in list(active_windows.keys()):
                if window_id not in current_window_ids:
                    app_name, window_name, start_time = active_windows.pop(window_id)
                    end_time = time.time()
                    duration = end_time - start_time
                    end_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
                    if end_time_str == datetime.now().strftime('%Y-%m-%d %H:%M:%S'):
                        log_file.write(f"Window ID '{window_id}' was not closed.\n")
                    else:
                        log_file.write(f"Window ID '{window_id}' was closed at {end_time_str} after being active for {duration:.2f} seconds.\n")
                        csv_writer.writerow([window_id, app_name, window_name, datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S'), end_time_str, duration])
            
            # Check for new windows
            for window_id, app_name, window_name in current_windows:
                if window_id not in active_windows:
                    start_time = time.time()
                    active_windows[window_id] = (app_name, window_name, start_time)
                    log_file.write(f"Window ID '{window_id}', '{window_name}' from application '{app_name}' became active at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.\n")
            
            time.sleep(1)  # Check every second
    except KeyboardInterrupt:
        # Log the end time of the program
        end_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"Program ended at: {end_time_str}\n")
        
        # Check for any remaining active windows
        for window_id, (app_name, window_name, start_time) in active_windows.items():
            end_time = time.time()
            duration = end_time - start_time
            log_file.write(f"Window ID '{window_id}' was not closed.\n")
            csv_writer.writerow([window_id, app_name, window_name, datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S'), end_time_str, "not closed"])
        
        log_file.write("Stopped.\n")
