import envparse


DEBUG: bool = envparse.env("DEBUG", default=True, cast=bool)
APP_URL: str = envparse.env("APP_URL", default='localhost:3000/', cast=str).rstrip('/')

QR_CODE_BOX_SIZE: int = envparse.env("QR_CODE_BOX_SIZE", default=40, cast=int)
