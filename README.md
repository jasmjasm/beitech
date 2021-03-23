# Beitech

Prueba tecnica Python Beitech.
Proyecto desarrollado en Django + SQLite + Restframework + JQuery

## Para para instalar proyecto en modo desarrollo (backend)

- cd PROJECT_FOLDER
- python3.7 -m venv venv
- source venv/bin/activate
- Crear un archivo .env en la raiz del projecto con la clave secreta para Django. **SECRET_KEY='una_clave_secreta_y_segura_para_mi_aplicacion'**
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py loaddata initial
- python manage.py runserver
- Los datos iniciales crean por defecto un usuario con todos los permisos sobre la aplicacion usuario: **beitech@email.com** con contraseña: **1234**
- La api rest queda de público acceso por efectos de la prueba.
- API root: "http://localhost:8000/api/"
- API order: "http://localhost:8000/api/order/"
- API order_detail: "http://localhost:8000/api/orderdetail/"
- 

## Para acceder al panel administrativo de Django

- python manage.py runserver
- **localhost:8000/admin** con el usuario y contraseña especificado anteriormente
- En esta secccion se puede visualizar todos los modelos de datos, los cuales pueden ser administrador a través de el panel administrativo Django.