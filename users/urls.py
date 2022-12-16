from rest_framework.routers import DefaultRouter
from .api import UserViewSet, UserViewGenericViewSet
from .routers import CustomRouter
#todo| lagardo
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt.views import(
	TokenObtainPairView,
	TokenRefreshView,
	TokenVerifyView
)
from . import views
#todo| FIN lagardo

user_router = DefaultRouter()
user_custom_router = CustomRouter()

user_router.register(r"users", UserViewSet, basename="users")
user_custom_router.register(r"custom/users", \
	UserViewGenericViewSet, basename="users_custom")

#todo| lagardo
router = routers.DefaultRouter()
router.register('', views.GetUsers)
urlpatterns = [
	#si no funciona, probar cion / adelante
	path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name= "login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name= "jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name= "token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name= "token_verify"),

]
urlpatterns += router.urls
#todo| FIN lagardo

urlpatterns += user_router.urls
urlpatterns += user_custom_router.urls

