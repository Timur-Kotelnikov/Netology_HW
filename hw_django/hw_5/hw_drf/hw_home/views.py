from rest_framework.generics import UpdateAPIView, CreateAPIView, RetrieveAPIView, ListAPIView
from .models import Sensor, Measurement
from .serializers import SensorUpdateSerializer, MeasurementSerializer, SensorDescriptionSerializer, \
    SensorSerializer


class GetAllSensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateNewSensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDescriptionSerializer


class CreateNewMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class GetAllMeasurements(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class EditExistingSensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer
