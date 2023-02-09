import envparse


DEBUG: bool = envparse.env("DEBUG", default=True, cast=bool)
APP_URL: str = envparse.env("APP_URL", default='localhost:3000/', cast=str).rstrip('/')
