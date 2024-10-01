from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Doctors, Direction
from .serializers import DoctorSerializer, DirectionSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

class DoctorPagination(PageNumberPagination):
    page_size = 2

class DirectionListView(ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class DoctorListView(ListAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['directions', 'experience']
    ordering_fields = ['birth_date', 'experience']

class DoctorDetailView(RetrieveAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer

class DirectionDetailView(RetrieveAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer