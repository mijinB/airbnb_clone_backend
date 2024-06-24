from django.db import models

# DB에 추가하지 않고 다른 model에서 재사용하기 위한 model이다.


class CommonModel(models.Model):
    """Model Definition for Common"""

    # auto_now_add : field의 값을 해당 object가 처음 생성되었을 때 date로 설정한다.(공식문서)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    # auto_now : object가 저장될 때마다 해당 field를 현재 date로 설정한다.
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    # django가 이 model을 봐도 DB에 저장하지 않을 것이다.
    class Meta:
        abstract = True
