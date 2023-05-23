from django.contrib.auth.models import AbstractUser
# from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Класс пользователя
    """
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
