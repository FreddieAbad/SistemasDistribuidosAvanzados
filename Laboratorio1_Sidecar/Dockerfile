# Utiliza la imagen oficial de Python
FROM python:3.9-slim

# Copia los archivos de código al contenedor
COPY EventLoggerSidecar.py /app/EventLoggerSidecar.py
COPY Sidecar.py /app/Sidecar.py

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias necesarias (si las hay)
RUN pip install threading

# Ejecuta el script al iniciar el contenedor
CMD ["python", "Sidecar.py"]
