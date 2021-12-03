from django.urls import path
from .views import home_view,register

app_name = "register"

urlpatterns = [
    path('', home_view, name="home"),
    path('register_patient/', register, name="register_patient"),

]
