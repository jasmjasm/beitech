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
- API order: "http://localhost:8000/api/order/"
- Incluyo JSON de prueba para la insercion de la orden en la API:
- ````
    {
        "date": "2021-03-22",
        "customer": 1,
        "delivery_address": "Calle 10",
        "total": "0",
        "order_detail": [
            {
                "product_description": "Galletas",
                "quantity": 3,
                "product": 3
            },
            {
                "product_description": "Leche",
                "quantity": 1,
                "product": 1
            },
            {
                "product_description": "Pan",
                "quantity": 2,
                "product": 2
            },
            {
                "product_description": "lll",
                "quantity": 2,
                "product": 4
            },
            {
                "product_description": "yyy",
                "quantity": 2,
                "product": 5
            }
        ]
    }


## Para acceder al panel administrativo de Django

- python manage.py runserver
- **localhost:8000/admin** con el usuario: **beitech@email.com** con contraseña: **1234** se ingresa a este sitio.
- En esta secccion se puede visualizar/administrar todos los modelos de datos, se puede establecer los productos por cliente con su respectivo precio.
