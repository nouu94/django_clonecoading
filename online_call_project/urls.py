"""online_call_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))

    어떠한  url로 들어갈 때 어떠한 view 안에 있는 shop 이라는 함수를 호출할 것인가?
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('delivery/', include('delivery.urls')),
    path('boss/', include('boss.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
