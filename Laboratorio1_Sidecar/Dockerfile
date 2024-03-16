# Utiliza la imagen oficial de Python
FROM python:3.9-slim

# Copia los archivos de código al contenedor
COPY EventLoggerSidecar.py /app/EventLoggerSidecar.py
COPY Sidecar.py /app/Sidecar.py
RUN pip install flask

# Establece el directorio de trabajo
WORKDIR /app

# Exponer el puerto 5000
EXPOSE 5000

# Ejecuta el script al iniciar el contenedor
CMD ["python", "Sidecar.py"]
