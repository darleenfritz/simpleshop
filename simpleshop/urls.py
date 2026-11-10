"""
URL configuration for simpleshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Simple Shop swagger UI",
        default_version='v1.0'
    ),
    public = True,
    permission_classes =(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('customermanager.urls')),
    path('addresses/', include('addressmanager.urls')),
    path('products/', include('productmanager.urls')),
    path('cart/', include('cartmanager.urls')),
    path('api/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]
# Notizen
# product/ -> GET , POST
# product/<id> -> GET, PUT, DELETE
