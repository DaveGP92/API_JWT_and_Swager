# Usamos una imagen oficial de Python como base
FROM python:3.11.0-buster

# Exponemos el puerto donde la app estará corriendo (usualmente el 8000 para Django)
EXPOSE 8000

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /django-app

# Copiamos el archivo de dependencias al contenedor
COPY requirements.txt /django-app/

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

# Copiamos el resto de la aplicación al contenedor
COPY . /django-app/


# Ejecutamos el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
