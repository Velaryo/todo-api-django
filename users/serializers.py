from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"
		#esto no es encesario xq tiene auto_now True 
		# (en el model). Se pone xq así lo pide el taller
		#read_only_fields = "created_at"

		