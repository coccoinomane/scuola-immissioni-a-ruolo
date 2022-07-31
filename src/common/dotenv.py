import os, dotenv
from typing import Any, List

dotenv.load_dotenv()


def getenv(key: str, default: Any = "") -> str:
    """
    Shorthand to get environment variables
    """
    return os.getenv(key, default)
