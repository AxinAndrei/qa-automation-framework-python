import os


def get_browser():
    return os.getenv("BROWSER", "chrome").lower()


def is_headless():
    return os.getenv("HEADLESS", "false").lower() == "true"


def get_base_url():
    return "https://www.google.com"

# Timeouts
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", 5))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", 10))
