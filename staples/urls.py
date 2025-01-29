from . import views
from django.urls import path

urlpatterns = [
    path('staples', views.render_staples_list, name='staples'),
]
