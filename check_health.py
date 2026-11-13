import os

MONITOR_URL_ENV_VAR = "MONITOR_URL"
ALLOWED_URL_PREFIXES = ("http://", "https://")


class ConfigError(Exception):
    """Raised when the checker's own configuration is missing or invalid."""


def load_config():
    url = os.environ.get(MONITOR_URL_ENV_VAR)

    if url is None:
        raise ConfigError(
            f"{MONITOR_URL_ENV_VAR} environment variable is missing. "
            "Set it to the full health endpoint URL."
        )

    url = url.strip()

    if not url:
        raise ConfigError(
            f"{MONITOR_URL_ENV_VAR} is empty. "
            "Set it to the full health endpoint URL."
        )

    if not url.startswith(ALLOWED_URL_PREFIXES):
        raise ConfigError(
            f"{MONITOR_URL_ENV_VAR} must start with http:// or https://, got: {url}"
        )

    return url
