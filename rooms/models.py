from django.db import models


class Room(models.Model):
    """Model Definition for Rooms"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    country = models.CharField(
        max_length=50,
        default="Korea",
    )
    city = models.CharField(
        max_length=80,
        default="Soeul",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )


class Amenity(models.Model):
    """Model Definition for Amenity"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,
    )
