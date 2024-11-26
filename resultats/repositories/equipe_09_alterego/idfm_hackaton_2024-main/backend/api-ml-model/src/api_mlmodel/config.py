from dotenv import load_dotenv
from pathlib import Path
import os


def load_api_key(env_file: str) -> str:
    """
    Loads the API key from the specified .env file.

    Args:
        env_file (str): Path to the .env file.

    Returns:
        str: API key value.
    """
    load_dotenv(dotenv_path=Path(env_file).resolve())
    api_key = os.getenv("PRIM")
    if not api_key:
        raise ValueError("API key not found in the .env file.")
    return api_key
