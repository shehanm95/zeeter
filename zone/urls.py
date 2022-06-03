from  .import views
from django.urls import path

app_anem = 'zone'
urlpatterns = [
    path('', views.home , name = 'home'),
]