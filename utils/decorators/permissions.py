from functools import wraps
from typing import List

def permissions_required(role: str, permissions: List[str]):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                user = args[0].user
                if len(user.permissions) < 1:
                    return 403, {"detail": "User does not have any permission."}
                for permission_required in permissions:
                    perm_req = f"{role}.{permission_required}"
                    if perm_req not in user.permissions:
                        return 403, {
                            "error": "User does not have the required permissions."
                        }
            except:
                return 401, {"error": "Unauthorized."}
            value = function(*args, **kwargs)
            return value

        return wrapper
    return decorator