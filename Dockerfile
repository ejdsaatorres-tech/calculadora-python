FROM python:3.9-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# 1. Copiamos requirements.txt (asumiendo que está en la raíz, fuera de src)
COPY requirements.txt .

# 2. Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copiamos TODO el proyecto (incluida la carpeta src)
COPY . .

# Exponemos el puerto
EXPOSE 5000

# IMPORTANTE: Agregamos src al PYTHONPATH para evitar errores de importación
ENV PYTHONPATH=/app/src

# 4. Ajustamos el comando para ejecutar app.py dentro de src
CMD ["python","-m", "src.app"]