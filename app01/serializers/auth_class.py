

from rest_framework.authentication import  BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app01.models import UserToken

# 认证
class LoginAuth(BaseAuthentication):

    def authenticate(self, request):
        token = request.GET.get("token")

        token_obj = UserToken.objects.filter(token=token).first()

        if token_obj:
            return token_obj.user,token_obj.token
        else:
            raise AuthenticationFailed("认证失败了！")