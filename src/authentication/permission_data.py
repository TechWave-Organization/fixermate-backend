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
                "description": "Permite a un usuario autorizado crear nuevos clientes en el sistema.\
                    Este usuario puede ingresar la información requerida en la base de datos del sistema.",
            },
            {
                "name": "view",
                "label": "Ver un cliente.",
                "description": "Permite a un usuario autorizado acceder y visualizar la información de los clientes existentes.\
                    Tambien incluyendo datos personales y de contacto.",
            },
            {
                "name": "update",
                "label": "Actualizar un cliente.",
                "description": "Permite a un usuario autorizado hacer cambios en los detalles de un cliente existente.\
                    Este usuario puede actualizar información de contacto. También puede modificar detalles personales entre otros.",
            },
            {
                "name": "delete",
                "label": "Borrar un cliente.",
                "description": "Permite a un usuario autorizado eliminar un cliente del sistema. Este proceso debería usarse con precaución.\
                    Al eliminar se eliminarán todas las informaciones asociadas con el cliente.",
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
