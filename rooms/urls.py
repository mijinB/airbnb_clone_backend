from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_rooms),
    # <받을 파라미터의 type:받은 파라미터를 부를 별명>
    path("<int:room_id>", views.see_one_room),
]
