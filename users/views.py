from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import generics, status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SingUpSerializer, GetUserSerializer
from .tokens import create_jwt_pair_for_user
from .models import User


class SignUpView(generics.GenericAPIView):
	serializer_class = SingUpSerializer

	def post(self, request: Request):
		data = request.data

		serializer = self.serializer_class(data=data)

		if serializer.is_valid():
			serializer.save()

			resp ={
				"message":"Usuario creado correctamente",
				"data": serializer.data
			}
			return Response(data=resp, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=400)

class LoginView(APIView):

	def post(self, request: Request):
		email = request.data.get('email')
		password = request.data.get('password')
		#valida si las credenciales son validas
		user = authenticate(email=email, password=password)

		if user is not None:
			#genera el token
			tokens = create_jwt_pair_for_user(user)
			resp = {
				"message":"Logeado correctamente",
				"email": email,
				"token": tokens
			}
			return Response(data=resp, status=status.HTTP_200_OK)
		else:
			return Response(data={
				"message": "Correo o contraseña invalida"
			})

	def get(self, request: Request):
		content = {"user": str(request.user), "auth": str(request.auth)}

		return Response(data=content, status=status.HTTP_200_OK)

# verifica si el user está logeado o no?
class GetUsers(viewsets.ReadOnlyModelViewSet):
	serializer_class = GetUserSerializer
	queryset = User.objects.all()
