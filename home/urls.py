from . import views
from django.urls import path

urlpatterns = [
    path('', views.render_home, name='home'),
]
