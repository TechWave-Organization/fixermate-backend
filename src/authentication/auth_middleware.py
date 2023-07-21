import requests
from decouple import config

from src.schemas.user import UserAuth


def verify_token(access_token:str):
    try:
        result = requests.get(f"{config('AUTH_URL')}/auth/verify-token",
                    headers={
                        "Authorization": f"Bearer {access_token}",
                    })
        if result.status_code == 200:
            return result.json()
        return None
    except:
        return None
    
class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access_token = None
        authorization_header = request.headers.get("Authorization")

        if authorization_header:
            try:
                _, access_token = authorization_header.split()
            except ValueError:
                pass

        user_data = verify_token(access_token)
        user = None
        if user_data:
            user = UserAuth(
                id=user_data.get("id"),
                username=user_data.get("username"),
                permissions=user_data.get("permissions"),
            )
        request.user = user
        response = self.get_response(request)
        return response