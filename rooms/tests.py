from rest_framework.test import APITestCase
from . import models


class TestAmenities(APITestCase):

    NAME = "Amenity Test"
    DESC = "Amenity Des"

    # 먼저 실행되면서 Amenity가 하나 생성될 것이고,
    def setUp(self) -> None:
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    # 하나의 객체가 있는 list를 반환받을 것이다.
    def test_all_amenities(self):
        # self.client ⇒ API로 get / post / put / delete request를 보낼 수 있게 해준다.
        response = self.client.get("/api/v1/rooms/amenities/")
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
        )
