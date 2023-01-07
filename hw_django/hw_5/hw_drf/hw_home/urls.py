from django.urls import path

from .views import CreateNewSensor, EditExistingSensor, CreateNewMeasurement, GetAllSensors, GetAllMeasurements

urlpatterns = [
    path('sensor_add/<pk>/', CreateNewSensor.as_view()),
    path('sensor/<pk>/', EditExistingSensor.as_view()),
    path('measurements/', GetAllMeasurements.as_view()),
    path('measurement_add/', CreateNewMeasurement.as_view()),
    path('sensors/', GetAllSensors.as_view())
]