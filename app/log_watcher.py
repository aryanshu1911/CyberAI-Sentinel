import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from app.log_analyzer import analyze_logs
from app.auto_response import block_ip
from app.alerts import send_alert

LOG_FILE = "sample.log"

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(LOG_FILE):
            threats = analyze_logs(LOG_FILE)
            if threats:
                for threat in threats:
                    ip = threat["ip"]
                    status = threat["status"]
                    message = f"⚠️ {status.upper()} detected for IP: {ip}"
                    print(message)
                    
                    # Send alert
                    send_alert(message)
                    
                    # Auto-block IP
                    block_ip(ip)

def start_watcher():
    event_handler = LogHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    print("🔍 Watching log file in real-time with auto-response...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()