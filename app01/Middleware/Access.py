from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,HttpResponse

class Push(MiddlewareMixin):

    def process_response(self,request,response):

        if request.method == "OPTIONS":

            response["Access-Control-Allow-Headers"] = "Content-Type"

        response["Access-Control-Allow-Origin"] = "*"

        return response
