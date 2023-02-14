#la convención es poner en API lo q hasta ahora iba en view
from .models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
import random
from rest_framework.response import Response

#from twilio.rest import Client

class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	#q genere el codigo solo cuando está en update
	def get_throttles(self):
		#puede ser list, retrieve, update, create, destroy
		if self.action == "update":
			# aca vamos a decir que use el throttle_scope
			self.throttle_scope = "generate_code"
		return super().get_throttles()
			
	def update(self, request, pk):
		user = User.objects.get(pk=pk)
		code = random.randint(1000, 9999)
		# si queremos aumentar datos al request
		#  primero debemos hacerlo mutable
		request.data._mutable = True
		request.data["code"] = code
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			# twilio credentials
			# TWILIO_ACCOUNT_SID = "AC193846e53eb15555a77e162a1f8fa611"
			# TWILIO_AUTH_TOKEN = "e57dfba0462919565d7ce478389f13d4"
			# Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN).messages.create(
			# 	messaging_service_sid='MG7b8723096f42451a0cbe6eb423a38155', 
			# 	body=f"Tu codigo es {code}",      
			# 	to='+51967617166'
			# )
			serializer.save()

			return Response({
				"ok": True,
				"message": "user updated"
			})

class UserViewGenericViewSet(RetrieveModelMixin,GenericViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	# campo de la URL
	lookup_field = 'username'

	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)

#todo| LINDER
from rest_framework.views import APIView
from .models import User


# class UserApiView(APIView):

# 	throttle_scope = "generate_code"

# 	def put(self, request,id):
# 		user = User.objects.get(pk=id)
# 		#ingresa un codigo random de 4 digitod
# 		code = random.randint(1000,9999)
# 		#guardar en la db
# 		user.code = code
# 		user.save()
