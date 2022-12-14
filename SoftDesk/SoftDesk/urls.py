"""SoftDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from connexion.views import InscriptionAPIView
from api.views import ProjetViewset, UserViewset, ProblemeViewset, CommentaireViewset

router = routers.SimpleRouter()
router.register("projects", ProjetViewset, basename="projects")

user_router = routers.NestedSimpleRouter(router, "projects", lookup="projects")
user_router.register("users", UserViewset, basename="users")

issues_router = routers.NestedSimpleRouter(router, "projects", lookup="projects")
issues_router.register("issues", ProblemeViewset, basename="issues")

comments_router = routers.NestedSimpleRouter(issues_router, "issues",
                                             lookup="issues")
comments_router.register("comments", CommentaireViewset, basename="comments")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", TokenObtainPairView.as_view()),
    path("login/refresh/", TokenRefreshView.as_view()),
    path("signup/", InscriptionAPIView.as_view()),
    path("", include(router.urls)),
    path("", include(user_router.urls)),
    path("", include(issues_router.urls)),
    path("", include(comments_router.urls)),
]
