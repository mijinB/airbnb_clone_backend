from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        """ 포함시킬 속성 설정
        fields = (
            "name",
            "kind",
        )
        fields = "__all__" """
        """ 제외시킬 속성 설정
        exclude = ("created_at",) """
