categories = [
    {
        "name": "user",
        "label": "Usuario",
        "permissions": [
            {
                "name": "create",
                "label": "Crear un usuario.",
                "description": "Permite a un usuario autorizado crear nuevas cuentas de usuario en el sistema."
            },
            {
                "name": "update",
                "label": "Actualizar un usuario.",
                "description": "Permite a un usuario autorizado a actualizar la información de un usuario en el sistema.\
                    Solo puede acceder a aquellos que tienen un rol jerárquico inferior al suyo."
            },
            {
                "name": "delete",
                "label": "Borrar un usuario.",
                "description": "Permite a un usuario autorizado a borrar una cuenta de un usuario en el sistema.\
                    Solo puede acceder a aquellos que tienen un rol jerárquico inferior al suyo."
            },
            {
                "name": "get_list",
                "label": "Listar usuarios.",
                "description": "Permite a un usuario obtener una lista de usuarios.\
                    Solo puede acceder a aquellos que tienen un rol jerárquico inferior al suyo."
            },
        ]
    }
]

def get_permissions():
    return [item for category in categories for permission in category['permissions'] for item in [category['name'] + '.' + permission['name']]]
