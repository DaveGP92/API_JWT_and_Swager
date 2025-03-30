# Proyecto: API de Gestión de Tareas

Este proyecto es una API REST construida con Django Rest Framework (DRF) que permite gestionar tareas. Implementa autenticación con JWT y documentación con Swagger.

## 🚀 Tecnologías utilizadas
- Django Rest Framework
- Django
- drf-spectacular (para documentación OpenAPI/Swagger)
- JWT (para autenticación)
- MySQL (base de datos)

## 📌 Instalación y configuración
### Requisitos previos
- Docker y Docker Compose (opcional, pero recomendado)

Si no usas Docker:
- Python 3.12+
- MySQL 8.0+

### Pasos para instalar
1. Clona el repositorio:
   ```sh
   git clone https://github.com/DaveGP92/API_JWT_and_Swager.git
   cd tu_repositorio
   ```
2. Si estás en producción, ejecuta: 
    cp .env.development .env

-  Si estás en desarrollo, ejecuta:
    cp .env.development .env

3. Si usas Docker, levanta los servicios:
   
   docker-compose up --build (construir y correr)
   docker-compose stop (detener)
   
4. Si no usas docker:
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser (para acceder al endpoint del token)
   python manage.py runserver

## 📡 Endpoints principales
### Autenticación JWT
- `POST /api-v1/token/` → Obtener tokens de acceso y refresco
- `POST /api-v1/token/refresh/` → Renovar token de acceso
- `POST /api-v1/token/verify/` → Verificar token

### Tareas (`/api-v1/tasks/`)
- `GET /api-v1/tasks/` → Lista todas las tareas
- `POST /api-v1/tasks/` → Crea una nueva tarea
- `GET /api-v1/tasks/{id}/` → Obtiene una tarea específica
- `PUT /api-v1/tasks/{id}/` → Actualiza una tarea
- `DELETE /api-v1/tasks/{id}/` → Elimina una tarea

### Documentación con Swagger
- `GET /api-v1/schema/swagger/` → Interfaz Swagger UI

