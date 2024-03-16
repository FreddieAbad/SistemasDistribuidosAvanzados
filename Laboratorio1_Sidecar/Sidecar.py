from flask import Flask
from EventLoggerSidecar import EventLoggerSidecar
import threading
import time

app = Flask(__name__)

class Main:
    def __init__(self):
        self.sidecar = EventLoggerSidecar()

    def process_message(self, message):
        print(f"Processing message: {message}")
        self.sidecar.log_event(f"Message processed: {message}")

main_instance = Main()

@app.route('/')
def home():
    main_instance.process_message("Mensaje de prueba")
    return 'Mensaje procesado y registrado en el log.'

if __name__ == '__main__':
    # Crear una instancia de EventLoggerSidecar
    sidecar = EventLoggerSidecar()

    # Crear un hilo para ejecutar print_log_every_30_seconds
    log_thread = threading.Thread(target=sidecar.print_log_every_30_seconds)
    log_thread.daemon = True
    log_thread.start()

    app.run(debug=True)
