import qrcode
import qrcode.image.svg as qr_svg
from django.conf import settings
from pdf417gen import encode, render_svg
from xml.etree.ElementTree import ElementTree, Element, SubElement
import xml


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


class PDF417Code:

    @staticmethod
    def generate(uuid: str, ticket_id: int) -> str:
        new_pdf: ElementTree = render_svg(encode(data=f"{uuid}:{ticket_id}", security_level=3), ratio=4)
        return xml.etree.ElementTree.tostring(new_pdf.getroot(), encoding='unicode', method='xml')

    def __call__(self, uuid: str, ticket_id: int) -> str:
        return self.generate(uuid, ticket_id)


qr_instance: QrCode = QrCode(settings.APP_URL_BASE)
