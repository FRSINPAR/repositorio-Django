"""
URL configuration for TestConnectSQL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from appTest.views import create_products, list_products, mostrar_datos, mostrar_datosSQL, list_afipcodigos, list_afiptipocomprobante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appTest/create_products/', create_products),
    path('appTest/list_products/', list_products),
    path('appTest/lista_prueba/', mostrar_datosSQL),
    path('appTest/afipcodigos/', list_afipcodigos, name='list_afipcodigos'),
    path('appTest/afiptipocomprobante/', list_afiptipocomprobante, name='list_afiptipocomprobante'),
]
