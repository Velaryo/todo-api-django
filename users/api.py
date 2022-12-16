#la convención es poner en API lo q hasta ahora iba en view
from .models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserViewGenericViewSet(RetrieveModelMixin,GenericViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	# campo de la URL
	lookup_field = 'username'

	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)