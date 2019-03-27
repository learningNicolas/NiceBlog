"""NiceBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from blog import module

from django.conf.urls import  url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
#    path('admin/', admin.site.urls),
# module 路由
    path('',module.index),
    path('module/index.html', module.moduleIndex, name='moduleIndex'),
    path('module/detail.html', module.moduleDetail, name='moduleDetail'),
    url(r'^admin/', admin.site.urls),
# views 接口
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

