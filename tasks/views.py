from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class TaskView(ModelViewSet):
	#array de permisos
	#permission_classes = [IsAuthenticated]
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


#todo| Clase 12-dic
#API VIEW BASADO EN CLASES

class TodoView(APIView):
	'''APIView YA TIENE GET, POST, PUT, DELETE ,PATCH'''
	def get(self, request):
		todo = Todo.objects.all().order_by('-id')
		serializer = TodoSerializer(todo, many=True)
		return Response({
			"ok": True,
			"data": serializer.data
		})

	def post(self, request):
		serializer = TodoSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return  Response({
				"ok": True,
				"message": "TODO creado"
			}, status=status.HTTP_201_CREATED)
		
		#si no es valido:
		return Response({
			"ok": False,
			"message": serializer.errors
		}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TodoViewDetail(APIView):
	"""Listar por ID"""
	def get(self, request, id):
		todo = get_object_or_404(Todo, pk=id)
		serializer = TodoSerializer(todo)

		return Response({
			"ok": True,
			"data": serializer.data
		})
	
	"""Actualizar por ID"""
	def put(self, request, id):
		todo = get_object_or_404(Todo, pk=id)
		#envia objeto y la info nueva
		serializer = TodoSerializer(todo, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return  Response({
				"ok": True,
				"message": "TODO actualizado"
			})

	"""Eliminar por ID"""
	def delete(self, request, id):
		todo = get_object_or_404(Todo, pk=id)
		todo.delete()

		return  Response({
				"ok": True,
				"message": "TODO eliminado"
			})