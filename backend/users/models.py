from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models import UniqueConstraint


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name', )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=settings.LENGTH_OF_FIELDS)
    last_name = models.CharField(
        max_length=settings.LENGTH_OF_FIELDS,
        verbose_name='Фамилия',)
    email = models.EmailField(
        max_length=settings.LENGTH_OF_FIELDS,
        verbose_name='email',
        unique=True)
    username = models.CharField(
        verbose_name='username',
        max_length=settings.LENGTH_OF_FIELDS,
        unique=True,
        validators=(UnicodeUsernameValidator(),))

    class Meta:
        ordering = ('username', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='follower',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        related_name='following',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-id', )
        constraints = [
            UniqueConstraint(
                fields=('user', 'author'),
                name='unique_follow')
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self) -> str:
        return f"{self.user} подписан на {self.author}"
