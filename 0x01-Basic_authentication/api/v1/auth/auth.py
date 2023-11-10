from typing import List, TypeVar
from flask import request

class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authentication method
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization header method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user method
        """
        return None

