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
