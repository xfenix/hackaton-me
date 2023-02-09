import qrcode
import qrcode.image.svg as qr_svg
from cashapp import env_settings


class QrCode:

    def __init__(self, app_url: str):
        self._app_url: str = app_url

    def generate(self, event_alias: str) -> str:
        img = qrcode.make(
            f"{self._app_url}/{event_alias}/",
            image_factory=qr_svg.SvgPathFillImage,
            box_size=env_settings.QR_CODE_BOX_SIZE
        )
        return img.to_string(encoding='unicode')


qr_instance: QrCode = QrCode(env_settings.APP_URL)
