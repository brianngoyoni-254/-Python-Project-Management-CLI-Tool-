def validate_email(email: str) -> bool:
    """
    Simple, safe email validation for CLI usage.
    """
    return isinstance(email, str) and "@" in email and "." in email


def validate_user(name: str, email: str):
    """
    Lightweight validation wrapper used by services.
    Returns a CLEAN dict OR None.
    """

    if not name or not isinstance(name, str):
        return None

    if not validate_email(email):
        return None

    return {
        "name": name.strip(),
        "email": email.strip()
    }