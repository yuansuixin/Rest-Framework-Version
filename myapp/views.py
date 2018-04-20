from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.request import Request


# class ParamVersion(object):
#     def determin_version(self,request):
#         version = request.query_params.get('version')
#         return version
#

from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
# class UsersView(APIView):
#     versioning_class = QueryParameterVersioning
#     def get(self,request,*args,**kwargs):
#         print(request.version)
#         return HttpResponse('用户列表')

class UsersView(APIView):
    def get(self,request,*args,**kwargs):
        self.dispatch()
        # 1.获取版本
        print(request.version)
        # 2.获取版本的对象
        print(request.versioning_scheme)
        # 3. 内置的反向生成url，不需要指定版本，会自动生成，其实是当前url的版本
        u1 = request.versioning_scheme.reverse(viewname='uuu',request=request)
        print(u1)
        # 使用Django内置的反向生成url,必须要指定版本
        u2 = reverse(viewname='uuu',kwargs={'version':1})
        print(u2)
        return HttpResponse('用户列表')


class DjangoView(APIView):
    def get(self,request):
        print(type(request._request))
        from django.core.handlers.wsgi import WSGIRequest

        return HttpResponse('post 和body')