from rest_framework import serializers
from rest_framework import viewsets, generics
from rest_framework.viewsets import ModelViewSet

from vehicle.models import Car, Moto
from vehicle.serializers import CarSerializer, MotoSerializer, MilageSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoSerializer


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()

class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()

class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()

class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()

class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializer


