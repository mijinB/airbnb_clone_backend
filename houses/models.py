from django.db import models  # type: ignore


class House(models.Model):
    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField(help_text="Positive Numbers Only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True,
        # 도움말
        help_text="Does this house allow pets?",
        # 기본 title은 변수 이름이지만 verbose_name로 변경 가능
        verbose_name="Pets Allowed?",
    )

    def __str__(self):
        return self.name
