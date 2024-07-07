from django.urls import path
from .views import Wishlists, WishListDetail

urlpatterns = [
    path("", Wishlists.as_view()),
    path("<int:pk>", WishListDetail.as_view()),
]
