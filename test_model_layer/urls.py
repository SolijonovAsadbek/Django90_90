from django.urls import path

from test_model_layer import views

urlpatterns = [
    path('', views.export_excel, name='export-excel'),
]
