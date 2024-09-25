from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=200)
    profile = models.ImageField(upload_to='%Y%m%d/', blank=True, null=True)
    luckypoint = models.IntegerField(default=0, blank=True, null=True)

    # groups와 user_permissions 필드를 수정
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # 충돌 방지를 위한 related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # 충돌 방지를 위한 related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.nickname
