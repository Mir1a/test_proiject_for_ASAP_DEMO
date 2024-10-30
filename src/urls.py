"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.urls import router as user_router
from author.urls import router as author_router
from book.urls import router as book_router

api_urlpatterns = [
    path('users/', include(user_router.urls)),
    path('authors/', include(author_router.urls)),
    path('books/', include(book_router.urls)),
]

swagger_api = [
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-swagger'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='api-schema'), name='api-redoc'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]

authorization_api = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += swagger_api \
               + api_urlpatterns \
               + authorization_api

