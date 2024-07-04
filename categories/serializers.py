from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):

    pk = serializers.IntegerField(
        read_only=True,
    )
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(
        read_only=True,
    )

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # .get ⇒ 첫번째 인자가 없을 경우에 두번째 인자를 default 값으로 설정 (=사용자가 name을 보내지 않았다면 현재의 값을 보내서 사용한다.)
        instance.name = validated_data.get("name", instance.name)
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()
        return instance
