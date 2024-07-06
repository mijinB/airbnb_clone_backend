from rest_framework.serializers import ModelSerializer
from .models import Room, Amenity


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        # 관계성(relationship)을 확장하는 첫번째 방법. 하지만, custom이 불가능하다. 모든 정보가 다 보인다.
        depth = 1


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"
