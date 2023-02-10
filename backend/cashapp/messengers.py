import smtplib
from email.mime.text import MIMEText

import httpx
from django.conf import settings


def send_email(to: str, subject: str, text: str) -> None:
    msg = MIMEText(text)
    msg['Subject'] = subject
    msg['From'] = settings.NO_REPLY_EMAIL
    msg['To'] = to

    smtp_client = smtplib.SMTP(settings.APP_URL_BASE)
    smtp_client.sendmail(settings.NO_REPLY_EMAIL, [to], msg.as_string())
    smtp_client.quit()


def send_sms(to: str, text: str) -> None:
    try:
        response: httpx.Response = httpx.get(
            f'{settings.SMS_PROVIDER_URL}?login={settings.SMS_PROVIDER_LOGIN}&psw={settings.SMS_PROVIDER_PASSWORD}&phones={to}&mes={text}'
        )
        response.raise_for_status()
    except httpx.HTTPError as exc:
        print(f"Error while requesting {exc}")
    return None
