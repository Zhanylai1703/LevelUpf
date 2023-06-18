from django.core.mail import send_mail
from django.conf import settings


class FeedbackMessageManager:
    @staticmethod
    def perform_create(feedback_message):
        message = f"Имя пользователя: {feedback_message.name}\n" \
                  f"{feedback_message.feedback}\n\n"

        send_mail(
            f"Feedback from {feedback_message.email}",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        return {"message": "Ваше сообщение успешно отправлено."}

