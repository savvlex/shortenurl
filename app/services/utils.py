import random
import string

SHORT_DEAFAULT_LENGTH = 6
SYMBOLS_ALLOWED = string.ascii_letters + string.digits


def generate_unique_short_link(length=SHORT_DEAFAULT_LENGTH) -> str | None:
    """
    Generates a unique short link of the specified length.
    """
    return ''.join(random.choices(SYMBOLS_ALLOWED, k=length))
