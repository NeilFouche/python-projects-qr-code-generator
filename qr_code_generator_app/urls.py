from django.urls import path
from . import views

app_name = "qr_code_generator_app"
urlpatterns = [
    path("", views.generate_qr, name="generate_qr"),
    path("download/", views.download_qr, name="download_qr")
]