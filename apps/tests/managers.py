from apps.tests.models import (
    Answer,
)

from django.core.mail import send_mail


def check_test_and_send_email(user_email, submitted_answers):
    score = 0
    total_questions = len(submitted_answers)

    for answer_id in submitted_answers:
        try:
            answer = Answer.objects.get(id=answer_id)
            if answer.is_true:
                score += 1
        except Answer.DoesNotExist:
            return {"error": f"Answer with id {answer_id} does not exist."}

    # Prepare the email
    subject = 'Your Test Results'
    message = f'You scored {score} out of {total_questions}.'
    from_email = 'kasymkulovajanylai@gmail.com'  

    # Send the email
    send_mail(subject, message, from_email, [user_email], fail_silently=False)

    return {'score': score, 'total_questions': total_questions}