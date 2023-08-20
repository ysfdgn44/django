from rest_framework.viewsets import ModelViewSet
from .serializers import Todo, TodoSerializer
from rest_framework.pagination import PageNumberPagination
from .paginations import PaginationNumber
from django_filters.rest_framework import DjangoFilterBackend
# PageNumberPagination.page_size = 25
# PageNumberPagination.page_size_query_param='adet'
# PageNumberPagination.page_query_param='sayfa'

class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = PaginationNumber
    # def get_queryset(self):
    #     return self.queryset.filter(is_done=True)
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['is_done', 'id', 'priority']