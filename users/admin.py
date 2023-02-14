from django.contrib import admin
from .models import User
#agregarlo al admin
admin.site.register(User)