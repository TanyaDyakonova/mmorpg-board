from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse

CATEGORY_CHOICES = [
    ('tank', 'Танки'),
    ('healer', 'Хилы'),
    ('dd', 'ДД'),
    ('merchant', 'Торговцы'),
    ('guildmaster', 'Гилдмастеры'),
    ('questgiver', 'Квестгиверы'),
    ('blacksmith', 'Кузнецы'),
    ('leatherworker', 'Кожевники'),
    ('alchemist', 'Зельевары'),
    ('spellmaster', 'Мастера заклинаний'),
]

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.get_name_display()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ответ от {self.user.username} в посте {self.post.title}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'