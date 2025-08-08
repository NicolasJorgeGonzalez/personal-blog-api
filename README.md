# Blog API con FastAPI y MongoDB

API REST para gestionar publicaciones de un blog personal, creada con FastAPI y MongoDB. Permite realizar operaciones CRUD (crear, leer, actualizar, eliminar) sobre publicaciones, incluyendo manejo de etiquetas, categorías y búsqueda por texto.

---

## Características

- CRUD completo para publicaciones
- Manejo de tags y categorías
- Búsqueda por texto en título y categoría
- Uso de FastAPI para alta performance y documentación automática
- Base de datos MongoDB para almacenamiento flexible y escalable

---

## Requisitos

- Python 3.10+
- MongoDB en funcionamiento
- Dependencias en `requirements.txt`

---

## Instalación

1. Clonar el repositorio:

    ```bash
    git clone https://github.com/NicolasJorgeGonzalez/personal-blog-api.git
    cd personal-blog-api
    ```

2. Crear y activar entorno virtual:

    - Linux/Mac:

      ```bash
      python -m venv venv
      source venv/bin/activate
      ```

    - Windows (PowerShell):

      ```powershell
      python -m venv venv
      .\venv\Scripts\Activate.ps1
      ```

    - Windows (cmd):

      ```cmd
      python -m venv venv
      .\venv\Scripts\activate.bat
      ```

3. Instalar dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configurar conexión a MongoDB (archivo de configuración o variables de entorno).

---

## Uso

Ejecutar la API con:

```bash
uvicorn main:app --reload
```

## Documentación
La documentación interactiva estará disponible en:

http://localhost:8000/docs
