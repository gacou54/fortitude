import uuid


def generate_random_8char() -> str:
    return str(uuid.uuid4())[:8]
