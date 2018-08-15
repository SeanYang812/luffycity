from rest_framework import serializers
from app01.models import *
from django.contrib.contenttypes.models import ContentType

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    level=serializers.SerializerMethodField()
    def get_level(self, obj):
        level = obj.get_level_display()
        return level


class CourseDetailModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseDetail
        fields = "__all__"

    course_name = serializers.CharField(source="course.name")
    course_img = serializers.CharField(source="course.course_img")
    course_brief = serializers.CharField(source="course.brief")

    teachers = serializers.SerializerMethodField()
    def get_teachers(self,obj):
        temp = []
        for i in obj.teachers.all():
            temp.append(i.name)
        return temp


    recommend_courses = serializers.SerializerMethodField()
    def get_recommend_courses(self,obj):
        temp = []
        for i in obj.recommend_courses.all():
            temp.append({
                "name":i.name,
                "pk":i.pk
            })
        return temp


    price_policy=serializers.SerializerMethodField()
    def get_price_policy(self,obj):
        temp=[]
        course=obj.course
        ctype = ContentType.objects.get_for_model(course)
        price_policy_list=PricePolicy.objects.filter(content_type=ctype,object_id=course.id).all()

        for i in price_policy_list:
            temp.append({
                "time":i.get_valid_period_display(),
                "price":i.price
            })
        return temp


    chapters = serializers.SerializerMethodField()
    def get_chapters(self,obj):
        temp = []

        course = obj.course
        chapters = course.chapter_set.all()
        for chapter in chapters:
            coursesections = CourseSection.objects.filter(chapter=chapter)
            temp2 = []
            for ccoursesection in coursesections:

                temp2.append(ccoursesection.name)
            temp.append({
                "chapter_name":chapter.name,
                "chapter_num":chapter.num,
                "coursesections":temp2
            })

        return temp



