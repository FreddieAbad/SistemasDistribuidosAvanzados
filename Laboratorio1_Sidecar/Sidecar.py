import threading
import time

class EventLoggerSidecar:
    def __init__(self):
        self.log_file = "event_log.txt"
        self.log_buffer = []

    def log_event(self, event):
        self.log_buffer.append(event)

    def write_log_to_file(self):
        with open(self.log_file, "a") as file:
            for event in self.log_buffer:
                file.write(event + "\n")
        self.log_buffer.clear()

    def print_log_every_30_seconds(self):
        while True:
            time.sleep(30)
            self.write_log_to_file()
            print("Log printed.")

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
