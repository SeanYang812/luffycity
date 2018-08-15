from rest_framework.views import APIView
from app01.models import *
import random,uuid
from django.http import JsonResponse

class LoginModelView(APIView):

    def post(self,request):
        username = request.data.get("user")
        password = request.data.get("pwd")

        try:
            response = {"code":1000, "user":"","msg":""}
            user = User.objects.filter(user=username,pwd=password).first()
            if user:
                random_str = uuid.uuid4()
                UserToken.objects.update_or_create(user=user,defaults={"token":random_str})
                response["token"] = random_str
                response["user"] = user.user
            else:
                response['code'] = 2000
                response["msg"] = "用户名或密码错误！"
        except Exception as e:
            response['code'] = 3000
            response['msg'] = str(e)
        print(response)
        return JsonResponse(response)