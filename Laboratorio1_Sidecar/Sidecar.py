from event_logger import EventLoggerSidecar
import threading
import time

class Main:
    def __init__(self):
        self.sidecar = EventLoggerSidecar()

    def process_message(self, message):
        print(f"Processing message: {message}")
        self.sidecar.log_event(f"Message processed: {message}")

app = Main()

log_thread = threading.Thread(target=app.sidecar.print_log_every_30_seconds)
log_thread.daemon = True
log_thread.start()

app.process_message("Mensaje de prueba")

time.sleep(60)
