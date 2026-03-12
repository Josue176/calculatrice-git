"""Module d'authentification calculatrice securisee"""

USERS = {
    "admin": "password123",
    "user": "calc2025"
}

def login(username: str, password: str) -> bool:
    """Verifie les identifiants de l'utilisateur."""
    return USERS.get(username) == password

def logout(username: str) -> str:
    """Deconnecte l'utilisateur et retourne un message."""
    return f"Au revoir, {username} !"