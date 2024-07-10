from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    # 이게 PublicUser의 아래로 가게되면 "me"를 username으로 인식해서 오류가 나게 된다.
    path("me", views.Me.as_view()),
    # 위 주석과 같은 문제를 해결하고자 username앞에 "@"를 추가하는 방법도 있다.
    path("@<str:username>", views.PublicUser.as_view()),
]
