from rest_framework.views import APIView
from app01.serializers.auth_class import LoginAuth
from app01.serializers.response import BaseResponse
from app01.serializers.exceptions import PriceException
from django_redis import get_redis_connection
from app01.models import *
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import datetime



from django.conf import settings

class ShoppingCarView(APIView):

    authentication_classes = [LoginAuth,]
    response = BaseResponse()
    conn = get_redis_connection("default")

    def post(self,request):
        """
        结算课程的保存
        :param request: 
        :return: 
        """
        course_id_list = request.data.get("course_id_list")

        for course_id in course_id_list:
            shopping_car_key = settings.LUFFY_SHOPPING_CAR_KEY
            shopping_car_key = shopping_car_key%(request.user.pk,course_id)

            if not self.conn.exists(shopping_car_key):
                self.response.error_msg = "购物车中没有该课程"
                self.response.code = 2000
                raise Exception

            course_detail = self.conn.hgetall(shopping_car_key)

            course_detail_dict = {}

            for key,val in course_detail.items():
                key = key.decode("utf8")
                val = val.decode("utf8")
                if key == "price_policys":
                    val = json.loads(val)

                course_detail_dict[key] = val

            now = datetime.datetime.now().date()

            coupon_record_list = CouponRecord.objects.filter(
                user=request.user,
                status=0,
                coupon__valid_begin_date__lt=now,
                coupon__valid_end_date__gt=now
            )

        return JsonResponse(self.response.dict)

    def get(self,request):
        pass