from rest_framework.views import APIView
from app01.models import *
from app01.serializers.Serializers import *
from rest_framework.response import Response


class CourseModelView(APIView):

    def get(self,request,*args,**kwargs):
        course_obj = Course.objects.all()
        cs = CourseSerializer(course_obj,many=True)

        return Response(cs.data)


class CourseDetailModelView(APIView):

    def get(self,request,pk,*args,**kwargs):
        coursedetail_obj = CourseDetail.objects.filter(pk=pk).first()
        cds = CourseDetailModelSerializers(coursedetail_obj)
        return Response(cds.data)


# class OftenAskedQuestionModelView(APIView):
#
#     def get(self,request,*args,**kwargs):
#
#         often_obj = OftenAskedQuestion.objects.all()
#         oas = OftenAskedQuestionModelSerializers(often_obj,many=True)
#
#         return Response(oas.data)