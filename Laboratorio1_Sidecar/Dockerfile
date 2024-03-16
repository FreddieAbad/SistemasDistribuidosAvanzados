# Utiliza la imagen oficial de Python
FROM python:3.9-slim

# Copia el código fuente al contenedor
COPY main.py /app/main.py

# Instala las dependencias necesarias
RUN pip install threading

# Establece el directorio de trabajo
WORKDIR /app

# Exponer el puerto 8000
EXPOSE 8000

# Ejecuta el script al iniciar el contenedor
CMD ["python", "main.py"]
