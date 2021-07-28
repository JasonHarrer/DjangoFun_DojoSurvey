from django.urls import path
from . import views

urlpatterns = [
                path('', views.index),
                path('process', views.process_dojo_survey),
                path('result', views.result)
              ]
