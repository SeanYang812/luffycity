from rest_framework.views import APIView
from app01.serializers.auth_class import LoginAuth
from app01.serializers.response import BaseResponse
from app01.serializers.exceptions import PriceException
from django_redis import get_redis_connection
from app01.models import *
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

class ShoppingCarView(APIView):

    authentication_classes = [LoginAuth,]
    response = BaseResponse()
    conn = get_redis_connection("default")

    def post(self,request):
        """
        购物添加课程请求
        :param request: 
        :return: 
        """
        # 获取数据
        course_id = request.data.get("course_id")
        price_policy_id = request.data.get("price_policy_id")

        try:
            # 校验课程是否存在
            course_obj = Course.objects.get(pk=course_id)

            # 查找课程关联的所有的价格策略
            price_policy_list = course_obj.price_policy.all()

            # 将当前课程的所有价格策略取出来将每个价格策略以id为键组成字典
            price_policy_dict = {}
            for price_policy_item in price_policy_list:
                price_policy_dict[price_policy_item.pk] = {
                    "price":price_policy_item.price,
                    "valid_period":price_policy_item.valid_period,
                    "valid_period_text":price_policy_item.get_valid_period_display()
                }

            # 判断如果前端服务器发送的价格策略id不在字典中报错
            if price_policy_id not in price_policy_dict:
                raise PriceException()

            # 将用户id和课程id拼接到一起 组成键
            shopping_car_key = "ShoppingCarKey_%s_%s"
            user_id = request.user.pk
            shopping_car_key = shopping_car_key%(user_id,course_id)

            # 新字典的值
            val = {
                "course_name":course_obj.name,
                "course_img":course_obj.course_img,
                # 将值为字典的提前进行json序列化，这样取出来的时候就可以直接将其反序列化成字典
                "price_policys":json.dumps(price_policy_dict),
                "default_prcie_policy_id":price_policy_id
            }
            # redis操作 批量设置键值对
            self.conn.hmset(shopping_car_key,val)
            self.response.data = "success"

        except PriceException as e:
            self.response.code = "3000"
            self.response.error_msg = e.msg

        except ObjectDoesNotExist as e:
            self.response.code = "2000"
            self.response.error_msg = "该课程不存在！！"

        return JsonResponse(self.response.dict)

    def get(self,request):
        pass