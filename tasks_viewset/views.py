#utilizado el modelo de otra app (TASKS)
#reutilizando cosas hechas en otra app
from tasks.models import Todo
from tasks.serializers import TodoSerializer
from rest_framework.viewsets import ModelViewSet, \
	ReadOnlyModelViewSet
from .pagination import SimplePagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action

from rest_framework.throttling import \
	AnonRateThrottle, UserRateThrottle

class TaskViewSet(ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer
	pagination_class = SimplePagination
	#filtrar x campos especificos
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields = ['title', 'body']
	search_fields = ['title', 'body']

	throttle_classes = [UserRateThrottle]

	#url y el asename
	#agrega funcioes extra a una clase 
	@action(detail=True, methods=['get'], url_path="detalle", url_name="detalle")
	def detalle(self, request, pk=None):
		return self.retrieve(request, pk)


class TaskReadOnlyViewSet(ReadOnlyModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

	filter_backends = [filters.SearchFilter]
	search_fields = ['title', 'body']

