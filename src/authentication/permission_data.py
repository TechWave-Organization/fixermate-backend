categories = [
    {
        "name": "user",
        "label": "Usuario",
        "permissions": [
            {
                "name": "create",
                "label": "Crear un usuario.",
                "description": "Permite a un usuario autorizado crear nuevas cuentas de usuario en el sistema.",
            },
            {
                "name": "update",
                "label": "Actualizar un usuario.",
                "description": "Permite a un usuario autorizado a actualizar la información de un usuario en el sistema.\
                    Solo puede acceder a aquellos que tienen un rol jerárquico inferior al suyo.",
            },
            {
                "name": "delete",
                "label": "Borrar un usuario.",
                "description": "Permite a un usuario autorizado a borrar una cuenta de un usuario en el sistema.\
                    Solo puede acceder a aquellos que tienen un rol jerárquico inferior al suyo.",
            },
            {
                "name": "view",
                "label": "Listar usuarios.",
                "description": "Permite a un usuario obtener una lista de usuarios.\
                    Solo puede acceder a aquellos que tienen un rol jerárquico inferior al suyo.",
            },
        ],
    },
    {
        "name": "client",
        "label": "Cliente",
        "permissions": [
            {
                "name": "create",
                "label": "Crear un cliente.",
                "description": "Permite a un usuario autorizado crear nuevos clientes en el sistema.",
            },
            {
                "name": "view",
                "label": "Visualizar clientes.",
                "description": "Permite a un usuario autorizado acceder y visualizar la información de los clientes existentes.",
            },
            {
                "name": "update",
                "label": "Actualizar un cliente.",
                "description": "Permite a un usuario autorizado hacer cambios en los detalles de un cliente existente.",
            },
            {
                "name": "delete",
                "label": "Borrar un cliente.",
                "description": "Permite a un usuario autorizado eliminar un cliente del sistema.",
            },
        ],
    },
    {
        "name": "brand",
        "label": "Marca",
        "permissions": [
            {
                "name": "create",
                "label": "Crear una marca.",
                "description": "Permite a un usuario autorizado crear nuevas marcas en el sistema.",
            },
            {
                "name": "view",
                "label": "Visualizar marcas.",
                "description": "Permite a un usuario autorizado acceder y visualizar la información de las marcas existentes.",
            },
            {
                "name": "update",
                "label": "Actualizar una marca.",
                "description": "Permite a un usuario autorizado hacer cambios en los detalles de una marca existente.",
            },
            {
                "name": "delete",
                "label": "Borrar una marca.",
                "description": "Permite a un usuario autorizado eliminar una marca del sistema.",
            },
        ],
    },
    {
        "name": "device_model",
        "label": "Modelo de dispositivo",
        "permissions": [
            {
                "name": "create",
                "label": "Crear un modelo de dispositivo.",
                "description": "Permite a un usuario autorizado crear nuevos modelos de dispositivos en el sistema.",
            },
            {
                "name": "view",
                "label": "Visualizar modelos de dispositivo.",
                "description": "Permite a un usuario autorizado acceder y visualizar la información de los modelos de dispositivos existentes.",
            },
            {
                "name": "update",
                "label": "Actualizar un modelo de dispositivo.",
                "description": "Permite a un usuario autorizado hacer cambios en los detalles de un modelo de dispositivo existente.",
            },
            {
                "name": "delete",
                "label": "Borrar un modelo de dispositivo.",
                "description": "Permite a un usuario autorizado eliminar un modelo de dispositivo del sistema.",
            },
        ],
    },
    {
        "name": "device",
        "label": "Dispositivo",
        "permissions": [
            {
                "name": "create",
                "label": "Crear un dispositivo.",
                "description": "Permite a un usuario autorizado crear nuevos dispositivos en el sistema.",
            },
            {
                "name": "view",
                "label": "Visualizar dispositivos.",
                "description": "Permite a un usuario autorizado acceder y visualizar la información de los dispositivos existentes.",
            },
            {
                "name": "update",
                "label": "Actualizar un dispositivo.",
                "description": "Permite a un usuario autorizado hacer cambios en los detalles de un dispositivo existente.",
            },
            {
                "name": "delete",
                "label": "Borrar un dispositivo.",
                "description": "Permite a un usuario autorizado eliminar un dispositivo del sistema.",
            },
        ],
    },
]


def get_permissions():
    return [
        item
        for category in categories
        for permission in category["permissions"]
        for item in [category["name"] + "." + permission["name"]]
    ]
