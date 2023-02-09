import qrcode
import qrcode.image.svg as qr_svg
from django.conf import settings


class QrCode:

    def __init__(self, app_url: str):
        self._app_url: str = app_url

    def generate(self, event_alias: str) -> str:
        img = qrcode.make(
            f"{self._app_url}/{settings.CHECKOUT_INFIX}/{event_alias}/",
            image_factory=qr_svg.SvgPathFillImage,
            box_size=settings.QR_CODE_BOX_SIZE
        )
        return img.to_string(encoding='unicode')


qr_instance: QrCode = QrCode(settings.APP_URL_BASE)
