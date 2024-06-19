from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Model Definition for Users"""

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")
    # BooleanField는 non-nullable field라서 default 값을 지정해주거나 null=True로 지정해줘야 migration 가능
    is_host = models.BooleanField(default=False)
