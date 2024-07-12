from rest_framework.test import APITestCase
from . import models


class TestAmenities(APITestCase):

    NAME = "Amenity Test"
    DESC = "Amenity Des"

    URL = "/api/v1/rooms/amenities/"

    # 먼저 실행되면서 Amenity가 하나 생성될 것이고,
    def setUp(self) -> None:
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    # 하나의 객체가 있는 list를 반환받을 것이다.
    def test_all_amenities(self):
        # self.client ⇒ API로 get / post / put / delete request를 보낼 수 있게 해준다.
        response = self.client.get(self.URL)
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

    def test_create_amenity(self):

        new_amenity_name = "New Amenity"
        new_amenity_description = "Amenity desc."

        response = self.client.post(
            self.URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_description,
            },
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["name"],
            new_amenity_name,
        )
        self.assertEqual(
            data["description"],
            new_amenity_description,
        )

        response = self.client.post(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)
