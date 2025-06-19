from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Reply

@receiver(post_save, sender=Reply)
def send_notification_to_post_author(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Новый отклик на ваше объявление',
            message=(
                    f'Пользователь {instance.user} оставил отклик на "{instance.post.title}".\n\n'
                    f'Перейдите по ссылке для просмотра объявления: '
                    f'http://127.0.0.1:8000/post/{instance.post.id}/'
                    ),
            from_email= settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.post.author.email],
        )

@receiver(post_save, sender=Reply)
def notify_reply_accepted(sender, instance, **kwargs):
    if instance.accepted:
        send_mail(
        subject = f'Ваш отклик на "{instance.post.title}" был принят!',
        message = f'Ваш отклик:\n\n"{instance.text}"\n\nбыл принят автором объявления.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[instance.user.email],
        )