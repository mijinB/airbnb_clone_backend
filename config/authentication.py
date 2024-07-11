# Authentication class가 views.py보다 먼저 실행되고,
# user를 찾은 다음 거기서 찾아진 user가 모든 views의 request.user로 들어가게 된다.
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class TrustMeBroAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get("Trust-Me")
        if not username:
            # 로그아웃을 시도했다는 것이므로 로그아웃 될 것이다.
            return None
        try:
            # 로그인 시 user와 None을 튜플로 함께 보내는건 규칙이다.
            user = User.objects.get(username=username)
            return (user, None)
        except User.DoesNotExist:
            # 로그인 시도를 했지만 username이 존재하지 않기 때문에 예외처리
            raise AuthenticationFailed(f"No user {username}")
