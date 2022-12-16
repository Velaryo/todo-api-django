from django.db import models

#todo| Linder
# class User(models.Model):
# 	username = models.CharField(max_length=200)
# 	password = models.CharField(max_length=200)
# 	realname = models.CharField(max_length=100)
# 	created_at = models.DateTimeField(auto_now_add=True)

# 	class Meta:
# 		db_table = "users"

#todo| lagardo
from django.contrib.auth.base_user import BaseUserManager
#clase customizadora
class CustomUserManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
	
	def create_superuser(self, email, password, **extra_fields):
		#EXTRAFIELS SON LOS CAMPOS EXTRA - AGREGADOR
		extra_fields.setdefault("is_stuff", True)
		extra_fields.setdefault("is_superuser", True)

		if extra_fields.get("is_stuff") is not True:
			raise ValueError("El super user necesita q is_stuff = True")
		if extra_fields.get("is_superuser") is not True:
			raise ValueError("El super user necesita q is_superuser = True")

		return self.create_user(email, password=password, **extra_fields)

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	email = models.CharField(max_length=80, unique=True, default="no@email.com")
	username = models.CharField(max_length=45)
	date_of_birth = models.DateField(null=True)

	objects = CustomUserManager()
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["username"]

	def __str__(self)-> str:
		return self.email