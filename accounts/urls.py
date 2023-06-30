from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_app, name='start'),
    path('register/',views.register, name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
]

