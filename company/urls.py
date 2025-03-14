"""
URL configuration for company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/$
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
from django.urls import path, include
from rest_framework import routers
from products import views

# Setup of the API router by registering Viewsets to a path
router = routers.DefaultRouter()
router.register(r"products", views.ProductViewSet)
router.register(r"manufacturers", views.ManufacturerViewSet)
router.register(r"thermaltypes", views.ThermalTypeViewSet)

urlpatterns = [
    # Attaching the router the url paths of the project
    path("", include(router.urls)),
    # Attaching the default django admin/superuser endpoints to the project url paths
    path("admin/", admin.site.urls),
    # Attaching djangorestframework authentication to the project url paths
    path("api-auth", include("rest_framework.urls")),
]
