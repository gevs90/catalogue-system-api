from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To, From, Subject, Content
from fastapi import status
from app.exceptions import log


def send_email_to_admin(subject, content, emails):
    message = Mail(
        from_email=From("support@influencities.net"),
        to_emails=[To(user.email) for user in emails],
        subject=Subject(subject),
        plain_text_content=Content("text/plain", content)
    )

    try:
        sendgrid_api_key = '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'
        sg = SendGridAPIClient(api_key=sendgrid_api_key)
        sg.send(message)
    except Exception as e:
        log(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
