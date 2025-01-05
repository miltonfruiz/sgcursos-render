# Sistema de Gestión de Cursos

Este proyecto es una aplicación web diseñada para la gestión de cursos, permitiendo administrar información como alumnos, profesores y materias. Puedes acceder a la versión desplegada [aquí](https://sgcursos-muom.onrender.com/).

## Tecnologías Utilizadas

- **Backend**: Flask
  - Flask-Migrate para la gestión de migraciones de base de datos.
- **Frontend**: HTML, CSS y JavaScript
- **Base de Datos**: SQLAlchemy (compatible con PostgreSQL)
- **Despliegue**: Render

## Estructura del Proyecto

```
Sistema de Gestion de Cursos/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   └── templates/
│
├── app.py
├── requirements.txt
└── env/
```

### Descripción de Archivos y Carpetas

- **app/**: Carpeta principal del módulo de la aplicación.
  - `__init__.py`: Configuración inicial de la aplicación Flask.
  - `config.py`: Configuraciones generales del proyecto (como configuración de base de datos).
  - `models.py`: Definición de modelos para la base de datos.
  - `routes.py`: Rutas de la aplicación.
  - `static/`: Archivos estáticos (CSS, JavaScript, imágenes).
  - `templates/`: Plantillas HTML para las vistas.
- **app.py**: Archivo principal para ejecutar la aplicación.
- **requirements.txt**: Dependencias del proyecto.
- **env/**: Carpeta opcional para configuraciones de entorno local.

## Configuración e Instalación

### Prerrequisitos

- Python 3.8 o superior
- Gestor de paquetes `pip`
- Entorno virtual de Python (opcional pero recomendado)

### Pasos para Configurar el Proyecto

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/sistema-gestion-cursos.git
   cd sistema-gestion-cursos
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv env
   source env/bin/activate   # En Windows: env\Scripts\activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno necesarias en un archivo `.env` o directamente en el sistema (por ejemplo, la URL de la base de datos).

5. Realizar las migraciones de base de datos:

   ```bash
   flask db upgrade
   ```

6. Ejecutar la aplicación localmente:

   ```bash
   flask run
   ```

7. Acceder a la aplicación en el navegador:

   ```
   http://localhost:5000
   ```

## Despliegue

El proyecto está desplegado en Render. El proceso de despliegue incluye:

1. Configurar un repositorio en GitHub con el código del proyecto.
2. Vincular el repositorio a Render.
3. Configurar las variables de entorno necesarias en el panel de Render.
4. Render se encargará del despliegue automático en cada push al repositorio principal.

## Contribución

Si deseas contribuir a este proyecto:

1. Realiza un fork del repositorio.
2. Crea una rama para tus cambios:

   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

3. Realiza tus cambios y haz commits:

   ```bash
   git commit -m "Agregada nueva funcionalidad"
   ```

4. Envía un pull request describiendo los cambios realizados.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.

