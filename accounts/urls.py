from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('dashboard/', views.home, name="home"),
    path('logout/',views.logoutUser, name="logout"),
    path('responses/',views.viewResponse, name="responses"),
    path('uploaddata/',views.uploadData, name="uploaddata"),
    path('testsurvey/',views.testSurvey, name="testSurvey"),
]